#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
deploy_to_library.py — 把工作台一键落地到资料库「我的文档」。

用法（client 模式）：
    WB_TOKEN=<token> python deploy_to_library.py
    WB_TOKEN=<token> python deploy_to_library.py --manifest custom.json --space-id <id>

- token 从环境变量读取（由 connect_open_platform 取得），不写文件、不回显。
- 省略 --space-id 时，建库与上传都默认落「我的文档」。
- 依赖 library 技能脚本（database/create_database.py, batch_add_database_records.py,
  page/import_html.py）；脚本目录自动探测（CODEBUDDY_PLUGIN_ROOT 或插件缓存）。
"""
import argparse, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL_ROOT = os.path.dirname(os.path.dirname(HERE))  # assets/deploy -> skill root


def find_library():
    p = os.environ.get("CODEBUDDY_PLUGIN_ROOT")
    if p:
        cand = os.path.join(p, "skills", "library")
        if os.path.isdir(os.path.join(cand, "database")) and os.path.isdir(os.path.join(cand, "page")):
            return cand
    base = os.path.expanduser("~/.workbuddy/plugins/cache/workbuddy-builtin")
    if os.path.isdir(base):
        for root, dirs, files in os.walk(base):
            if "database" in dirs and "page" in dirs:
                if os.path.exists(os.path.join(root, "database", "create_database.py")) \
                   and os.path.exists(os.path.join(root, "page", "import_html.py")):
                    return root
    raise FileNotFoundError("找不到 library 技能脚本目录（database/page）")


def run(script, args, token):
    cmd = [sys.executable, script, "--token-stdin"] + args
    res = subprocess.run(cmd, input=token, capture_output=True, text=True, timeout=90)
    out = (res.stdout or "").strip()
    if out.startswith("KS_IMPORT_OK"):
        m = re.search(r"KS_IMPORT_OK\s+(\{.*\})", out, re.S)
        return json.loads(m.group(1)) if m else {"raw": out}
    try:
        return json.loads(out)
    except Exception:
        return {"raw": out, "stderr": (res.stderr or "").strip()[:300]}


def main():
    ap = argparse.ArgumentParser(add_help=False)
    ap.add_argument("--manifest", default=os.path.join(HERE, "manifest.json"))
    ap.add_argument("--html", default=None)
    ap.add_argument("--space-id", default="")
    ap.add_argument("--token-env", default="WB_TOKEN")
    args, _ = ap.parse_known_args()

    token = os.environ.get(args.token_env, "")
    if not token:
        print(json.dumps({"error": f"缺少环境变量 {args.token_env}（请先从 connect_open_platform 取 token 注入）"}))
        sys.exit(1)

    lib = find_library()
    db_dir = os.path.join(lib, "database")
    page_dir = os.path.join(lib, "page")

    manifest = json.load(open(args.manifest, encoding="utf-8"))
    html_path = args.html or os.path.join(SKILL_ROOT, manifest.get("html", ""))
    if not os.path.isfile(html_path):
        print(json.dumps({"error": f"HTML 不存在: {html_path}"}))
        sys.exit(1)

    space_body = {"space_id": args.space_id} if args.space_id else {}

    result = {"databases": {}, "page": {}, "errors": []}
    db_ids = []
    for mod in manifest["modules"]:
        schema = {"title": mod["title"], "properties": mod["properties"]}
        schema.update(space_body)
        r = run(os.path.join(db_dir, "create_database.py"),
                ["--schema", json.dumps(schema, ensure_ascii=False)], token)
        if "database_id" not in r:
            result["errors"].append({"module": mod["name"], "step": "create", "detail": r})
            continue
        db_id = r["database_id"]
        result["databases"][mod["name"]] = db_id
        db_ids.append(db_id)
        if mod.get("seed"):
            r2 = run(os.path.join(db_dir, "batch_add_database_records.py"),
                     ["--database-id", db_id, "--records", json.dumps(mod["seed"], ensure_ascii=False)], token)
            if "error" in r2:
                result["errors"].append({"module": mod["name"], "step": "seed", "detail": r2})

    imp_args = [html_path, "--databases", json.dumps([{"id": i} for i in db_ids], ensure_ascii=False)]
    if args.space_id:
        imp_args += ["--space-id", args.space_id]
    r3 = run(os.path.join(page_dir, "import_html.py"), imp_args, token)
    if "node_block_id" in r3:
        result["page"] = {"node_block_id": r3.get("node_block_id"), "url": r3.get("url")}
    else:
        result["errors"].append({"step": "import_html", "detail": r3})

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

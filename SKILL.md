---
name: workbench-builder
slug: workbuddy-workbench-builder
displayName: Workbench Builder（工作台构建器）
description: 基于 WorkBuddy 资料库，零依赖单文件交付可插拔的个人/团队工作台。把用户的待办/记忆/指标聚合为一个可离线 HTML 工作台，数据自动落到资料库 CSV 并托管为在线 page、自动双向同步。内置 19 模块、4 布局、13 风格预设、11 角色配方；存储层已封装在种子，选模块即自动确定页面元素与数据库字段。当用户说"搭个工作台/做个个人面板/用资料库建仪表盘/给我一个本地可运行的看板/每天自动更新工作台数据"时使用。
version: 1.4.0
summary: 零依赖单文件工作台构建器；内置 19 模块/4 布局/13 风格/11 角色配方；数据落资料库 CSV 并托管在线 page，自动双向同步；存储层已封装，改 WORKBENCH_CONFIG 即可装配，选模块即自动适配页面元素与数据结构。v1.4.0：借鉴「缮语·企业 Claw」经营工作台——新增 briefing 今日简报/insight 外部洞察/approvals 审批中心/cron 定时任务 4 模块与 claw 企业蓝风格（含绿/橙/红状态色 --warn token），新增企业经营配方。
author: Remo
level: personal
license: MIT
agent_created: true
metadata:
  spec_version: "V1.0"
  data_classification: L2
---

# 工作台构建器（Workbench Builder）

把用户的零散数据、待办、记忆、指标，聚合为一个**零依赖、单文件、可离线、可分享**的 HTML 工作台；所有持久化数据落到 WorkBuddy **资料库**的 CSV(database) 节点，并支持以在线 page 节点托管。

## 核心原则（铁律）

1. **数据权威在资料库**：持久化数据最终落资料库 CSV(database) 节点；工作台 HTML 是视图 + 运行时编辑层。
2. **交付终态 = 资料库「我的文档」**：最终交付必须是资料库节点（在线 page + 各模块 CSV），二者默认落「我的文档」（省略 `--space-id`）；本地 HTML 仅为生成中间产物。
3. **单文件内联离线**：HTML 不依赖任何 CDN/外部运行时；CSS/JS/图标(SVG)/图片(data URI) 全内联，可断网双击打开。
4. **一切可插拔**：模块由注册表驱动、UI 由模板驱动，用户从现成模板直接选，而非从零描述。
5. **存储层已封装（重要护栏）**：持久化、双向同步、本地降级已在 `examples/reference-workbench.html` 实现。**AI 不得重写持久化层、不得回退到 localStorage 直读 CSV**；新模块沿用全局 `toCSV(rows, schema)` 约定，无需各自实现存储。
6. **默认不联网不扫描**：仅处理用户显式给出的数据/路径；备份等联网动作需用户明确开启。

## 装配流程（以种子为准）

> 唯一权威种子：`examples/reference-workbench.html`（已内联 15 模块 + 4 布局 + 5 风格，开箱即用）。**不要从零重写**，按 `WORKBENCH_CONFIG` 改配置即可。

1. **需求澄清**：问清要哪些模块、UI 风格、有无存量数据（及来源：本地 CSV/Excel、微信/腾讯文档、飞书、Notion 导出等）。
2. **选模块 / UI**：从 `MODULE_REGISTRY`（15 模块）与 4 套布局、5 套风格预设中选；改 `WORKBENCH_CONFIG` 即可。**模块自带 `schema`+`render`，选模块即自动确定页面元素与数据库字段，无需手动适配结构。**
3. **改种子**：复制种子，按第 2 步修改顶部 `WORKBENCH_CONFIG`（`title/ui/theme/style/modules`，可选 `accent`、`databases`）；角色场景直接套用 `references/presets.md` 的 10 个配方（布局×风格×模块已按角色差异化校准，避免千篇一律）；存量数据作各模块 `seed` 或保持默认示例。
4. **落库交付**：优先跑 `assets/deploy/deploy_to_library.py`（读 `manifest.json` 的 schema/seed，自动 `find_library()` 建库 + 灌数 + 上传 HTML 到「我的文档」）。token 按下方「鉴权」注入 `WB_TOKEN`。
5. **（可选）自动更新**：含新闻/行情等动态模块时，用 `automation_update` 配置每日追加更新（尽力而为，创建后立即手动验证一次）。
6. **（可选）跨平台备份**：用 `automation_update` 定时导出 CSV 到飞书/ima/github（单向，需用户确认目标节点）。

## 鉴权（落地资料库前必读）

- 运行模式：先 `python3 "${CODEBUDDY_SKILL_DIR}/runtime_context.py"` 判定 `mode`。
  - `sandbox`：auth-proxy 注入身份，直接跑。
  - `client`：每次网络命令前取 token——`ToolSearch connect_open_platform` → `DeferExecuteTool(skill_id="library")` 拿 token → `printf '%s' "<token>" | python3 <script> --token-stdin [args]`。token 不落地、不回显、不进产物。
- 库脚本根用 library 的 `${CODEBUDDY_SKILL_DIR}`（**不要**用失效的 `${CODEBUDDY_PLUGIN_ROOT}/skills/library/`）；`deploy_to_library.py` 内置 `find_library()` 会自动定位，无需手填。token 传给 deploy 脚本两种方式等价：`printf '%s' "<token>" | python deploy_to_library.py --token-stdin` 或 `WB_TOKEN=<token> python deploy_to_library.py`。
- 在线 page URL 是资料库文档编辑器（SPA，需登录态，SDK 由编辑器注入），**不要用浏览器/Playwright 直开验收**；在线侧验证用 `curl -s -o /dev/null -w "%{http_code}" <url>` 确认 200 + 用 library API 查 database 记录代替。
- 「我的文档」= 省略 `--space-id` / `space_id`。

## 自动化验收（交付前必过）

按 `references/checklist.md` + `references/test-cases.md` 跑六维验收（UI 交互 / 样式 / 布局 / 数据结构 / 一致性 / 自动化），P0 FAIL 一律退回修复后重跑，并产出验收报告。
**重点验证双向同步**：勾选待办/新增记录后，数据库确实更新、刷新前端后仍保持（证明持久化层生效，而非回退到 localStorage）。

## 装配参考（种子已内置）

- `WORKBENCH_CONFIG`：改这一个对象即可切换模块、UI、风格（含 `databases` 槽，由 deploy 脚本自动回填 `database_id`）。
- `MODULE_REGISTRY`：15 模块全部开箱即用，每模块含 `schema`/`seed`/`render`；CSV 读写复用全局 `toCSV(rows, schema)`（CSV 列 === schema === 落库字段）。
- `UI_LAYOUTS`：4 套布局；5 套风格预设（`default/macaron/ink/ocean/sunset`）共享同一组 CSS token，全局切换生效。
- **持久化已封装**：配置 `database_id` 后运行时直连资料库节点、自动双向同步；未配置（file:// 预览）自动降级到 localStorage 以保证可演示。**AI 无需理解其实现，只需用种子。**
- 更多模板见 `examples/templates/`（8 套完整模板）+ `examples/style-gallery.html`（预设预览器）。
- **权威种子 vs 视觉骨架**：`reference-workbench.html` 是唯一权威交付种子；`assets/ui/*.html` 仅为布局视觉骨架参考、非成品，切勿当种子交付。

## 扩展

- **新增模块**：`MODULE_REGISTRY` 加 `{type,title,icon,schema,seed,render}`，type 加进用户 `modules` 即可；CSV 复用全局 `toCSV`。
- **新增 UI 模板**：`UI_LAYOUTS` 加布局函数 + CSS（可放 `assets/ui/<新>.html` 作骨架参考，但仅视觉骨架、非交付种子）。

## 安全约束

- 涉及密码/key/身份证等敏感数据：停止，提示走合规通道。
- 不向用户回显 token / Cookie / 接口响应 / 本地绝对路径。
- 备份到外部平台前必须用户明确确认目标节点；删除资料库记录/字段仅按 library 规则在用户明确要求时执行。
- 不自动扫描用户目录；只处理用户显式给出的路径与数据。

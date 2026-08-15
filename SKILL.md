---
name: workbench-builder
slug: workbuddy-workbench-builder
displayName: Workbench Builder（工作台构建器）
description: 基于 WorkBuddy 资料库构建可插拔、单文件交付的个人/团队工作台。覆盖：①存量数据确认与导入(SQL/微信文档/飞书/Notion/多维表) ②可插拔模块选择(todo/mem/dashboard 等，含官方案例映射) ③多套 UI 模板选择 ④强制 CSV 存储 + 单文件内联 HTML 交付 ⑤每日信息源自动更新(新闻/行情等 automation 自动配置) ⑥可选跨平台备份(飞书/ima/github 定时任务)；并在交付前执行**自动化验收**(构建 checklist + 验收 test case)保证 UI 交互逻辑/样式配色/布局完整度与合理性/数据结构完整性/设计一致性/自动化任务符合预期的完整与合理。**本 skill 的交付终态是资料库「我的文档」里的在线内容：单文件内联 HTML 作为资料库 page 节点、各模块数据作为 CSV(database) 节点（同样默认落「我的文档」）；本地 HTML 仅为生成过程中的中间产物，不作为最终交付。** 当用户说"搭个工作台/做个个人面板/用资料库建仪表盘/给我一个本地可运行的看板/每天自动更新工作台数据"时使用。
version: 1.1.0
summary: 基于 WorkBuddy 资料库，零依赖单文件交付可插拔的个人/团队工作台；内置 15 模块（含「资源中心」公共资源聚合）、4 布局、5 风格预设，强制资料库 CSV 在线存储与双向同步，并含自动化验收。
author: Remo
level: personal
license: MIT
agent_created: true
metadata:
  spec_version: "V1.0"
  data_classification: L2
---

# 工作台构建器（Workbench Builder）

把用户的零散数据、待办、记忆、指标，聚合为一个**零依赖、单文件、可离线、可分享**的 HTML 工作台，并把所有持久化数据落到 WorkBuddy **资料库**的 CSV 节点里。

## 调研结论（设计依据）

经深度调研，本 skill 采用以下被验证过的模式：

- **可插拔架构 = Widget Registry 模式**：用 `Map<模块类型, 渲染器>` 注册模块，工作台容器只按配置渲染已启用模块，新增模块无需改动容器（参考 Open Mercato Dashboard Widgets、airrun 插件系统、dashboard-patterns）。
- **单文件交付 = 零依赖自包含 HTML**：Flashboard、GPU-Schedule-Board、FlowAI 模板均证明"纯 HTML/CSS/JS + 内联资源 + localStorage + CSV 导入导出 + CSS 变量设计 token + 深/浅色"可稳定离线运行、可邮件/微信发送。
- **强制存储 = 资料库 CSV 为权威源**：资料库 `database` 品类对标 Notion 多维表，支持建表、CRUD、`get_database_content` 导出 CSV、`import_csv` 导入；工作台 HTML 的"导出 CSV"产物即回写资料库 CSV 的载体。
- **跨平台备份 = 本地定时任务触发**：WorkBuddy `automation_update` 可在本地定时跑"导出 CSV → 上传到飞书文档/ima 知识库/github"，不保证双向完整同步（用户明确为"可选、尽力而为"）。

## 核心原则（铁律）

1. **数据权威在资料库**：任何"需要持久化"的数据，最终都要落到资料库 CSV(database) 节点；工作台 HTML 是**视图 + 运行时编辑层**（localStorage 暂存，CSV 导入/导出做同步）。
2. **交付终态 = 资料库「我的文档」**：最终交付必须是资料库节点——单文件内联 HTML 作为**在线 page** 节点、各模块数据作为 **CSV(database)** 节点，二者默认都落「我的文档」（省略 `--space-id` 即默认）。**本地 HTML 只是生成中间产物，绝不能只把本地文件交给用户当作交付。**
3. **单文件、内联、离线**：交付的 HTML 不依赖任何 CDN/外部运行时；CSS、JS、图标(SVG/emoji)、图片(data URI)全部内联；双击即用、可断网打开。
4. **一切可插拔**：模块由注册表驱动，UI 由模板驱动；用户从**现成模板直接选**，而非从零描述。
5. **默认不联网、不扫描**：仅处理用户显式给出的数据/路径；备份等联网动作需用户明确开启。

## 执行环境与鉴权（落地资料库前必读）

- 库脚本位置：资料库 library skill 的脚本根由 library 自身的 `${CODEBUDDY_SKILL_DIR}` 提供（实际位于 `~/.workbuddy/plugins/cache/workbuddy-builtin/skill-library/<版本>/` 下的 `database/`、`page/`）。**不要**写成 `${CODEBUDDY_PLUGIN_ROOT}/skills/library/`（该路径不存在）。落地时优先跑 `assets/deploy/deploy_to_library.py`，其内置 `find_library()` 会自动定位 library 脚本，无需手填路径（token 仍按下方注入）。若必须手写命令，用 `${CODEBUDDY_SKILL_DIR}/database/...` 与 `${CODEBUDDY_SKILL_DIR}/page/...`。
- 运行模式：先 `python3 "${CODEBUDDY_SKILL_DIR}/runtime_context.py"` 判定 `mode`。
  - `sandbox`：脚本不读 token，auth-proxy 注入身份，直接跑即可。
  - `client`：**每次**网络命令（create_database / batch_add / import_html 等）前必须取 token：
    1. `ToolSearch` 精确查 `connect_open_platform`；
    2. `DeferExecuteTool` 调 `connect_open_platform`，参数 `{"skill_id":"library"}`，拿到 `token`；
    3. 把 `token` 作为 stdin 首行传给脚本：`printf '%s' "<token>" | python3 <script> --token-stdin [args]`。
  - token 不落地、不写文件、不向用户回显、不进任何产物。
- **「我的文档」= 省略 `--space-id` / `space_id`**：建库与上传 HTML 都不传空间参数，后端默认落「我的文档」。

## 工作流（五步）

### 第 1 步 · 存量数据确认（必须先做）

目标：搞清楚用户有没有现成数据要进工作台，以及要不要调整结构。

1. 静默读取运行环境（`python3 "${CODEBUDDY_SKILL_DIR}/runtime_context.py"`，若走资料库需按 library SKILL 鉴权）。
2. 询问用户：「你是否有现成数据要导入工作台？」给出导入来源选项：
   - **本地 CSV / Excel**（最推荐，零依赖）：直接 `import_csv` / `import_excel` 进资料库。
   - **SQL 数据库**：本机无通用 SQL 连接器 → 请用户从数据库导出 CSV 后走本地 CSV 路径。
   - **微信文档 / 腾讯文档**（tencent-docs 已连接）：读取在线表/文档 → 转 CSV。
   - **飞书文档 / 多维表**（feishu 已连接）：用 lark-doc / lark-base 读取 → 转 CSV。
   - **Notion**（无连接器）：请用户在 Notion 导出 CSV 后走本地路径。
3. 若有历史记录：把导入的 CSV 列结构展示给用户，**确认是否需要调整字段/映射到某个模块 schema**（见 `references/module-catalog.md`）。
4. 确认后，用资料库 `database` 能力建表或 `import_csv` 落库，得到 `database_id` 列表（工作台生成时作为初始数据来源）。
5. 若用户无存量数据：跳过导入，进入第 2 步。

> 决策门：本步结束必须明确「有无存量 / 来源 / 已落库 database_id 列表 / 是否需要结构映射」。

### 第 2 步 · 需求板块确认（可插拔模块选择）

目标：确定工作台包含哪些模块，全部从注册表选。

1. 向用户展示**模块目录**（`references/module-catalog.md`），默认勾选 `todo`、`mem`、`dashboard`，并列出调研补充的候选模块（notes、links、kanban、calendar、ledger、habits、reading、contacts、inventory、journal、news）。
2. 让用户直接勾选或说"按推荐来"。若无偏好，默认 = `[todo, mem, dashboard]`。
3. 确认每个选中模块的字段是否需要自定义（一般直接用 catalog 里的默认 schema）。
4. 若第 1 步有存量数据，询问「这些 CSV 分别映射到哪个模块？」（按列名智能匹配 + 用户确认）。

> 决策门：产出 `modules = [选中的模块类型列表]` 与「模块↔资料库 database_id 映射」。

### 第 3 步 · UI 规范确认（模板 + 风格选择）

目标：选一套 UI 模板和一套全局风格预设，保证整个工作台视觉一致。

1. 展示 **UI 模板目录**（`references/ui-design-system.md`），提供 4 套可直接选用的布局：
   - `sidebar` 侧边栏导航 + 内容面板（控制台风，模块多时首选）
   - `cardGrid` 卡片网格马赛克（概览风，模块少/重可视首选）
   - `topnav` 顶部导航 + 标签页（简洁风）
   - `masonry` 瀑布流（展示/灵感墙风）
2. 展示 **UI 风格预设**（`examples/style-gallery.html` 可直接预览），5 套全局配色：
   - `default` 云灰蓝（中性专业）
   - `macaron` 马卡龙（粉彩柔润）
   - `ink` 墨韵（极简黑白）
   - `ocean` 深海（青蓝清爽）
   - `sunset` 晚霞（暖橙活力）
3. 若用户说"换个 UI 风格 / 换肤 / 换配色"等，**必须列出这 5 套预置风格让用户选择**，并说明切换会全局生效（所有布局、模块、图表同步换肤）。选择后把对应 `style` 键写进 `WORKBENCH_CONFIG.style`。
4. 让用户选布局（无偏好默认 `sidebar`）；可选深/浅色或跟随系统；`default` 风格下可再微调 `accent` 主题色，预置风格则使用其自带强调色。
5. 参考 `assets/ui/<模板>.html` 的布局与 CSS 变量设计 token（实际装配以 `examples/reference-workbench.html` 权威种子为准，见下方"装配参考"说明）。

> 决策门：产出 `ui = 模板键`、`theme = light|dark|auto`、`style = default|macaron|ink|ocean|sunset`、可选 `accent`（仅 default 风格生效）。

### 第 4 步 · 生成并交付到资料库「我的文档」（强制终态）

目标：产出单文件 HTML 工作台，并把数据与 HTML 落到资料库「我的文档」。**最终交付必须是资料库节点，本地 HTML 只是中间产物。**

- **a. 装配 HTML**：以 `examples/reference-workbench.html` 为种子（已内联全部 14 个模块与 4 套 UI 主题，是唯一的权威交付种子），按用户选择修改顶部 `WORKBENCH_CONFIG`：
  - `title`、`ui`（第 3 步）、`theme`、`modules`（第 2 步）。
  - 把第 1 步的存量数据作为各模块 `seed`，或保持默认示例数据。
- **b. 生成「构建 Check List」+「验收 Test Case」并自检**（交付前必须全部 PASS，模板见 `references/checklist.md` 与 `references/test-cases.md`）：
  - **构建 Check List（交付硬约束）**：单文件、无外部脚本/样式/CDN 引用；所有资源内联（图标/图片走 SVG 或 data URI）；可离线 `file://` 双击打开；含「导出 CSV / 导入 CSV / 主题切换 / 重置」工具栏。
  - **验收 Test Case（质量门）**：逐项执行 `references/test-cases.md` 的用例，覆盖 ①UI 交互逻辑（增删改、筛选、导入导出、主题切换可用且无 JS 报错）②样式配色（设计 token 全局唯一、深浅色对比达标）③布局完整度与合理性（4 套模板在 ≥1280px 与 ≤480px 视口下均不破版）④数据结构完整性（每个模块 CSV 列与 `schema` 一致、seed 可落库）⑤设计一致性（字体/间距/圆角/配色全局统一）⑥若配置了自动化任务，其 rrule / 范围 / prompt 完全符合预期。
  - 任一 P0 用例 FAIL 必须修复后重跑，禁止带缺陷交付；最终产出一份「验收报告」随交付一并给出（格式见 `references/test-cases.md` 末尾）。
- **c. 落库（强制存储 · CSV → 我的文档）**：对每个选中模块，在「我的文档」建 database 节点并灌入初始/存量数据。**推荐直接运行 `assets/deploy/deploy_to_library.py`**（自动 `find_library()` 定位 library 脚本、读 `manifest.json` 的 schema/seed 一键建库 + 灌数 + 上传 HTML，token 按 §鉴权 注入 `WB_TOKEN`）。若必须手写命令，库脚本根用 library 的 `${CODEBUDDY_SKILL_DIR}`（**不要**用失效的 `${CODEBUDDY_PLUGIN_ROOT}/skills/library/`）：
  - 建表（**不传 `--space-id`**，默认落「我的文档」）：
    `printf '%s' "<token>" | python3 "${CODEBUDDY_SKILL_DIR}/database/create_database.py" --token-stdin --schema '<schema JSON>'` → 拿到 `database_id`。
  - 灌数据（有数据时）：
    `printf '%s' "<token>" | python3 "${CODEBUDDY_SKILL_DIR}/database/batch_add_database_records.py" --token-stdin --database-id <id> --records '<records JSON>'`。
  - 回执每个模块的 `database_id` 与访问链接。
- **d. 交付 HTML（资料库 page → 我的文档）**：
  - 先过图片内链自检（本工作台无 `<img>` 外链，天然通过；命令见 library page `entry.md` §2）。
  - 上传为「我的文档」在线 page（**不传 `--space-id`**，并关联第 3 步的 database 节点）：
    `printf '%s' "<token>" | python3 "${CODEBUDDY_SKILL_DIR}/page/import_html.py" '<local.html>' --databases '[{"id":"<各database_id>"}]'`。
  - 解析 stdout 的 `KS_IMPORT_OK` 中的 `url` 与 `node_block_id`，回执给用户；拿到 `url` 后必须调预览组件打开。
- **e. 可复现脚本**：上述「建库 + 灌数 + 上传」已固化为编排脚本 `assets/deploy/deploy_to_library.py`，agent 直接改 `WORKBENCH_CONFIG` 后运行即可一键落地（token 仍按 §鉴权 注入，不写文件）。

> 决策门：产出「资料库 page 链接 + 各模块 database_id 清单 + 访问链接 + 验收报告（全部 P0 PASS）」——缺一不可。

### 第 5 步 · 每日信息源自动更新（可选，按需求自动配置）

目标：若工作台含"动态信息源"模块（新闻、行情、经营数据、外链聚合等），**自动配置**一个每日定时任务，把最新数据写回对应资料库 CSV，实现"工作台每日自更新"。

1. 在第 2 步选定的模块里识别"动态信息源"：如 `news`/`links` 或外部驱动的 `dashboard` 指标。若没有此类模块，跳过本步。
2. 询问用户更新频率与信息源（默认每日 08:00；来源如"AI 资讯 / 行业新闻 / 指定网站"）。无明确来源时默认用 WebSearch 抓取用户给定主题的最新内容。
3. **自动创建自动化任务**（用 `automation_update`，`scheduleType=recurring`，rrule 如 `FREQ=DAILY;BYHOUR=8;BYMINUTE=0`）：
   - `name`：`<工作台名>-每日信息源更新`
   - `prompt`（自包含，不含调度/空间细节）：「读取资料库 database `<database_id>`（<模块名>）当前数据；用 WebSearch/抓取获取 <主题> 的最新 N 条，整理为 <schema 字段> 的结构化记录；调用资料库 library 的 `batch_add_database_records` 仅**追加**新记录（不删不改旧数据）；若已存在同款则跳过；失败仅提示，不阻塞。」
   - `cwds`：本工作台项目目录；`status`：`ACTIVE`。
   - 自动化运行时按 library skill 的 client 模式鉴权（`connect_open_platform` 取 token，经 `--token-stdin` 注入），**不在 prompt 里写死任何凭证**。
4. 回执自动化任务的 `id`、下次运行时间、绑定到的 `database_id`，并提示用户可在设置里暂停/修改。

> ⚠️ **自动化任务创建为「尽力而为」**：`automation_update` 的创建结果以工具回执为准，不要在 prompt 里假设它一定生效。创建后**必须立即手动触发一次验证**（在自动化设置里点"运行一次"，或把 prompt 当一次普通任务跑），确认：能取到 token、能 `batch_add` 仅追加、不报错、不重复/不删旧数据。验收环节第 ⑥ 条（TC-AU-05）要求"模拟一次运行不报错"，**未验证的自动化任务不得声称"已配置可用"**。

> 决策门：若含动态模块，必须产出「自动化任务 id + rrule + 绑定 database_id + 自包含 prompt」且已实测运行一次；否则明确标注"无动态模块，跳过自动更新"。该任务也会进入第 6 步之后的「自动化验收环节」第 ⑥ 条被校验。

### 第 6 步 · 跨平台备份（可选，用户明确要才做）

目标：定时把工作台数据备份到外部平台，**尽力而为、不保证完整同步**。

1. 确认用户是否需要备份；若否，流程结束。
2. 给出可选备份目标（仅列出**已连接**的）：
   - 飞书文档 / 多维表（feishu 已连接）→ 用 lark-doc / lark-base 写入。
   - 腾讯文档（tencent-docs 已连接）→ 建在线表/文档。
   - GitHub（当前未连接）→ 提示先连接后再用 CLI 提交 CSV。
   - ima 知识库（当前未连接）→ 提示先连接 ima-mcp。
3. 用 `automation_update` 创建一个**本地定时任务**（如每日 03:00），prompt 大意：「导出工作台各模块 CSV（调用资料库 get_database_content 或读取本地 HTML 导出文件），上传到 <目标平台> 的 <节点/仓库>；失败仅提示，不阻塞。」
4. 明确告知用户：备份是单向、定时的，不是实时双向同步；首次需用户确认目标节点。

## 自动化验收环节（交付前必过）

生成完成后、把交付物交给用户前，必须跑一轮**自动化验收**，产出一份「验收报告」随交付一并给出。验收不是人工过目，而是按 `references/test-cases.md` 的用例逐条执行 + 按 `references/checklist.md` 的 P0/P1/P2 门判定。该环节对应第 4 步第 ② 小节的 6 个维度，缺一不可：

1. **UI 交互逻辑**：增/删/改/查、筛选、CSV 导入导出、主题切换、**风格预设切换**、重置——逐项点一遍，无 JS 报错、状态正确回写 localStorage 与导出文件。
2. **样式配色**：设计 token（CSS 变量）为全局唯一来源；深浅色对比度达标；无硬编码颜色漂移。
3. **布局完整度与合理性**：4 套模板在 ≥1280px 与 ≤480px 两种视口下均不破版、无重叠/溢出、信息层级清晰。
4. **数据结构完整性**：每个模块导出的 CSV 列名与 `schema` 完全一致；seed 能成功 `import_csv`/落库；空数据与超长字段不崩。
5. **设计一致性**：全局字体/字号阶梯/间距/圆角/配色统一；模块卡片风格一致；无混用两套视觉语言。
6. **自动化任务符合预期**（若第 5 步配置了）：rrule 正确、`cwds` 指向正确目录、prompt 自包含且引用了正确的 `database_id` 与模块 schema；模拟一次运行不报错。

**产出**：一份 Markdown 验收报告，列出每条 Test Case 的 PASS/FAIL + 证据（截图 / 控制台日志 / 落库回执），P0 FAIL 一律退回修复后重跑。报告模板与示例见 `references/test-cases.md` 末尾。

## 装配参考（agent 实操）

`examples/reference-workbench.html` 是**已完整可运行**的种子。它内置：

- `WORKBENCH_CONFIG`：改这一个对象即可切换模块、UI 模板与全局风格（直接满足"模板/风格选择"）。字段包括 `ui`、`theme`、`style`、`accent`、`modules`。
- `MODULE_REGISTRY`：**14 个模块全部开箱即用**（todo / mem / dashboard / notes / links / kanban / calendar / ledger / habits / reading / contacts / inventory / journal / news），每个含 `schema`（CSV 列）、`seed`、`render`；CSV 导入/导出由全局共享的 `toCSV(rows, schema)` 按各模块 `schema` 列名统一处理（CSV 列 === schema 字段 === 资料库落库字段），故各模块无需各自实现。
- `UI_LAYOUTS`：4 套布局（sidebar / cardGrid / topnav / masonry），CSS 变量驱动深/浅色与全局风格。
- **UI 风格预设系统**：种子内置 5 套风格（`default / macaron / ink / ocean / sunset`），共享同一组 CSS 设计 token；右上角工具栏有「🎨 风格」按钮，点击弹出预设列表供用户选择，切换全局生效并持久化到 `localStorage['wb:style']`。
- 工具栏：导出全部 CSV（打包下载）、导入 CSV、主题切换、风格切换、重置。
- 持久化：localStorage 运行时暂存；CSV 导入/导出与资料库 CSV 对齐。
- 更多模板示例见 `examples/templates/`（8 套完整模板：5 套预设+布局组合 + 3 套从 GitHub 优秀项目汲取灵感并改写为零依赖/同一 token 系统的导航启动页/玻璃仪表盘/质感起始页）和 `examples/style-gallery.html`（预设预览器）。

> **权威种子 vs 视觉骨架（重要）**：`examples/reference-workbench.html` 是**唯一的权威交付种子**——它已实现全部 14 个模块与 4 套 UI 主题，可直接改成任意工作台交付。**`assets/ui/<模板>.html` 仅是「布局/视觉骨架参考」，不是交付种子**（模块不全、仅展示布局），生成时一律以 `reference-workbench.html` 为准，切勿拿 `assets/ui/*.html` 当成品交付。

agent 落地时优先用 `assets/deploy/deploy_to_library.py`（读 `manifest.json` 的模块 schema/seed，自动建库 + 灌数 + 上传 HTML 到「我的文档」）：先按 §鉴权 取 token 注入 `WB_TOKEN` 环境变量，再 `python assets/deploy/deploy_to_library.py`。也可手动按第 4 步命令逐项落地。新增模块/UI 模板见下方"扩展"。

## 扩展

**新增模块**：在 `MODULE_REGISTRY` 增加一项 `{type,title,icon,schema,seed,render}`，并把 type 加进某用户的 `modules` 即可，容器无需改动；CSV 导入/导出复用全局共享的 `toCSV(rows, schema)`（按 `schema` 列名工作），无需模块各自实现。schema 字段定义参考 `references/module-catalog.md`。

**新增 UI 模板**：在 `UI_LAYOUTS` 增加一项布局函数 + 对应 CSS（可放一份 `assets/ui/<新模板>.html` 作骨架参考，但记得它只是视觉骨架、不能作为交付种子），把键加入 `references/ui-design-system.md`。

## 安全约束

- 涉及密码 / key / 身份证号等 L3/L4 敏感数据：停止，提示走合规通道；拿不准按敏感处理。
- 不向用户回显 token / Cookie / 接口原始响应 / 本地绝对路径。
- 备份到外部平台前必须用户明确确认目标节点；删除资料库记录/字段仅按 library 规则在用户明确要求时执行。
- 不自动扫描用户目录；只处理用户显式给出的路径与数据。

# 模块目录（Module Catalog）

工作台所有模块均为**可插拔**组件，由 `MODULE_REGISTRY` 注册、由 `WORKBENCH_CONFIG.modules` 启用。
每个模块定义包含：唯一 `type`、展示标题 `title`、图标 `icon`、CSV `schema`（决定资料库落库的列）、默认 `seed` 数据、`render` 渲染器、以及 `toCSV / fromCSV` 与资料库 CSV 对齐。

> 字段类型约定（对标资料库 database 字段）：`text` / `number` / `date` / `checkbox` / `url` / `select`。CSV 导入导出按这些列名对齐。

> **存储模型（v1.2 · 直连资料库 + 双向同步）**：模块在 `WORKBENCH_CONFIG.databases` 中配置了 `database_id` 时，运行时经平台注入的 `window.__SMART_PAGE__.database` **直读直写**对应 database 节点，**不再以 localStorage 为数据源**；前端改动自动 diff 为 add/update/delete 写回，外部（CSV/资料库）改动经定时轮询自动刷新前端。每行 `id` 字段即数据库 `_id`（主键对齐）。本地 `file://` 预览无 SDK 时优雅降级到 localStorage（仅演示）。新增模块无需改动数据层。

> **全部模块均已开箱即用**：下面的 15 个模块（含新增「资源中心 resources」）都已在 `examples/reference-workbench.html` 的 `MODULE_REGISTRY` 中实现（含 `render`/`seed`/`toCSV`/`fromCSV`），并已在 `assets/deploy/manifest.json` 中配好落库 schema/seed。差别只在于是否默认勾选，而非"有没有代码"。

---

## 默认推荐模块（建议必选）

### 1. todo · 待办清单
- **描述**：轻量任务管理，支持新增、勾选完成、删除、截止日期。
- **CSV schema**：`id(text), title(text), done(checkbox), due(date), created(date), priority(select:低/中/高)`
- **特性**：勾选即持久化、按优先级/截止日排序、完成率统计。
- **推荐场景**：几乎所有工作台默认带；个人效率、项目跟进。

### 2. mem · 速记 / 记忆碎片
- **描述**：一行式灵感、临时备忘、关键词记录，带标签。
- **CSV schema**：`id(text), text(text), tags(text), created(date)`
- **特性**：即时添加、标签筛选、全文搜索。
- **推荐场景**：脑子里的碎片想法、会议随手记。

### 3. dashboard · 概览仪表盘
- **描述**：聚合其它模块的指标（任务完成率、各模块条目数），并用 Canvas 画柱状/进度图；可加自定义 KPI。
- **CSV schema**：`id(text), name(text), value(number), unit(text)`
- **特性**：自动汇总各模块计数、内置进度环/柱状图（零依赖 Canvas）、自定义指标卡。
- **推荐场景**：想要"一屏看全局"时必选。

---

## 可选模块（按需勾选，均已实现）

> 以下模块同样已在种子中实现，只是默认不勾选；按工作台场景选用即可。

### 4. notes · 长笔记
- **描述**：带标题与正文的笔记卡片，支持编辑、删除、按更新时间排序。
- **CSV schema**：`id(text), title(text), body(text), updated(date)`
- **推荐场景**：比 mem 更正式的内容沉淀、周报草稿、读书摘要。

### 5. links · 收藏链接
- **描述**：网址书签，带标题、分类、URL。
- **CSV schema**：`id(text), title(text), url(url), category(text), created(date)`
- **推荐场景**：资料收集、竞品库、常用工具入口。

### 6. kanban · 看板
- **描述**：列（待办/进行中/完成等）+ 卡片拖拽的轻量看板。
- **CSV schema**：`id(text), title(text), column(select), order(number)`
- **推荐场景**：工作流可视化、项目阶段管理（比 todo 更重流程）。

### 7. calendar · 日历 / 日程
- **描述**：月历视图 + 当日事件列表，事件带日期与备注。
- **CSV schema**：`id(text), title(text), date(date), note(text)`
- **推荐场景**：排期、生日提醒、内容发布日历。

### 8. ledger · 流水账
- **描述**：收支记录，带金额、类别、收支方向，自动汇总余额。
- **CSV schema**：`id(text), item(text), amount(number), type(select:收入/支出), category(text), date(date)`
- **推荐场景**：个人记账、小本经营流水、活动预算。

### 9. habits · 习惯打卡
- **描述**：每日打卡矩阵，记录习惯与连续天数。
- **CSV schema**：`id(text), name(text), date(date), done(checkbox)`
- **推荐场景**：自律追踪、日更打卡。

### 10. reading · 阅读清单
- **描述**：书/文章清单，带状态（想读/在读/读完）与评分。
- **CSV schema**：`id(text), title(text), author(text), status(select:想读/在读/读完), rating(number)`
- **推荐场景**：知识管理、书单。

### 11. contacts · 联系人
- **描述**：姓名、电话、邮箱、备注。
- **CSV schema**：`id(text), name(text), phone(text), email(text), note(text)`
- **推荐场景**：轻量 CRM、供应商/客户台账。

### 12. inventory · 物品台账
- **描述**：物品名称、数量、位置、备注。
- **CSV schema**：`id(text), name(text), qty(number), location(text), note(text)`
- **推荐场景**：库存、固定资产、杂物登记。

### 13. journal · 日记
- **描述**：按日期写一段心情/复盘，时间线展示。
- **CSV schema**：`id(text), date(date), mood(select:😀/😐/😞), body(text)`
- **推荐场景**：每日复盘、情绪记录。

### 14. news · 每日信息源（动态更新）
- **描述**：新闻/资讯/外链聚合条目，带标题、摘要、来源、链接、日期；配合第 5 步「每日信息源自动更新」由自动化任务每日追加最新条目。
- **CSV schema**：`id(text), title(text), summary(text), source(text), url(url), date(date)`
- **推荐场景**：每日 AI 资讯、行业新闻、指定主题抓取的"工作台自更新"源。
- **注意**：该模块默认 seed 为空（等待自动化任务写入），UI 会提示"数据由每日自动化任务更新"。

### 15. resources · 资源中心
- **描述**：预置 24 个优质公共 API / 开放数据集 / 免费素材 / 效率参考站点，带名称、链接、分类、描述、免费方式；支持搜索与分类筛选。
- **CSV schema**：`id(text), name(text), url(url), category(text), desc(text), free(text), created(date)`
- **特性**：开箱即用的资源索引；支持增删改与分类筛选；可作为团队的"工具箱"或"数据源目录"。
- **推荐场景**：开发者工作台、数据团队资源索引、公共 API 速查。
- **预置 seed**：24 条（含 Open-Meteo / Frankfurter / REST Countries / NASA Open APIs / World Bank Open Data / Kaggle Datasets / arXiv / Project Gutenberg / Unsplash 等，覆盖开放 API、开放数据、公共知识、效率参考、免费素材 5 大类）。

---

## 默认推荐组合

> 角色化完整配方（含风格与布局绑定）见 `references/presets.md`，下表仅按场景给模块组合。

| 场景 | 推荐 modules |
|---|---|
| 极简个人面板 | `todo, mem, dashboard` |
| 知识工作者 | `todo, mem, notes, links, dashboard` |
| 项目协作 | `todo, kanban, calendar, dashboard` |
| 个人经营 | `todo, ledger, inventory, dashboard` |
| 自律成长 | `todo, habits, reading, journal, dashboard` |
| 开发者 / 数据团队 | `todo, mem, links, resources, dashboard` |

---

## 存量数据映射建议

导入 CSV 后，按列名智能匹配到模块 schema：
- 含 `title`/`完成`/`done` → `todo`
- 含 `text`/`内容`/`备注` 且无结构 → `mem` 或 `notes`
- 含 `url`/`链接` → `links`
- 含 `金额`/`amount` → `ledger`
- 含 `日期`/`date` 为主 → `calendar`

匹配后**展示给用户确认**是否调整字段名/增删列，再落库。

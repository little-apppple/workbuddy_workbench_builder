# workbench-builder

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
![WorkBuddy Skill](https://img.shields.io/badge/WorkBuddy-Skill-brightgreen)
![Modules](https://img.shields.io/badge/Modules-15-blue)
![UI Templates](https://img.shields.io/badge/UI%20Templates-4-orange)
![UI Styles](https://img.shields.io/badge/UI%20Styles-5-pink)
![Templates](https://img.shields.io/badge/Templates-8-purple)

基于 **WorkBuddy 资料库** 构建可插拔、单文件交付的个人 / 团队工作台 Skill。

把用户的零散数据（待办、记忆、指标、笔记、链接、看板、账本、习惯……）聚合为一个**零依赖、单文件、可离线、可分享**的 HTML 工作台，并把所有持久化数据落到 WorkBuddy **资料库**的 CSV(database) 节点里。

> ⚠️ **运行环境约束**：本 Skill **仅支持 WorkBuddy**。它深度依赖 WorkBuddy 的「资料库（Library）」「自动化（automation）」与「连接器 / MCP」能力——工作台的交付与持久化终态都建立在 WorkBuddy 资料库节点之上。它**不能**作为独立脚本在纯浏览器、或非 WorkBuddy 的 Agent 框架里直接运行。

![工作台动态演示（官方示例 · 生活工作台）](examples/demo.gif)

> 演示动画来自 WorkBuddy 资料库官方示例工作台「生活工作台」（生活全能），自上而下滚动浏览。更多说明见 [`examples/usage-example.md`](./examples/usage-example.md)。

---

## 特性

- **15 个开箱即用模块**（按需勾选）：`todo` / `mem` / `dashboard` / `notes` / `links` / `kanban` / `calendar` / `ledger` / `habits` / `reading` / `contacts` / `inventory` / `journal` / `news` / `resources`
- **4 套 UI 模板**：`sidebar`（侧边栏）/`cardGrid`（卡片网格）/`topnav`（顶部导航）/`masonry`（瀑布流），深 / 浅色主题
- **13 套全局 UI 风格预设**：原生 6 套（`default` 云灰蓝/`wb` WorkBuddy 官方/`macaron` 马卡龙/`ink` 墨韵/`ocean` 深海/`sunset` 晚霞）+ 社区经典 6 套（`nord` 北欧/`catppuccin` 奶咖/`rosepine` 玫瑰松/`tokyonight` 东京夜/`everforest` 常青/`mono` 纯粹），切换全局生效，图表/模块同步跟随
- **8 套模板示例**：5 套风格×布局内置组合 + 从 GitHub 优秀项目汲取灵感的导航启动页、玻璃仪表盘、质感起始页（均改写为同一 token 系统、零依赖）
- **强制资料库 CSV 落库**：工作台 HTML 是视图 + 运行时编辑层；最终交付是资料库「我的文档」里的在线 page + database 节点
- **在线存储 + 自动双向同步**：数据以资料库 `CSV(database)` 节点在线保存（跨设备、非本地文件）；工作台运行时直连资料库 database 节点，本地编辑自动 diff 写回，资料库变更经轮询自动刷新前端——无需手动导入导出 CSV。本地 `file://` 预览无 SDK 时优雅降级到 localStorage（仅演示）
- **每日信息源自动更新**：对 `news` / `links` / 外部驱动的 `dashboard` 等动态模块，自动配置 `automation_update` 每日定时把最新数据写回资料库 CSV（即修改存储、不改视图）
- **交付前自动化验收**：六维质量门（UI 交互逻辑 / 样式配色 / 布局完整度 / 数据结构 / 设计一致性 / 自动化任务符合预期），配套 Check List 与 Test Case

## 一句话安装（复制即用）

在 WorkBuddy 对话里**直接发这条消息**，即可把本 Skill 安装到你的环境：

> 安装 workbench-builder 这个 Skill，从 GitHub 仓库 `https://github.com/little-apppple/workbuddy_workbench_builder` 克隆到用户级 skills 目录（`~/.workbuddy/skills/workbench-builder`），跨项目复用。

如果你的 WorkBuddy 已接好技能市场，也可以更简版只说「安装 workbench-builder skill」，由技能市场自动定位并安装。装好后再用「搭个工作台」之类的自然语言即可唤起它。

## 安装

把本仓库放到 WorkBuddy 的 skills 目录即可（二选一）：

```bash
# 用户级（跨项目复用，推荐）
git clone https://github.com/little-apppple/workbuddy_workbench_builder.git ~/.workbuddy/skills/workbench-builder

# 或项目级（仅当前项目）
git clone https://github.com/little-apppple/workbuddy_workbench_builder.git <workspace>/.workbuddy/skills/workbench-builder
```

## 使用

在 WorkBuddy 中直接说，例如：

> 搭个工作台 / 做个个人面板 / 用资料库建仪表盘 / 每天自动更新工作台数据

Skill 会按五步流程执行：

1. **存量数据确认** —— 导入 CSV / Excel / 微信文档 / 飞书 / 腾讯文档等
2. **需求板块确认** —— 从模块目录勾选要包含的模块
3. **UI 规范确认** —— 选择模板、风格与主题
4. **生成并交付到资料库「我的文档」** —— 产出单文件内联 HTML + 各模块 CSV 落库（强制终态）
5. **每日信息源自动更新** —— 按需自动配置定时任务

> 交付终态 = 资料库节点：单文件内联 HTML 作为在线 **page** 节点、各模块数据作为 **CSV(database)** 节点，二者默认都落「我的文档」。本地 HTML 仅作为生成中间产物。

## 数据存储与自动双向同步

工作台的数据**不是在本地文件里**，而是**在线存储在 WorkBuddy 资料库**，并与工作台保持**自动双向同步**：

- **在线存储**：每个模块的数据都是一个资料库 `CSV(database)` 节点（云端）。交付的在线 `page`（单文件 HTML）只是视图，真正的「真相源」是资料库里的 CSV——换设备、重开对话，数据都在。
- **工作台 → 资料库（自动写回）**：在 HTML 工作台里增删改后，前端自动 diff 为 add/update/delete 写回对应 database 节点，**无需手动导出 CSV**。
- **资料库 → 工作台（自动拉取）**：资料库里的数据发生变化（你手动改、或被自动化任务 / API 接入 / 其他服务更新）后，前端经定时轮询自动刷新，**无需手动导入 CSV**。
- **自动化任务：改的是存储，不是视图**：每日信息源更新、API 接入等自动化任务，只往资料库 `CSV(database)` 节点**写数据（即修改存储）**，**从不直接改动 HTML 工作台本身**。工作台是存储的「只读投影」——下次打开 / 自动刷新时，视图自然反映存储里的最新值。自动化与界面由此解耦：无论谁改了存储，视图都保持一致。
- **本地降级**：`file://` 预览无平台 SDK 时，自动降级到 localStorage（仅演示用途，不持久化到云端）。

> 这样既能享受单文件 HTML 的离线查看 / 分享便利，又不必担心数据散落在各自电脑的本地文件里——所有人 / 所有设备看到的都是资料库里的同一份在线数据。

## 目录结构

```
workbench-builder/
├── SKILL.md                      # 主流程与约束（权威说明）
├── examples/
│   ├── reference-workbench.html     # 权威交付种子（已内联 15 模块 + 4 模板 + 5 风格）
│   ├── style-gallery.html           # 13 套 UI 风格预设预览器
│   ├── templates/                   # 完整模板示例（预设/布局组合 + 外部灵感改写）
│   │   ├── README.md                # 模板索引：清单 + 配色速览 + 风格切换 + 起点指引
│   │   ├── macaron-masonry.html     # 马卡龙 + 瀑布流
│   │   ├── ocean-sidebar.html       # 深海 + 侧边栏
│   │   ├── ink-topnav.html          # 墨韵 + 顶部导航
│   │   ├── default-sidebar.html     # 默认 + 侧边栏（出厂基线）
│   │   ├── sunset-cardgrid.html     # 晚霞 + 卡片网格
│   │   ├── launchpad.html           # 导航型工作台（灵感：NavHub）
│   │   ├── glass-dashboard.html     # 玻璃拟态仪表盘（灵感：ZASENJC/dashboard）
│   │   └── textured-startpage.html  # 质感可换起始页（灵感：snownico0722/index-main）
│   ├── official-cases.md            # 资料库官方案例 → 模块组合映射
│   ├── usage-example.md             # 使用示例 + 分步截图说明
│   ├── preview.png                  # 静态界面预览
│   └── demo.gif                     # 4 套模板 + 深色主题动态演示
├── assets/
│   ├── deploy/
│   │   ├── deploy_to_library.py  # 一键建库 + 灌数 + 上传 HTML
│   │   └── manifest.json         # 模块 schema / seed 定义
│   └── ui/                       # 4 套布局 / 视觉骨架参考（非交付种子）
│       ├── sidebar.html
│       ├── card-grid.html
│       ├── topnav-tabs.html
│       └── masonry.html
├── references/
│   ├── module-catalog.md         # 15 模块字段定义
│   ├── ui-design-system.md       # UI 模板 + 风格预设规范
│   ├── checklist.md              # 交付前 Check List（P0/P1/P2）
│   └── test-cases.md             # 六维验收 Test Case + 报告模板
└── LICENSE
```

## 扩展

- **新增模块**：在 `reference-workbench.html` 的 `MODULE_REGISTRY` 增加一项 `{type,title,icon,schema,seed,render}`，并把 type 加入 `WORKBENCH_CONFIG.modules`；CSV 导入 / 导出复用全局共享的 `toCSV(rows, schema)`。
- **新增 UI 模板**：在 `UI_LAYOUTS` 增加布局函数 + 对应 CSS（用 CSS 变量，勿写死颜色）。

## 接入其他服务（通过 API 文档）

除了内置的 15 个模块，本 Skill 支持**你提供任意第三方服务的 API 文档（OpenAPI / Swagger / 接口说明），据此把该服务接入为工作台的一个新模块**。接入后数据定期拉取并落到资料库 CSV，由 HTML 工作台统一展示，体验与内置模块一致。

典型流程：

1. **给文档** —— 把目标服务的 OpenAPI / Swagger JSON，或接口文档链接 / 文本交给 Skill。
2. **生成模块** —— Skill 解析接口，定义该模块的 `schema`（字段）+ `render`（展示），并产出调用该服务的适配层（鉴权、请求、字段映射）。
3. **落到资料库** —— 实际的外部请求走 WorkBuddy 的**自动化 / 连接器 / MCP** 能力代发（不在前端明文嵌密钥），拉取结果写入对应 `CSV(database)` 节点。
4. **工作台展示** —— HTML 模块直接读该 CSV 渲染。

> - 前端单文件**不包含**任何密钥 / 后端调用；所有外部请求由 WorkBuddy 侧中间层（自动化任务或连接器）代发，符合本 Skill「资料库是唯一持久化层」的设计。
> - 生成「API → 调用 Skill」的适配能力，可复用同生态的 `openapi2skill` 思路（基于 API 文档自动生成后端调用 skill）。
> - 目标服务若没有公开 API、但有网页 / 导出文件，也支持以「网页抓取 / 文件导入」方式接入（见「使用」第 1 步存量数据确认）。

## 许可证

[MIT](./LICENSE)

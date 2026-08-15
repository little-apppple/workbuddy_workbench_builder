# CHANGELOG — workbench-builder（工作台构建器）

所有版本的变更说明、Git 发布记录与 SkillHub 上线记录。日期为提交/发布当日（GMT+8）。

发布渠道：
- **GitHub**：`workbench-builder` 仓库 main 分支（源码权威）
- **SkillHub**：skillId `156574`，slug `workbuddy-workbench-builder`

格式约定参考 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)，版本号遵循语义化版本。

---

## [1.4.0] — 2026-08-15

> 借鉴「缮语·企业 Claw 工作台」，模块 15→19，风格 12→13，配方 10→11。

### 新增
- **briefing 今日简报**：晨会简报卡片，level 三色标签（正常/关注/预警，绿/橙/红），一键「✓ 确认」流转。
- **insight 外部洞察**：政策/技术/市场/竞争四类情报，impact 分级（重大利好/积极/中性/风险），关键数字 20px 高亮，「采纳」流转。
- **approvals 审批中心**：顶部 KPI（待审/已通过/已驳回）实时联动，支持通过/驳回操作，金额 number 字段。
- **cron 定时任务**：任务清单 + schedule 表达式，状态圆点（运行中/已暂停），暂停/启用切换。
- **claw 企业蓝风格**（第 13 套）：light 态 `#f0f2f5/#1677ff`（radius 8px 商务风），dark 态驾驶舱 `#0a1628/#3c8dff`（数据密集大屏）。
- **--warn 状态色 token**（`#e8a33d`）：与既有 `--ok/--danger` 构成绿/橙/红三态语义色。
- **角色配方 11**：企业经营 · 缘语配方（`briefing/insight/dashboard/approvals/cron/calendar` + claw）。

### 变更
- `examples/reference-workbench.html`：插入 4 个 register() 模块（schema+seed+render，保持 function() 种子风格）。
- `examples/style-gallery.html`：同步 claw 双态 CSS 与 PREVIEWS 第 13 项。
- `assets/deploy/manifest.json`：modules 15→19（properties 用 config 信封、seed 用类型信封）。
- `references/module-catalog.md`：新增第 16-19 节模块定义。
- `references/presets.md`：计数改 13 风格×4 布局×19 模块，追加配方 11。
- `references/ui-design-system.md`、`examples/templates/README.md`：计数与 claw 风格行同步。

### 验证
- Playwright 端到端回归 **20/20 PASS**：claw 生效与 dark bg 断言、4 新模块导航、seed 渲染数、确认/采纳/通过/暂停交互后 localStorage 持久化、13 风格卡片弹窗、宽窄屏不破版、0 console error。

### 发布记录
- Git：`b7e5205`（9 files, +714 / -16），已推送 main。
- SkillHub：v1.4.0 发布成功（27 文件白名单 zip，skillId 156574）。
- 灵感来源：用户资料库个人空间「缮语企业Claw工作台」page（UyZJdQx6PFnHkCRbzClQtt）及配套 40K 复刻提示词文档（1Lyk8ONZddyv4ZqnMyNPaf）。

---

## [1.3.0] — 2026-08-15

> 风格库 5→12 + 角色配方预设。

### 新增
- 7 套新风格（构成 12 套）：`mono` 极简单色、`nature` 自然绿意、`candy` 糖果撞色、`tech` 科技深色、`paper` 纸质文档、`neon` 霓虹、`claw` 前身蓝灰（本版定名）等。
- **10 个角色配方**（`references/presets.md`）：按角色（管理者/开发者/创作者/学生/财务等）差异化校准布局×风格×模块组合，避免千篇一律。
- `examples/style-gallery.html`：13 档风格画廊页（12 风格 + dark 态预览）。

### 发布记录
- Git：`2d52fd1`。

---

## [1.2.4] — 2026-08-15

### 修复
- 吸收端到端模拟验收（sim-review）反馈的细节问题。

### 发布记录
- Git：`86dce99`。

---

## [1.2.3] — 2026-08-15

### 修复
- 全量 review 修复：文档与种子不一致项、edge case 文案、参数校验。

### 发布记录
- Git：`23ee411`。

---

## [1.2.1] — 2026-08-15

### 变更
- 5 套 UI 预置模板（default/ocean/ink/macaron/sunset）同步至 reference 升级版：资料库直连双向同步 + 资源中心 + 密度打磨 + 工具栏落底。
- textured-startpage 模板工具栏移底。

### 发布记录
- Git：`77fae18`。

---

## [1.2.0] — 2026-08-15

> 存储层重构：去 localStorage 数据源，直连资料库 database。

### 新增
- **直连资料库 database 自动双向同步**：工作台内编辑实时写回 CSV 节点；本地降级（离线时缓存，恢复后补写）。
- `assets/deploy/deploy_to_library.py` 支持自动回填 `databases` 映射。

### 发布记录
- Git：`c6c569d`（主体）、`b2f76be`（修复待办勾选等编辑未同步——字段按类型用正确信封 text/checkbox/number/date/select/url，深拷贝 `_cache` 与展示数据解耦）。

---

## [1.1.0] — 2026-08-14

### 新增
- **resources 资源中心**模块：24 个公开 API/数据集/素材入口；修复 refresh 目标（SLOTS map）；工具栏移至右下角并补内容让位 padding。

### 变更
- 模块 14→15；SKILL.md frontmatter 对齐 SkillHub 发布规范（`911dae0`、`7e88a36`、`a6f5ce7`）。

### 发布记录
- Git：`f6502a0`（resources）、`a6f5ce7`（版本同步）。

---

## [1.0.0] — 2026-08-14

> 首个正式版：SkillHub 上线。

### 核心能力
- 零依赖单文件 HTML 工作台：CSS/JS/SVG/data URI 全内联，断网双击可开。
- 14 模块注册表（`register()` 模式：schema/seed/render）、4 布局、5 风格，`WORKBENCH_CONFIG` 一处装配。
- 数据落资料库 CSV(database) 节点 + 在线 page 托管（默认「我的文档」）。
- 风格×布局模板矩阵（`ffd6c28`：default+sidebar、sunset+cardGrid 等组合）。

### 发布记录
- Git：初始系列提交（`480c682`…`7e88a36`）。
- SkillHub：首次发布，skillId 156574，slug `workbuddy-workbench-builder`。

---

## 实战交付页（线上示例）

| 交付物 | 地址 | 说明 |
| --- | --- | --- |
| 老板工作台 | https://www.workbuddy.cn/space/d/Rpg1OaekWXBnovNmvk4nLi | 个人面板实战交付页 |

---

## 未发布（Unreleased）

- 本文件（CHANGELOG.md）随上线文档更新创建，README 已链接。

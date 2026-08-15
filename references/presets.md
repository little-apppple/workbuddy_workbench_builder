# 角色配方预设（Recipes）

> 解决"每次搭出来都一个样"的问题：不同角色一句话进来，直接命中差异化的
> **布局 × 风格 × 模块组合**，而不是永远 `default + sidebar + 六模块`。
>
> 用法：需求澄清时先对照本表选配方（或让用户挑），把配方整段粘进种子顶部的
> `WORKBENCH_CONFIG` 即可。用户有明确偏好时以用户为准，本表是缺省兜底。

## 组合空间

13 套风格 × 4 种布局 × 19 模块。常用配方如下（均为实测组合，风格与布局刻意错开）：

## 1. 老板指挥台（管人管事管节奏）

```javascript
{ title: "老板工作台", ui: "sidebar", theme: "auto", style: "wb", accent: "#185fa5",
  modules: ["todo","kanban","dashboard","calendar","mem"] }
```

看板推进项目 + 仪表盘看经营 + 日程管节奏。`wb` 官方风格稳重克制，汇报场景不怯场。

## 2. 开发者工作台（写码的一天）

```javascript
{ title: "Dev Deck", ui: "sidebar", theme: "auto", style: "tokyonight", accent: "#7aa2f7",
  modules: ["todo","mem","links","resources","dashboard"] }
```

速记踩坑、收藏文档、resources 自带 24 条开发常用 API/数据源。东京夜霓虹深蓝，深夜 debug 不刺眼。

## 3. 创作者灵感台（内容/设计/写作）

```javascript
{ title: "灵感工作台", ui: "masonry", theme: "auto", style: "rosepine", accent: "#d7827e",
  modules: ["mem","notes","kanban","reading","links"] }
```

瀑布流墙式铺开碎片灵感，看板管理选题管道（选题→草稿→发布），reading 追踪对标内容。玫瑰松温润雅致，适合写作型晚间工作。

## 4. 学生成长台（自律打卡）

```javascript
{ title: "学期面板", ui: "cardGrid", theme: "auto", style: "macaron", accent: "#b48ad4",
  modules: ["todo","habits","reading","calendar","journal"] }
```

习惯打卡 + 阅读清单 + 日记复盘，日历管考试DDL。马卡龙粉彩轻盈无压，cardGrid 一屏总览。

## 5. 数据团队台（指标与口径）

```javascript
{ title: "Data Ops", ui: "sidebar", theme: "auto", style: "nord", accent: "#5e81ac",
  modules: ["dashboard","ledger","todo","resources"] }
```

仪表盘先行（放第一个，打开即指标），ledger 记数据口径/变更流水，resources 存内部数据字典。北欧冷色，长时间盯数不疲劳。

## 6. 小生意经营台（夫妻店/个体户）

```javascript
{ title: "小店管家", ui: "topnav", theme: "auto", style: "sunset", accent: "#f0735f",
  modules: ["ledger","inventory","contacts","todo","dashboard"] }
```

流水账第一、库存第二、熟客联系人第三。topnav 手机上也好点，晚霞暖橙亲和、不拒人。

## 7. 极简专注台（越少越好）

```javascript
{ title: "Focus", ui: "cardGrid", theme: "light", style: "mono", accent: "#111111",
  modules: ["todo","mem","dashboard"] }
```

三模块到顶，黑白极简 4px 锐角，零装饰零干扰。适合"我就要个能用的清单"的用户。

## 8. 生活记录台（慢生活/疗愈系）

```javascript
{ title: "生活手账", ui: "masonry", theme: "auto", style: "everforest", accent: "#8da101",
  modules: ["journal","habits","calendar","mem","news"] }
```

日记为主，习惯打卡为辅，news 每日信息源当晨报。常青森林绿自然疗愈，瀑布流随手翻。

## 9. 夜猫子台（固定深色）

```javascript
{ title: "Night Owl", ui: "sidebar", theme: "dark", style: "catppuccin", accent: "#cba6f7",
  modules: ["todo","mem","notes","reading"] }
```

`theme: "dark"` 锁死深色（不跟随系统），奶咖低饱和深夜最护眼，长时使用无疲劳感。

## 10. 人脉经营台（销售/BD/猎头）

```javascript
{ title: "人脉雷达", ui: "sidebar", theme: "auto", style: "catppuccin", accent: "#8839ef",
  modules: ["contacts","calendar","todo","mem","notes"] }
```

联系人为主库（跟进记录写 notes），日历约访、todo 跟进提醒。浅色奶咖日常社交场合适用。

---

## 定制指引（配方之上再微调）

- **换主色**：`default` 风格吃 `accent` 自定义色；其余 11 套预置风格自带 accent，改了会被风格覆盖（想改主色就让用户换风格，而不是硬改 accent）。
- **加/减模块**：直接增删 `modules` 数组即可，页面与数据库结构自动适配（见 module-catalog.md）。
- **深色锁定**：`theme: "dark"`（同理 `"light"`），`"auto"` 跟随系统。
- **混搭**：布局和风格可以任意组合（如 mono + masonry = 极简灵感墙），本表组合只是经过审美校准的默认值。

## 11. 企业经营 · 缮语配方（v1.4 新增）

> 借鉴「缮语·企业 Claw」AI 企业经营管理工作台，面向高管/经营管理者。

```js
const WORKBENCH_CONFIG = {
  title: "企业经营工作台",
  ui: "sidebar",
  theme: "auto",
  style: "claw",            // 企业蓝：商务科技蓝白；dark 态即驾驶舱大屏风
  accent: "#1677ff",
  modules: ["briefing","insight","dashboard","approvals","cron","calendar"],
};
```

- **模块逻辑**：briefing 每日简报（先看什么）→ insight 外部洞察（外面发生了什么）→ dashboard 概览（经营数字）→ approvals 审批中心（拍板）→ cron 定时任务（自动化）→ calendar 日程
- **状态色编码**：claw 风格下 正常/通过=绿、关注/待审=橙、预警/驳回=红，全模块一致
- **自动化联动**：cron 模块登记任务，WorkBuddy automation 定时执行并回写 lastRun/status

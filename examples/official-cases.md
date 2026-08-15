# 官方案例库 · 使用资料库搭建个人和团队工作台

> 本文件取自资料库团队空间「🚀资料库的100种用法」下的官方指南
> **《💗使用资料库搭建个人和团队工作台》**（nodeId: `MFIIY4nQkybtYnVL0W7SIt`）。
> 用途：本 skill 生成工作台时，可直接从这里挑「官方案例风格」套用，
> 每个案例都给了**推荐模块组合**与**推荐 UI 模板**，省去从零设计。

---

## 一、两类场景怎么选（官方原文）

- **把资料变好看**：汇报、复盘、攻略、作品集。数据不常变，一个 HTML 页面就够。
- **把资料变能用**：个人工作台、客户跟进、任务看板、记账。过去得配数据库，
  现在 HTML 加一张 CSV 数据表就行。

## 二、上手试一下的官方 prompt（可直接抄给 WorkBuddy）

```
请使用资料库的能力帮我制作一个「xxx」的个人工作台，需要实现数据在线存储和双向同步。
工作台需包含以下功能：xxx
```

要点（官方强调）：
- **数据在线存储**：数据存在 CSV 表里，不写死在页面代码里。
- **双向同步**：页面上改会写回数据表，数据表里改页面也跟着变。
- 之后想加字段、换配色、加筛选，直接说一句就行。
- 适用：读书记录、健身打卡、家庭开支——凡是还在用备忘录或 Excel 凑合的事。

---

## 三、官方案例清单（含本 skill 的模块映射）

### 👤 个人用（自带数据库，多端同步）

| 官方案例 | 链接 | 核心内容 | 推荐模块组合 | 推荐 UI |
|---|---|---|---|---|
| 个人目标管理工作台 | [SOURMoVsi3mttCxw1UnJ3K](https://www.workbuddy.cn/space/d/SOURMoVsi3mttCxw1UnJ3K) | 有终点、有总量的学习目标 | `todo` + `dashboard` | `sidebar` |
| 生活全能工作台 | [EoQ66K7Fhi6o0osgDlxxvE](https://www.workbuddy.cn/space/d/EoQ66K7Fhi6o0osgDlxxvE) | 记账、习惯、健康、日程装进一个台 | `ledger` + `habits` + `calendar` + `dashboard` | `cardGrid` |
| 手帐 | [OlEl7TptNz9EcczECfhWZM](https://www.workbuddy.cn/space/d/OlEl7TptNz9EcczECfhWZM) | 工资、工时、支出、自由目标 | `ledger` + `todo` | `sidebar` |

### 👥 团队用（自带数据库，多端同步）

| 官方案例 | 链接 | 核心内容 | 推荐模块组合 | 推荐 UI |
|---|---|---|---|---|
| 商品订单经营 | [oiDYQMticarM1KyL2lgZRJ](https://www.workbuddy.cn/space/d/oiDYQMticarM1KyL2lgZRJ) | 商品、订单、经营数据 | `inventory` + `ledger` + `dashboard` | `topnav` |
| 客户销售跟进 | [HByeBbnlsP3m9gWDolNqlS](https://www.workbuddy.cn/space/d/HByeBbnlsP3m9gWDolNqlS) | 跟进客户和销售进展 | `contacts` + `kanban` | `sidebar` |
| 任务看板 | [ppZs8Jn2sTeDKhhMYO4TPR](https://www.workbuddy.cn/space/d/ppZs8Jn2sTeDKhhMYO4TPR) | 任务、负责人、项目状态 | `kanban` + `dashboard` | `topnav` |
| 线上小店 | [WPKKP2ulAmLeK0S5hxazAh](https://www.workbuddy.cn/space/d/WPKKP2ulAmLeK0S5hxazAh) | 品牌内容 + 商品管理 | `inventory` + `links` | `masonry` |

### 🎨 比文档更好看、更具交互感的表达（偏展示，数据不常变）

| 官方案例 | 链接 | 核心内容 | 推荐模块组合 | 推荐 UI |
|---|---|---|---|---|
| 旅行网站 | [svvdpxUx58AGYRsKyWaoL0](https://www.workbuddy.cn/space/d/svvdpxUx58AGYRsKyWaoL0) | 旅行资料整理成可浏览网站 | `notes` + `links` | `masonry` |
| 餐厅地图 | [MAv7EL6exdBlzdjAbLtX6e](https://www.workbuddy.cn/space/d/MAv7EL6exdBlzdjAbLtX6e) | 餐厅清单变成可探索地图 | `links` + 自定义地图模块 | `cardGrid` |

> 官方结语：**先从手头的一份资料，或一个一直想解决的小问题开始。**

---

## 四、怎么在本 skill 里用这些案例

1. 第 2 步「需求板块确认」：对照上表，把用户想要的工作台对应到 `references/module-catalog.md`
   里的模块组合（如"生活全能工作台" → `ledger + habits + calendar + dashboard`）。
2. 第 3 步「UI 规范确认」：对照上表"推荐 UI"列选模板；用户无偏好时直接采用推荐值。
3. 第 4 步「生成」：以 `examples/reference-workbench.html` 为种子，把上表的模块组合写进
   `WORKBENCH_CONFIG.modules`，选好 `ui` 模板即可。
4. 若用户要"每日自动更新"（如新闻/经营数据），见 SKILL.md 第 5 步「每日信息源自动更新」。

> 注：以上链接为资料库官方在线节点，点击即可查看真实运行效果；
> 本 skill 不复制其页面代码，仅提供"风格 → 模块 → UI 模板"的映射，供生成时参考。

> **补充（模块已全量实现）**：本 skill 的 `examples/reference-workbench.html` 已**内置全部 14 个模块**——上表用到的 `todo`/`mem`/`dashboard`/`notes`/`links`/`kanban`/`calendar`/`ledger`/`habits`/`reading`/`contacts`/`inventory`/`journal`，以及第 5 步每日自动更新所需的 `news`，均开箱即用。因此任意官方案例的「模块组合」都能直接写进 `WORKBENCH_CONFIG.modules` 由种子一键生成，无需从零写模块代码。

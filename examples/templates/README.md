# 模板示例索引（`examples/templates/`）

本目录收录可直接打开、可当新工作台起点的**零依赖单文件 HTML** 模板。
全部基于 `workbench-builder` 同一套设计 token 系统，保证全局样式一致性：
5 套预置风格（`default` / `macaron` / `ink` / `ocean` / `sunset`）+ 浅/深色模式一键切换。

> 打开方式：双击用浏览器打开即可（`file://` 离线可用，无 CDN、无外链）。
> 数据：运行时直连资料库 database 节点自动双向同步；`file://` 预览时降级到 localStorage（仅演示）。

---

## 模板清单

| 文件 | 来源 / 灵感 | 预设 + 布局 | 特点 | 适合场景 |
|---|---|---|---|---|
| `macaron-masonry.html` | workbench-builder 内置 | 马卡龙 + 瀑布流 | 粉彩卡片、错落流式排版 | 灵感墙 / 轻记录 |
| `ocean-sidebar.html` | workbench-builder 内置 | 深海 + 侧边栏 | 左侧导航 + 主区数据 | 效率 / 数据向 |
| `ink-topnav.html` | workbench-builder 内置 | 墨韵 + 顶部导航 | 极简顶栏、留白阅读 | 极简文档 / 阅读 |
| `default-sidebar.html` | workbench-builder 内置 | 默认 + 侧边栏 | 中性蓝灰、出厂基线、全功能导航 | 通用 / 个人总台 |
| `sunset-cardgrid.html` | workbench-builder 内置 | 晚霞 + 卡片网格 | 暖橙活力、卡片化模块平铺 | 创作 / 灵感聚合 |
| `launchpad.html` | 灵感来自 [NavHub](https://github.com/1718638143/NavHub) (MIT) | 玻璃侧边栏 | 分类 Tab + 聚合搜索 + 书签网格 | 链接 / 导航型工作台 |
| `glass-dashboard.html` | 灵感来自 [ZASENJC/dashboard](https://github.com/ZASENJC/dashboard) (MIT) | 玻璃拟态 Hero | 实时时钟 / 运行时间 / 加载耗时 + 书签统计 | 个人仪表盘首页 |
| `textured-startpage.html` | 灵感来自 [snownico0722/index-main](https://github.com/snowico0722/index-main) | 中央搜索 + 质感 | 站点分组 + 8 种质感切换 | 质感可换起始页 |

> 现已覆盖**全部 5 套风格**（default / macaron / ink / ocean / sunset）× **4 种布局**（sidebar / cardGrid / topnav / masonry）的代表性组合。
> 所有外部灵感模板均已**重写为零依赖单文件**，统一使用本 skill 的 token 系统，
> 禁止外链图标字体 / CDN。对应设计模式与署名见 `references/ui-design-system.md`。

---

## 风格配色速览（开文件前先挑）

浅色模式下的代表 token；深色模式由 `[data-theme="dark"]` 自动派生，不另列。

| 风格 | 名称 | 主色 accent | 背景 bg | 表面 surface | 气质 |
|---|---|---|---|---|---|
| `default` | 云灰蓝 | `#3b6cff` | `#f5f6f8` | `#fff` | 中性专业、克制 |
| `macaron` | 马卡龙 | `#b48ad4` | `#fbf7fc` | `#fff` | 粉彩柔润、轻盈治愈 |
| `ink` | 墨韵 | `#33334d` | `#fafafa` | `#fff` | 极简黑白、锋利高级 |
| `ocean` | 深海 | `#0f8b8f` | `#f1f8f9` | `#fff` | 青蓝静谧、清爽专注 |
| `sunset` | 晚霞 | `#f0735f` | `#fff6f2` | `#fff` | 暖橙活力、亲和明快 |

> 色块示例（主色 / 背景 / 表面）：
> <span style="display:inline-block;width:14px;height:14px;background:#3b6cff;border-radius:3px;vertical-align:middle"></span>
> <span style="display:inline-block;width:14px;height:14px;background:#b48ad4;border-radius:3px;vertical-align:middle"></span>
> <span style="display:inline-block;width:14px;height:14px;background:#33334d;border-radius:3px;vertical-align:middle"></span>
> <span style="display:inline-block;width:14px;height:14px;background:#0f8b8f;border-radius:3px;vertical-align:middle"></span>
> <span style="display:inline-block;width:14px;height:14px;background:#f0735f;border-radius:3px;vertical-align:middle"></span>

---

## 全局风格切换（所有模板通用）

每个模板内置「🎨 风格」按钮（或设置入口），切换会**全局生效**：

- 5 套预置风格：`default` / `macaron` / `ink` / `ocean` / `sunset`
- 浅色 / 深色：`[data-theme="light" | "dark"]`
- 质感（仅 `textured-startpage.html`）：`[data-material]` 仅改表面表现，颜色仍由 token 控制
- 选择持久化到 `localStorage`，刷新不丢失

如需在自建页面启用同一套风格系统，复制模板顶部 `<style>` 中的
`STYLES` 注册表 + `applyStyle()` / `toggleTheme()` 即可，无需改动业务结构。

---

## 作为新工作台起点

1. 挑一个最贴近目标的模板，复制为你的工作台文件。
2. 改 `<html data-style="..." data-theme="...">` 选默认风格。
3. 按 `references/module-catalog.md` 的 15 个模块裁剪 `MODULE_REGISTRY`。
4. 接 `references/` 的验收 checklist + test-cases 跑一遍六维验收。
5. 跑 `assets/deploy/deploy_to_library.py` 一键建库灌数并上传 HTML 到资料库「我的文档」。

> 完整权威种子（含全部 15 模块 + 图表 + 验收钩子）见上级目录
> `examples/reference-workbench.html`，模板多为单一布局/场景的精简起点。

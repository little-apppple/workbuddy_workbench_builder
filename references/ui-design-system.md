# UI 设计系统（UI Template System）

工作台 UI 由**模板驱动**，全部用 CSS 变量（设计 token）实现深/浅色与主题统一，零外部依赖。
4 套布局已实现于 `examples/reference-workbench.html` 的 `UI_LAYOUTS`，并各有骨架参考 `assets/ui/<模板>.html`。

> 选择方式：用户只需说"用侧边栏风/卡片风/顶部标签风/瀑布流"，agent 改 `WORKBENCH_CONFIG.ui` 即可，无需重画。

---

## 设计 Token（所有模板共用）

```css
:root{
  --bg: #f5f6f8;          /* 页面背景 */
  --surface: #ffffff;     /* 卡片/面板 */
  --surface-2: #eef0f4;   /* 次级面板 */
  --text: #1f2430;        /* 主文字 */
  --text-dim: #6b7280;    /* 次文字 */
  --border: #e3e6ec;      /* 描边 */
  --accent: #3b6cff;      /* 主题色(可换) */
  --accent-weak: #e8efff; /* 主题色弱底 */
  --danger: #e5484d;      /* 危险操作 */
  --ok: #2fa66a;          /* 成功 */
  --radius: 14px;         /* 圆角 */
  --shadow: 0 4px 18px rgba(20,30,60,.08);
  --gap: 16px;
}
[data-theme="dark"]{
  --bg:#0f1218; --surface:#171b23; --surface-2:#1f2530; --text:#e7ebf2;
  --text-dim:#94a0b3; --border:#2a313d; --accent-weak:#1c2740;
  --shadow:0 4px 18px rgba(0,0,0,.4);
}
```

- 主题：`light` / `dark` / `auto`（跟随 `prefers-color-scheme`）。
- 配色：可换 `--accent`（蓝/绿/橙/紫），由 `WORKBENCH_CONFIG.accent` 控制。
- 响应式：所有布局在窄屏（<720px）自动堆叠为单列。

---

## 模板 1 · sidebar（侧边栏导航）— 默认推荐

- **结构**：左侧固定导航列（模块图标+名），右侧内容区渲染当前选中模块。
- **适合**：模块 ≥3、需要常驻切换、控制台风。
- **特点**：模块多也不挤；当前模块全屏编辑体验好。
- **骨架**：`assets/ui/sidebar.html`

## 模板 2 · cardGrid（卡片网格马赛克）

- **结构**：所有模块以卡片铺在网格里，一屏看全局；卡片可滚动。
- **适合**：模块 ≤5、重概览、dashboard 优先。
- **特点**：信息密度高、首屏即"全景"；单模块空间受限。
- **骨架**：`assets/ui/card-grid.html`

## 模板 3 · topnav（顶部导航 + 标签页）

- **结构**：顶部一条导航，点击切到对应模块标签页（类浏览器 tab）。
- **适合**：简洁风、模块少、偏好传统后台布局。
- **特点**：横向空间利用好；移动端导航可折叠。
- **骨架**：`assets/ui/topnav-tabs.html`

## 模板 4 · masonry（瀑布流）

- **结构**：Pinterest 式错落卡片流，模块按内容高度自然排布。
- **适合**：展示/灵感墙、notes/links/mem 为主。
- **特点**：视觉松弛、不规则美；不适合强表格类模块。
- **骨架**：`assets/ui/masonry.html`

---

## 选择速查

| 用户说 | 选 |
|---|---|
| "控制台风 / 像后台 / 模块多" | `sidebar` |
| "一屏看全 / 概览 / 仪表盘优先" | `cardGrid` |
| "简洁 / 标签页 / 传统" | `topnav` |
| "灵感墙 / 展示 / 松弛" | `masonry` |
| 无偏好 | `sidebar` |

---

## 组件规范（所有模板共用）

- 卡片：`background:var(--surface); border:1px solid var(--border); border-radius:var(--radius); box-shadow:var(--shadow); padding:16px;`
- 按钮：主按钮 `background:var(--accent);color:#fff`；次按钮 `background:var(--surface-2);color:var(--text)`。
- 输入：`background:var(--surface-2);border:1px solid var(--border);border-radius:10px;padding:8px 10px;`
- 图标：优先 emoji 或内联 SVG（**禁止外链图标字体/CDN**）。
- 图表：仅用原生 Canvas2D（禁止 Chart.js 等 CDN 库）。

# 工作台使用示例

下面以**侧边栏模板（sidebar）**为例，演示工作台的默认界面与核心交互。

> 静态预览

![我的工作台 - 侧边栏模板](preview.png)

> 动态演示：4 套 UI 模板 + 深色主题切换

![工作台动态演示](demo.gif)

## 一分钟上手

1. **直接打开种子文件**
   用浏览器双击打开 `examples/reference-workbench.html`：

   ```bash
   # macOS / Linux
   open examples/reference-workbench.html

   # Windows
   start examples/reference-workbench.html
   ```

   该文件是**零依赖、单文件、可离线**的 HTML，不依赖任何 CDN 或后端。

2. **切换模块 / 模板 / 主题**
   编辑文件顶部的 `WORKBENCH_CONFIG`：

   ```js
   const WORKBENCH_CONFIG = {
     title: "我的工作台",
     ui: "sidebar",      // 可换：cardGrid / topnav / masonry
     theme: "auto",      // 可换：light / dark / auto
     accent: "#3b6cff",
     modules: ["todo", "mem", "dashboard", "notes", "links"]
   };
   ```

   - `modules`：从 `references/module-catalog.md` 的 14 个模块中按需勾选。
   - `ui`：4 套布局任意切换。
   - `theme`：`light`、`dark` 或跟随系统的 `auto`。

3. **运行时操作**
   - 在任意模块里**新增 / 删除 / 编辑**记录，数据自动保存在浏览器 `localStorage`。
   - 点击右上角「**主题**」可在深/浅色之间切换。
   - 点击「**导出 CSV**」会按模块生成对应的 CSV 文件（列名 = 模块 `schema`），这些 CSV 可直接导入 WorkBuddy 资料库。
   - 点击「**重置**」会把当前模块恢复为示例数据。

4. **把数据落到资料库（交付终态）**
   推荐使用编排脚本：

   ```bash
   cd workbench-builder
   # 在 WorkBuddy client 模式下，先通过 connect_open_platform 拿到 token
   # 然后注入 WB_TOKEN 并运行：
   WB_TOKEN="<your-token>" python assets/deploy/deploy_to_library.py
   ```

   该脚本会：
   - 读取 `assets/deploy/manifest.json` 中各模块的 schema 与 seed；
   - 在资料库「我的文档」创建对应的 CSV(database) 节点；
   - 把单文件 HTML 上传为资料库「我的文档」的在线 page 节点；
   - 返回 page 链接与每个 database_id。

   详细流程见 [`SKILL.md`](../SKILL.md) 第 4 步。

## 界面说明

- **左侧导航**（sidebar）：列出所有已启用模块，点击切换主面板。
- **工具栏**（右上角）：导出 CSV / 导入 CSV / 切换主题 / 重置。
- **模块卡片**（cardGrid / masonry）：同时展示多个模块，适合概览与展示墙。
- **顶部标签**（topnav）：简洁的横向标签页，适合模块较少的场景。

## 从示例到真实工作台

1. 把默认的 `modules` 换成你需要的组合；
2. 把示例 `seed` 替换成你的真实 CSV 数据（见 `references/module-catalog.md` 的字段映射）；
3. 选好 `ui` 和 `theme`；
4. 运行 `deploy_to_library.py`，拿到资料库链接，即为最终交付物。

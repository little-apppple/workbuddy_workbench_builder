# 质量门（Quality Checklist）

生成工作台后，**逐项核对**，全部通过才算完成。分 P0（硬约束）/ P1（功能）/ P2（体验）。

> 交付前的**逐条自动化验收用例**（UI 交互 / 样式 / 布局 / 数据结构 / 设计一致性 / 自动化任务）见
> [`test-cases.md`](./test-cases.md)，本文件是"构建 Check List"硬约束版，二者配合完成 SKILL.md 的「自动化验收环节」。

## P0 · 交付硬约束（一票否决）

- [ ] **单文件**：交付物是 1 个 `.html`，无相邻 css/js 依赖文件。
- [ ] **零外链**：全文 grep 无任何 `http(s)://` 指向第三方运行时（脚本/样式/字体/图表库/CDN）。图标用 emoji 或内联 SVG，图片用 data URI。
  - 自检：`grep -Eoi 'https?://[^"'\'' )]+' workbench.html | grep -Eiv 'workbuddy|codebuddy'` 应无输出（允许资料库内链；本工作台通常用不到）。
- [ ] **可离线**：`file://` 双击即可完整运行，无需服务器、无需联网。
- [ ] **资源内联**：CSS 在 `<style>`、JS 在 `<script>`、SVG 内联；无 `<link rel=stylesheet>`、无 `<script src>`。
- [ ] **强制 CSV 落库**：每个选中模块都在资料库建成 CSV 节点（`database_id` 已回执），HTML 的"导出 CSV"列与资料库 schema 对齐。
- [ ] **设计 token 唯一来源**：所有颜色来自 `:root` / `[data-theme]` CSS 变量，无散落硬编码色值（对应 `test-cases.md` TC-ST-01）。
- [ ] **数据结构完整**：每个模块导出 CSV 列名与 `references/module-catalog.md` 该模块 schema 完全一致；seed 可成功 `import_csv`/落库；空数据与超长字段不崩（对应 TC-DT-*）。
- [ ] **自动化任务合规**（仅当第 5 步配置）：rrule/范围/`cwds`/`status` 正确，prompt 自包含且仅追加不删改、不含写死凭证（对应 TC-AU-*）。

## P1 · 功能完整

- [ ] 模块按 `WORKBENCH_CONFIG.modules` 渲染，缺一个都不行。
- [ ] 每个模块可**增 / 改 / 删**，改动即时写入 localStorage。
- [ ] 工具栏含：**导出 CSV（全部/单模块）**、**导入 CSV**、**主题切换**、**重置**。
- [ ] CSV 导入导出**往返一致**（导出再导入数据不丢、不串列）。
- [ ] UI 模板按 `WORKBENCH_CONFIG.ui` 正确切换（sidebar/cardGrid/topnav/masonry）。
- [ ] 深/浅色与 `theme` 配置一致，且 `auto` 跟随系统。
- [ ] **布局不破版**：4 套模板在 ≥1280px 与 ≤480px 两种视口下均不破版、无重叠/溢出（对应 `test-cases.md` TC-LO-*）。
- [ ] **设计一致性**：全局字体/字号阶梯/间距/圆角/配色统一，模块卡片风格一致，无混用两套视觉语言（对应 TC-DS-*）。

## P2 · 体验

- [ ] 窄屏（<720px）自动单列，不溢出。
- [ ] 空数据有占位提示，不报错。
- [ ] 操作有轻反馈（toast/动画），删除有二次确认（尤其清空/重置）。
- [ ] 标题、模块名清晰，无乱码（UTF-8）。
- [ ] 若上传为资料库在线 page：过图片内链自检（本工作台无外链图，天然通过）。

## 落库回执模板

成功示例：
`工作台已生成：单文件 HTML（<路径>）+ 资料库 CSV 节点 ×N（database_id 列表）。访问：<page 链接或本地路径>。备份（若开启）：<自动化任务说明>。`

失败示例：按具体阻塞点说明，不回显 token/路径细节。

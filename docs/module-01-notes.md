\# Module 01：GitHub 基础与第一个外贸自动化仓库



\## 1. 本模块目标



Module 01 的目标是完成我的第一个 GitHub 外贸自动化项目。



本模块我完成了：



\* 理解 GitHub 是什么；

\* 创建第一个 GitHub 仓库；

\* 理解仓库（repository）、提交（commit）、分支（branch）、README 等基础概念；

\* 创建适合外贸自动化学习的项目结构；

\* 编写第一个 README 文件；

\* 创建 `.gitignore` 文件；

\* 创建第一个 Python 脚本文件；

\* 创建第一个 Codex 任务说明文件；

\* 查看 GitHub 的提交记录。



这是我从“完全不熟悉 GitHub”到“拥有第一个可扩展项目仓库”的第一步。



\---



\## 2. GitHub 是什么



GitHub 可以理解成：



```text

在线项目仓库 + 版本记录系统 + 未来给 Codex 使用的项目空间

```



外贸业务类比：



如果我要做 Made-in-China 产品运营，可能会有很多文件：



```text

产品数据表

关键词表

FAQ 问题表

Python 自动化脚本

产品标题生成结果

Codex 任务说明

```



如果这些文件散落在电脑桌面、微信、U盘、不同文件夹里，时间久了会很乱。



GitHub 的作用就是把它们集中放进一个清楚的项目仓库里，并且记录每一次修改。



\---



\## 3. 重要概念



\### 仓库（repository）



仓库就是一个项目空间。



我创建的第一个仓库是：



```text

foreign-trade-automation

```



它是我学习 Python、GitHub、Codex 和 B2B 外贸自动化的主项目。



\---



\### 提交（commit）



提交就是保存一次版本记录。



可以理解成：



```text

给项目拍一张版本照片，并写一句说明

```



例如：



```text

Create data folder

Create scripts folder

Update main README

Add gitignore file

Add first Python automation script

```



每一次 commit 都会记录：



\* 谁提交的；

\* 什么时候提交的；

\* 改了什么；

\* 这次修改的说明是什么。



\---



\### 分支（branch）



分支可以理解成项目的不同版本线。



我现在主要使用的是：



```text

main branch

```



也就是主分支。



目前我是个人学习项目，所以直接提交到 `main` 就可以。



以后如果做复杂修改、测试新功能，或者多人协作，才需要使用新的 branch 和 pull request。



\---



\### 拉取请求（pull request）



Pull request 可以理解成：



```text

我在一个分支里改完内容，然后申请把这些内容合并到主分支

```



外贸类比：



公司有一份正式产品目录，这是 `main`。



我想尝试优化标题，但不想直接影响正式目录，于是复制一份测试版来改。改完后提交给负责人审核，审核通过再合并回正式版本。



这个过程就类似 pull request。



Module 01 暂时不需要深入 pull request。



\---



\### README.md



`README.md` 是项目首页说明文件。



它的作用是告诉自己、别人、未来的 Codex：



\* 这个项目是做什么的；

\* 文件夹分别放什么；

\* 当前有什么脚本；

\* 怎么运行项目；

\* 未来要做哪些自动化任务。



README 可以理解成：



```text

项目说明书 + 项目首页 + 给 Codex 的项目背景介绍

```



\---



\### .gitignore



`.gitignore` 是告诉 Git：



```text

哪些文件不要上传，不要记录

```



例如：



```text

客户数据

真实报价表

密码

API key

Python 缓存文件

临时 Excel 文件

```



我创建 `.gitignore` 的目的是防止敏感文件或无用文件进入 GitHub 仓库。



\---



\## 4. Module 01 创建的项目结构



Module 01 结束后，我的项目结构大概是：



```text

foreign-trade-automation

├── .gitignore

├── README.md

├── data/

│   └── data-notes.md

├── scripts/

│   ├── script-notes.md

│   └── hello\_automation.py

├── outputs/

│   └── output-notes.md

└── prompts/

&#x20;   ├── prompt-notes.md

&#x20;   └── first-codex-task.md

```



后来我把文件夹名称统一成：



```text

outputs/

prompts/

```



这是更适合长期项目的命名方式，因为里面会存放多个输出文件和多个提示词文件。



\---



\## 5. 每个文件夹的作用



\### `data/`



用来存放原始业务数据。



例如：



\* 产品数据；

\* 关键词列表；

\* FAQ 问题；

\* Made-in-China 产品信息；

\* SEO 数据。



可以理解成：



```text

原始资料柜

```



\---



\### `scripts/`



用来存放 Python 自动化脚本。



例如：



\* 产品数据清洗脚本；

\* 标题生成脚本；

\* 关键词整理脚本；

\* FAQ 生成脚本；

\* SEO 数据处理脚本。



可以理解成：



```text

自动化工具箱

```



\---



\### `outputs/`



用来存放 Python 脚本生成的结果。



例如：



\* 清洗后的产品表；

\* 生成后的产品标题；

\* FAQ 输出结果；

\* SEO 关键词分析结果。



可以理解成：



```text

自动化结果文件夹

```



\---



\### `prompts/`



用来存放给 Codex、ChatGPT 或自动化任务使用的提示词。



例如：



\* 产品数据清洗 prompt；

\* Made-in-China 标题生成 prompt；

\* FAQ 生成 prompt；

\* SEO 关键词分析 prompt；

\* Codex 编程任务说明。



可以理解成：



```text

任务说明书文件夹

```



\---



\### `docs/`



用来存放学习笔记和命令小抄。



例如：



```text

docs/git-command-cheatsheet.md

docs/module-01-notes.md

docs/module-02-notes.md

```



可以理解成：



```text

学习资料和复盘文件夹

```



\---



\## 6. Module 01 创建的重要文件



\### `README.md`



这是项目的主说明文件。



它记录了：



\* 项目目标；

\* 文件夹结构；

\* 未来自动化方向；

\* 学习说明。



\---



\### `.gitignore`



这是忽略规则文件。



它告诉 Git 不要记录：



```text

\_\_pycache\_\_/

\*.pyc

venv/

.env

\~$\*.xlsx

\~$\*.xls

customer\_data/

private\_data/

\*.key

\*.pem

```



这些内容包括 Python 缓存、虚拟环境、环境变量、Excel 临时文件和敏感业务数据。



\---



\### `scripts/hello\_automation.py`



这是我创建的第一个 Python 文件。



它的作用是确认：



```text

这个仓库可以存放 Python 自动化脚本

```



它是后续真正自动化脚本的起点。



\---



\### `prompts/first-codex-task.md`



这是我创建的第一个 Codex 任务说明文件。



它的作用是练习如何给 Codex 写清楚任务：



\* 任务目标；

\* 项目背景；

\* 输入文件；

\* 输出要求；

\* 代码要求；

\* 检查标准。



这让我明白，未来不能只对 Codex 说“帮我写代码”，而是要把任务拆清楚。



\---



\## 7. Module 01 学到的 GitHub 网页操作



本模块主要在 GitHub 网页端完成操作。



我学会了：



\* 创建 repository；

\* 创建新文件；

\* 用路径创建文件夹；

\* 编辑 README；

\* 创建 `.gitignore`；

\* 写 commit message；

\* 直接提交到 main branch；

\* 查看 commit history。



\---



\## 8. GitHub 创建文件夹的规则



GitHub 不能直接创建空文件夹。



如果我要创建一个文件夹，必须在里面创建一个文件。



例如：



```text

data/data-notes.md

```



意思是：



```text

创建 data 文件夹，并在里面创建 data-notes.md 文件

```



这里的 `/` 表示路径。



\---



\## 9. 文件路径的理解



在 GitHub 和本地项目中，文件名不只是名字，还包括它所在的位置。



例如：



```text

README.md

```



和：



```text

data/README.md

```



不是同一个文件。



因为第二个文件在 `data/` 文件夹里面。



\---



\## 10. Commit Message 的作用



每次提交时都要写 commit message。



它的作用是说明这次改了什么。



例如：



```text

Create data folder

Create scripts folder

Create outputs folder

Create prompts folder

Update main README

Add gitignore file

Add first Python automation script

Add first Codex task prompt

```



好的 commit message 应该简短、清楚，让以后回看项目历史时能知道每一步做了什么。



\---



\## 11. Direct Commit 和 Pull Request 的区别



在 GitHub 提交时，我看到过两个选项：



```text

Commit directly to the main branch

Create a new branch for this commit and start a pull request

```



Module 01 我选择：



```text

Commit directly to the main branch

```



原因是：



\* 这是个人学习项目；

\* 项目刚开始；

\* 不需要复杂协作流程；

\* 直接提交到 main 更简单。



Pull request 以后再学习。



\---



\## 12. 为什么这个项目结构适合 Codex



这个结构对 Codex 很友好：



```text

README.md   → 告诉 Codex 项目背景和目标

data/       → 放输入数据

scripts/    → 放 Python 脚本

outputs/    → 放输出结果

prompts/    → 放任务说明

docs/       → 放学习笔记和命令小抄

```



以后我可以对 Codex 说：



```text

请读取 data/ 里的产品表，

在 scripts/ 里写一个 Python 脚本，

把处理结果输出到 outputs/，

并更新 README 说明脚本怎么使用。

```



这就是 GitHub + Codex 配合的基本思路。



\---



\## 13. Module 01 的核心收获



Module 01 让我完成了从 0 到 1 的 GitHub 入门。



我现在知道：



\* GitHub 是在线项目仓库；

\* repository 是一个项目空间；

\* commit 是一次版本记录；

\* branch 是项目的不同版本线；

\* README 是项目说明书；

\* `.gitignore` 可以防止不该上传的文件进入仓库；

\* GitHub 网页端可以创建文件和提交修改；

\* 文件夹可以通过“路径/文件名”的方式创建；

\* 清楚的项目结构可以帮助以后使用 Codex。



\---



\## 14. Module 01 总结



Module 01 的最终成果是：



```text

我创建了第一个外贸自动化 GitHub 项目。

```



这个项目已经具备：



\* 基础 README；

\* 数据文件夹；

\* 脚本文件夹；

\* 输出文件夹；

\* 提示词文件夹；

\* Git 忽略规则；

\* 第一个 Python 文件；

\* 第一个 Codex 任务文件；

\* GitHub 提交记录。



这为 Module 02 的本地 Python 自动化工作流打下了基础。




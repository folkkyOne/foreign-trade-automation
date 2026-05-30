\# Module 02：本地 Python 自动化工作流



\## 1. 本周目标



第 2 周的目标是从“只在 GitHub 网页上操作”，进入到“在自己电脑本地操作项目”。



本周我学习了：



\* 如何把 GitHub 仓库克隆（clone）到本地电脑；

\* 如何用 PowerShell 进入项目文件夹；

\* 如何安装并检查 Python；

\* 如何在本地运行 Python 脚本；

\* 如何创建简单的产品数据 CSV 文件；

\* 如何用 Python 自动生成产品标题草稿；

\* 如何用 Git 记录本地修改；

\* 如何把本地 commit 推送（push）回 GitHub。



这是我完成的第一个 B2B 外贸自动化项目闭环。



\---



\## 2. 本周完成的项目流程



本周完成的基本流程是：



```text

GitHub 云端仓库

↓ git clone

本地项目文件夹

↓ 创建产品数据文件

Python 脚本

↓ 生成输出结果

输出 CSV 文件

↓ git add / git commit / git push

GitHub 云端仓库更新

```



在这个项目里，实际流程是：



```text

data/sample\_products.csv

↓

scripts/generate\_titles.py

↓

outputs/generated\_titles.csv

```



意思是：



\* `data/sample\_products.csv` 存放原始产品数据；

\* `scripts/generate\_titles.py` 读取产品数据，并生成产品标题草稿；

\* `outputs/generated\_titles.csv` 保存生成后的结果。



\---



\## 3. 项目文件夹作用



\### `data/`



这个文件夹用来存放原始业务数据。



例如：



\* 产品数据；

\* 关键词列表；

\* FAQ 问题；

\* Made-in-China 产品信息。



当前文件：



```text

data/sample\_products.csv

```



\---



\### `scripts/`



这个文件夹用来存放 Python 自动化脚本。



当前脚本：



```text

scripts/generate\_titles.py

```



这个脚本的作用是读取产品数据，并自动生成产品标题草稿。



\---



\### `outputs/`



这个文件夹用来存放 Python 脚本生成的结果。



当前输出文件：



```text

outputs/generated\_titles.csv

```



\---



\### `docs/`



这个文件夹用来存放学习笔记和命令小抄。



当前笔记包括：



```text

docs/git-command-cheatsheet.md

docs/week-02-notes.md

```



\---



\### `prompts/`



这个文件夹用来存放给 Codex、ChatGPT 和自动化任务使用的提示词。



\---



\## 4. 本周用到的 PowerShell 命令



\### 查看当前位置



```powershell

pwd

```



作用：查看我现在位于电脑的哪个文件夹。



\---



\### 查看当前文件夹内容



```powershell

ls

```



作用：列出当前文件夹里的文件和文件夹。



例如：



```powershell

ls data

```



作用：查看 `data` 文件夹里面有什么文件。



\---



\### 进入项目文件夹



```powershell

cd $HOME\\Documents\\GitHub\\foreign-trade-automation

```



作用：进入我本地的 GitHub 项目文件夹。



\---



\### 用记事本打开或创建文件



```powershell

notepad data/sample\_products.csv

```



作用：用 Windows 记事本打开或创建产品数据 CSV 文件。



例如：



```powershell

notepad scripts/generate\_titles.py

```



作用：用记事本打开或创建 Python 脚本文件。



\---



\## 5. 本周用到的 Python 命令



\### 检查 Python 版本



```powershell

python --version

```



作用：检查 Python 是否安装成功，并显示当前版本。



\---



\### 运行第一个测试脚本



```powershell

python scripts/hello\_automation.py

```



作用：运行项目里的第一个简单 Python 测试脚本。



\---



\### 运行标题生成脚本



```powershell

python scripts/generate\_titles.py

```



作用：读取 `data/sample\_products.csv` 里的产品数据，并生成标题草稿到 `outputs/generated\_titles.csv`。



\---



\### 查看生成结果



```powershell

Get-Content outputs/generated\_titles.csv

```



作用：直接在 PowerShell 里查看生成后的 CSV 文件内容。



\---



\## 6. 本周用到的 Git 命令



\### 克隆 GitHub 仓库



```powershell

git clone https://github.com/folkkyOne/foreign-trade-automation.git

```



作用：把 GitHub 上的仓库下载到本地电脑。



\---



\### 从 GitHub 拉取最新内容



```powershell

git pull

```



作用：把 GitHub 云端仓库的最新修改同步到本地电脑。



\---



\### 查看项目状态



```powershell

git status

```



作用：查看当前项目有没有新增、修改、删除、重命名或未提交的文件。



常见状态解释：



```text

Changes not staged for commit

```



意思：Git 已经发现文件变化，但这些变化还没有进入准备提交区。



```text

Changes to be committed

```



意思：这些变化已经进入准备提交区，可以 commit。



```text

nothing to commit, working tree clean

```



意思：没有未提交的修改，本地项目是干净的。



\---



\### 把修改加入准备提交区



```powershell

git add -A

```



作用：把所有新增、修改、删除、重命名的文件加入准备提交区。



我在重命名文件夹时用到了它：



```text

output → outputs

prompt → prompts

```



\---



\### 提交修改



```powershell

git commit -m "Rename folders and add title generator"

```



作用：保存一次本地版本记录，并写一句说明。



其中：



```text

\-m

```



是 message 的意思，用来写 commit 说明。



\---



\### 推送到 GitHub



```powershell

git push

```



作用：把本地 commit 上传到 GitHub 云端仓库。



\---



\## 7. 我对 Git 工作区的理解



Git 有几个重要区域：



```text

工作区 working directory

↓ git add

准备提交区 staging area

↓ git commit

本地版本库 local repository

↓ git push

GitHub 云端仓库 remote repository

```



简单理解：



\* 工作区：我实际编辑文件的地方；

\* 准备提交区：准备打包成 commit 的区域；

\* 本地版本库：commit 保存到我电脑本地后的版本记录；

\* GitHub 云端仓库：项目在线保存的位置。



\---



\## 8. 本周遇到的问题和解决方法



\### 问题 1：`git pull` 或 `git push` 失败



错误示例：



```text

Failed to connect to github.com port 443

```



意思：



Git 没有成功连接到 GitHub，通常是网络、VPN 或代理问题。



解决方法：



\* 重启 PowerShell；

\* 先打开 VPN 或代理，再打开 PowerShell；

\* 必要时给 Git 配置代理端口。



\---



\### 问题 2：Git 要求设置作者身份



错误示例：



```text

Author identity unknown

Please tell me who you are.

```



意思：



Git 不知道这次 commit 应该署名给谁。



解决方法：



```powershell

git config --global user.name "folkkyOne"

git config --global user.email "my-github-email@example.com"

```



\---



\### 问题 3：文件夹名字不统一



问题：



项目里原来有：



```text

output/

prompt/

```



但计划中的标准结构应该是：



```text

outputs/

prompts/

```



解决方法：



在本地重命名文件夹，然后提交到 GitHub。



```powershell

Rename-Item output outputs

Rename-Item prompt prompts

git add -A

git commit -m "Rename folders and add title generator"

git push

```



\---



\### 问题 4：Python 找不到输出文件夹



错误示例：



```text

FileNotFoundError: No such file or directory: 'outputs/generated\_titles.csv'

```



意思：



Python 脚本想把结果保存到 `outputs/` 文件夹里，但当时文件夹名字不匹配。



解决方法：



确认文件夹名字是：



```text

outputs/

```



而不是：



```text

output/

```



\---



\## 9. 我的第一个真实自动化结果



本周我创建了原始产品数据文件：



```text

data/sample\_products.csv

```



然后创建并运行了 Python 脚本：



```text

scripts/generate\_titles.py

```



脚本生成了结果文件：



```text

outputs/generated\_titles.csv

```



这说明我完成了第一个简单的外贸自动化流程：



```text

原始产品数据

↓

Python 处理

↓

生成产品标题草稿

```



\---



\## 10. 以后本地工作的标准流程



以后我在本地做这个项目时，可以按这个顺序操作：



```powershell

git pull

git status

python scripts/generate\_titles.py

git status

git add -A

git commit -m "describe my change"

git push

git status

```



意思是：



1\. `git pull`：先同步 GitHub 最新版本；

2\. `git status`：检查当前状态；

3\. 运行或修改 Python 脚本；

4\. 再次 `git status`：查看发生了什么变化；

5\. `git add -A`：把变化加入准备提交区；

6\. `git commit -m "..."`：保存本地版本记录；

7\. `git push`：上传到 GitHub；

8\. 最后 `git status`：确认工作区干净。



\---



\## 11. 第 2 周总结



第 2 周，我学会了如何把 GitHub、电脑本地文件、Python 脚本和 Git 工作流连接起来。



我现在不只是会在 GitHub 网页上创建文件，也可以：



\* 在本地操作 GitHub 项目；

\* 创建本地数据文件；

\* 运行 Python 自动化脚本；

\* 生成输出结果；

\* 用 Git 追踪项目变化；

\* 用 commit 保存版本；

\* 用 push 上传到 GitHub。



这是以后使用 Codex 辅助开发 Made-in-China 产品运营、关键词整理、FAQ 生成、SEO 内容准备等外贸自动化工具的基础。




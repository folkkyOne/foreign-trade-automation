# Git and PowerShell Command Cheatsheet

This file records the basic commands I need for learning Git, GitHub, Python, and Codex.

---

## 1. PowerShell Basic Commands

### `pwd`

```powershell
pwd
```

Comment: Show my current folder location.
中文：查看我现在在哪个文件夹里。

---

### `ls`

```powershell
ls
```

Comment: List files and folders in the current location.
中文：查看当前文件夹里面有什么。

---

### `cd`

```powershell
cd folder-name
```

Comment: Change directory. Enter a folder.
中文：进入某个文件夹。

Example:

```powershell
cd scripts
```

---

### `cd ..`

```powershell
cd ..
```

Comment: Go back to the parent folder.
中文：返回上一级文件夹。

---

### `$HOME`

```powershell
echo $HOME
```

Comment: Show my user home folder.
中文：查看我的用户主目录，通常类似 `C:\Users\YourName`。

Example:

```powershell
cd $HOME\Documents
```

Comment: Go to the Documents folder under my user home folder.
中文：进入我的 Documents 文件夹。

---

### `mkdir`

```powershell
mkdir folder-name
```

Comment: Create a new folder.
中文：创建一个新文件夹。

Example:

```powershell
mkdir docs
```

---

## 2. Python Commands

### Check Python version

```powershell
python --version
```

Comment: Check whether Python is installed and show the Python version.
中文：检查 Python 是否安装成功，并显示版本。

---

### Run a Python file

```powershell
python file-name.py
```

Comment: Run a Python script.
中文：运行一个 Python 脚本文件。

Example:

```powershell
python scripts/hello_automation.py
```

---

## 3. Git Basic Commands

### Check Git version

```powershell
git --version
```

Comment: Check whether Git is installed and show the Git version.
中文：检查 Git 是否安装成功，并显示版本。

---

### Clone a GitHub repository

```powershell
git clone repository-url
```

Comment: Download a GitHub repository to my computer.
中文：把 GitHub 上的仓库下载到我的电脑。

Example:

```powershell
git clone https://github.com/your-username/foreign-trade-automation.git
```

---

### Check Git status

```powershell
git status
```

Comment: Check which files have been changed, added, or not committed.
中文：查看哪些文件被修改了、哪些文件还没有提交。

---

### Pull latest changes

```powershell
git pull
```

Comment: Download the latest changes from GitHub to my local computer.
中文：把 GitHub 云端仓库的最新内容同步到本地电脑。

---

### Add changes

```powershell
git add .
```

Comment: Add all changed files to the staging area before commit.
中文：把所有修改加入“准备提交区”。

---

### Commit changes

```powershell
git commit -m "commit message"
```

Comment: Save a version record with a short message.
中文：保存一次版本记录，并写一句说明。

Example:

```powershell
git commit -m "Add Git command cheatsheet"
```

---

### Push changes

```powershell
git push
```

Comment: Upload local commits to GitHub.
中文：把本地提交上传到 GitHub 云端仓库。

---

## 4. Common Local Workflow

When I work on this project locally, I can follow this order:

```powershell
git pull
git status
git add .
git commit -m "describe my change"
git push
```

Comment:

1. `git pull` gets the latest version from GitHub.
2. `git status` checks what changed.
3. `git add .` prepares all changes for commit.
4. `git commit -m "message"` saves a version record.
5. `git push` uploads the local commit to GitHub.

中文：

1. `git pull`：先同步 GitHub 最新版本。
2. `git status`：检查我改了什么。
3. `git add .`：把修改加入准备提交区。
4. `git commit -m "message"`：保存一个版本记录。
5. `git push`：上传到 GitHub。

---

## 5. My Simple Memory Formula

When I get lost in PowerShell:

```powershell
pwd
ls
cd folder-name
ls
```

Comment:

* `pwd`: Where am I?
* `ls`: What is here?
* `cd`: Where do I want to go?
* `ls`: What is inside this folder?

中文记忆：

* `pwd`：我在哪？
* `ls`：这里有什么？
* `cd`：我要去哪里？
* `ls`：进去之后再看看有什么。

---

## 6. Important Notes

* Git is used for version control.
* GitHub is used to store the project online.
* Python is used to run automation scripts.
* Codex can help write and modify code based on the project structure.
* Do not upload customer data, private quotations, passwords, or API keys to a public GitHub repository.

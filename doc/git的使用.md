## Git
- 分布式版本控制系统。(https://www.cnblogs.com/uncleyong/p/10854115.html)
> 安装：直接去官网下载安装即可
### 命令详解
> 版本的查看：git --version  
> 初始化本地仓库:git init(先创建一个文件夹，进入文件夹执行)  
> 查看状态: git status  
> 文件添加到暂存区：git add 文件名/.  
> 在提交前必须进行配置:  
- git config --global user.name "xxx"
- git config --global user.email "XX@.com"
> 提交到本地仓库：git commit -am'提交说明'  
> 推送到远程: git push  

> 在远程仓库上新建项目
> 复制远程仓库的地址:  
> 添加远程仓库: git remote add 别名 复制的地址  
> git push 别名
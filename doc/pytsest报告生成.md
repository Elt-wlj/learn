## 安装pytest
- pip install pytest
## 安装allure
- 访问github进行下载：https://github.com/allure-framework/allure2/releases
- 注意：**版本和jdk的版本要一致**
## 运行alure报告
> 必须要生成reports文件之后才可以哟
- eg: pytest --alluredir ./reports .\1110pyte.py
- 在终端中执行: allure serve ./reports/ 
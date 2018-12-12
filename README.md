##  Sandy_2019
#### 2019项目

## 目录结构
   1. Core：公用方法
   2. Service：提供公用服务的代码层
   3. Config：全局配置文件，log文件，配置文件等
   4. Project：项目分区
   5. Shell: 全局脚本文件
    
## 代码规范：
   1. 文件夹、文件名、方法类名同意用驼峰规范，方法单词间用下划线连接
   2. 类方法或者文件夹避免与内置方法重名，在命名前加s
    
## 执行脚本记录
   1. pytest + allure 开始测试 && 生成测试报告
       ###### py.test test/ --alluredir ./result/  ---- pytest执行
       ###### allure generate ./result/ -o ./report/ --clean   ---- 生成html报告
   2. pytest + pytest-html 开始测试 && 生成测试报告
       ###### pytest DdtTest.py --html=./report/report.html -o log_cli=true -o log_cli_level=ERROR
       ###### ps: 执行文件夹， 测试文件必须以test_开头

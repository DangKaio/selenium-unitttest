####
使用了python+selenium+unittest
UI 自动化测试

 =====
 觉得有用的希望给个star，非常感谢
V1:登录、搜索功能已完成

V2:登录、搜索全局化、自动化测试框架的搭建

V3:发送报告功能已完成

V4:添加日志记录功能

V5:修改登录、搜索将初始登录提取出来

V6:对登录的异常情况、搜索进行添加

V7:增加截图，针对网页和弹窗分别截图。增加发送邮件模块

globalparam.py 修改



====
2018年11月
近期在编写自动化脚本的时候发现以前写的部分不是特别友好，而且好多垃圾代码，在此进行重构。废话不说

开始重构自动化框架，首先先理清思路：

使用的技术python+unittest+selenium+excel+ddt
这次多了excel和ddt
针对UI自动化测试，这次重新封装了selenium,利用ddt数据驱动，简化了自动化脚本的编写，希望对大家有用

##文件目录有：

	config:配置文件

	testcase:测试用例
		flow_case:流程测试用例存放目录
		function_case:功能测试用例存放目录
	common:公用方法　

	test_data：测试文件存放目录
		excel：测试用例
		file_download:测试过程中下载目录
		file_upload:测试过程中上传文件存放目录
		yaml:yaml文件的存放目录
	test_result:
		test_report:测试报告
		log:log文件存放目录
		img_screenshot:截图存放目录
	webdriver：驱动存放目录
##出现了一个list indices must be integers or slices,not str  错误，原来是数据传输过程中参数错误，已解决

#html有个小问题 等有时间改下就行了

##注意：
此处拉下来后，要在report建立一个log文件夹，不然找不到路径

selenium提供了三种模式的断言：assert,verify,waitfor
    Assert：失败时，该测试将终止
    Verify：失败时，该测试继续执行，并将错误日志记录在日显示屏
    Waitfor：等待某些条件变为真，一般使用在AJAX应用程序的测试


断言常用的有，具体见如下：
assertLocation：判断当前是在正确的页面
assertTitle：检查当前页面的title是否正确
assertValue：检查input的值，check or radio，有为on，无为off
assertSelected：检查select的下拉菜单中选中是否正确
assertSelectedOptions：检查下拉菜单中的A选项是否正确
asserttext：检查指定元素的文本
assertTextParset：检查在当前给用户显示的页面上是否具有出现指定的文本
asserttextNotPresent：检查在当前给用户显示的页面上是否没有出现指定的文本
assertAttribute：检查当前指定元素的属性的值
assertTable：检查table里的某个cell中的值
assertEditable：检查指定的input是否可以编辑
assertNotEditable：检查指定的input是否不可以编辑
assertAlert：检查是否有产生带指定message的alert对话框
verifyTitle：验证预期的页面标题
verifyTextPresent：验证预期的文本是否在页面上的某个位置
verifyElementPresent：验证预期的UI元素，它的html标签的定义，是否在当前网页上
verifyText：核实预期的文本和相应的HTML标签是否都存在于页面上
verifyTable：验证表的预期内容
waitForPageToLoad：暂停执行，直到预期的新的页面加载
waitForElementPresent：等待检验某元素的存在，为真时，则执行

##赞助一下

![image](https://github.com/DangKaio/python-selenium-unittest/tree/master/test_result/img_screenshot/20181110133035.png)


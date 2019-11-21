1.创建一个新项目：

scrapy startproject myproject
　

2.在新项目中创建一个新的spider文件：

scrapy genspider mydomain mydomain.com
mydomain为spider文件名，mydomain.com为爬取网站域名

 

3.全局命令：

startproject
genspider
settings
runspider
shell
fetch
view
version
 

4.只在项目中使用的命令（局部命令）：

crawl
check
list
edit
parse
bench
 

5.运行spider文件：

scrapy crawl <spider>
　　

6.检查spider文件有无语法错误：

scrapy check
 

7.列出spider路径下的spider文件：

scrapy list
 

8.编辑spider文件：

scrapy edit <spider>
相当于打开vim模式，实际并不好用，在IDE中编辑更为合适。

 

9.将网页内容下载下来，然后在终端打印当前返回的内容，相当于 request 和 urllib 方法：

scrapy fetch <url>
 

10.将网页内容保存下来，并在浏览器中打开当前网页内容，直观呈现要爬取网页的内容:　

scrapy view <url>
 

11.打开 scrapy 显示台，类似ipython，可以用来做测试：

scrapy shell [url]
 

12.输出格式化内容：

scrapy parse <url> [options]
 

13.返回系统设置信息：

scrapy settings [options]
如：

$ scrapy settings --get BOT_NAME
scrapybot
 

14.运行spider：

scrapy runspider <spider_file.py>
 

15.显示scrapy版本：

scrapy version [-v]
后面加 -v 可以显示scrapy依赖库的版本

 

16.测试电脑当前爬取速度性能：

scrapy bench
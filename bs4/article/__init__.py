# coding:utf8
import re

from bs4 import BeautifulSoup

html_doc = """
<html>
    <head>
    <title>bs4官方文档</title>
    </head>
    <body>
        <p class="title"><b>The Dormouse's story</b></p>
        
        <p class="story">Once upon a time there were three little sisters; and their names were</p>
        <p>
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        and they lived at the bottom of a well.
        </p>

        <p class="story"> 最后一个 p ;class="story"</p>
        <p class="storys"> p ;class="storys"</p>
"""

soup = BeautifulSoup(html_doc, "html.parser")
# -------------------------------------------------------------------------------------
# print soup.prettify()# 格式化输出 HTML文档
# print soup.title
# print soup.title.name
# print soup.title.string
# print soup.p

# -------------------------------------------------------------------------------------
# 查找 p 元素，且 该 p 元素满足 class属性的值为 story
# p_class.text 、p_class.string、p_class.get_text() 等价

# for p_class in soup.find_all('p', {'class': 'story'}):
#     print p_class.get_text()

# -------------------------------------------------------------------------------------

# for p_class in soup.find_all('p', {'class': re.compile('^s[A-Z].*s$')}):
#     print p_class.get_text()

# -------------------------------------------------------------------------------------
# 打印出第一个 a 标签

# print soup.a
# -------------------------------------------------------------------------------------
# 打印出所有的 a 标签
# i = 0
# for link in soup.find_all('a'):
#     i = i + 1
#     print '第 ', i, ' 个 a 标签的链接 = ', link[
#         'href'], '标签的内容 = ', link.string

# -------------------------------------------------------------------------------------
# i = 0
# for link in soup.find_all(name='a'):
#     i = i + 1
#     print  type(link), link['href'], link.string, link['id'], len(link)
# -------------------------------------------------------------------------------------
# 从文档中获取所有文本内容
print soup.get_text()
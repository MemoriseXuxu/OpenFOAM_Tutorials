# -*-coding:UTF-8-*-

''''
需要获取的信息如下：
<li>
    <h3 class="event-title"><a href="/events/python-events/1146/">PyCon US 2022</a>
    </h3>
        <p>                           
            <time datetime="2022-04-27T00:00:00+00:00">27 April – 05 May 
                <span class="say-no-more"> 2022
                </span>
            </time>                                     
            <span class="event-location">Salt Lake City, Utah, USA
            </span>                          
        </p>
</li>
'''

from html.parser import HTMLParser
from urllib.request import Request,urlopen
import re


def get_data(url):
   headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
      }
   req = Request(url, headers=headers)
   with urlopen(req, timeout=25) as f:
      data = f.read()
      print(f'Status: {f.status} {f.reason}')
      print()
   return data.decode("utf-8")

class MyHTMLParser(HTMLParser):
   def __init__(self):
      super().__init__()
      self.__parsedata='' # 设置一个空的标志位
      self.info = []

   def handle_starttag(self, tag, attrs):
      if ('class', 'event-title') in attrs:
         self.__parsedata = 'name'  # 通过属性判断如果该标签是我们要找的标签，设置标志位
      if tag == 'time':
         self.__parsedata = 'time'
      if ('class', 'say-no-more') in attrs:
         self.__parsedata = 'year'
      if ('class', 'event-location') in attrs:
         self.__parsedata = 'location'

   def handle_endtag(self, tag):
      self.__parsedata = ''# 在HTML 标签结束时，把标志位清空

   def handle_data(self, data):

      if self.__parsedata == 'name':
         # 通过标志位判断，输出打印标签内容
         self.info.append(f'会议名称:{data}')

      if self.__parsedata == 'time':
         self.info.append(f'会议时间:{data}')

      if self.__parsedata == 'year':
         if re.match(r'\s\d{4}', data): # 因为后面还有两组 say-no-more 后面的data却不是年份信息,所以用正则检测一下
            self.info.append(f'会议年份:{data.strip()}')

      if self.__parsedata == 'location':
         self.info.append(f'会议地点:{data} \n')

def main():
   parser = MyHTMLParser()
   URL = "https://www.python.org/events/python-events/"
   data = get_data(URL)
   parser.feed(data)
   for s in parser.info:
      print(s)

if __name__ == '__main__':
   main()
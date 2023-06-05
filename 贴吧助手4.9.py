# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 04:22:02 2023

@author: 11195
"""

# === 本代码用于根据用户名检索该用户曾经回复过的帖子 ===#

import requests

from bs4 import BeautifulSoup

# 读取配置
import configparser
# 配置文件大小写转换
class myconf(configparser.ConfigParser):
    def __init__(self,defaults=None):
        configparser.ConfigParser.__init__(self,defaults=None)
    def optionxform(self, optionstr):
        return optionstr

config= myconf()

CONFIG = 'config.ini'

config.read(CONFIG, encoding="utf-8-sig")

#配置信息
tieba_name = config.get('tieba', 'NAME')    # 贴吧名
pages = int(config.get('tieba', 'PAGES'))   # 一共检索几页
target_id = config.get('tieba', 'USERID')  # 要查找的用户ID

# tieba_name = 'python'
# pages = 2
# target_id = '小明'

# 贴吧URL和需要获取的页数
url = f'https://tieba.baidu.com/f?kw={tieba_name}&pn='


# 遍历每一页
for page in range(1, pages + 1):
    print(f'正在检索{page}页')
    page_url = url + str((page - 1) * 50)
    page_html = requests.get(page_url).text
    soup = BeautifulSoup(page_html, 'html.parser')
    link_arr = soup.find_all('a', class_='j_th_tit')
    # 获取每个帖子的标题和链接
    if len(link_arr):
        for item in link_arr:
            title = item.get_text().strip()
            link = 'https://tieba.baidu.com' + item.get('href')
            
            # 访问帖子链接，获取帖子的HTML代码
            post_html = requests.get(link).text
            post_soup = BeautifulSoup(post_html, 'html.parser')
                
            # 搜索HTML代码中是否包含目标ID
            if post_soup.find(string=target_id):
                print(f'帖子【{title}】({link})中有用户{target_id}的回复')
            else:
                print('没有找到')
    else:
        print('连接超时或解析错误')



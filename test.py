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
LINK = config.get('user', 'LINK')
print(LINK)

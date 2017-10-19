# -*- coding: utf-8 -*-
import scrapy
import sys
from email.mime.text import MIMEText
import smtplib
from send_email import send_email
#from gupiao.items import GupiaoItem
reload(sys)
sys.setdefaultencoding('utf-8')

class GpSpider(scrapy.Spider):
    name = "gp"
    str = 'http://hq.sinajs.cn/list='
    gp_full_code = {'奥瑞德':'600666','中国石化':'600028'}
    gp_code =(gp_full_code['中国石化'],gp_full_code['奥瑞德'])
    group_code = ()
    for each in gp_code:
        sstr = str +'sh'+''.join(each)
        group_code =group_code + (sstr,)
    #allowed_domains = ["http://stockpage.10jqka.com.cn/600028/"]
    start_urls = group_code

    def parse(self, response):
        #selector = scrapy.Selector(response)
        #gp_data = selector.xpath('//div[@id="price"]')
        content = response.body.decode('gb2312')
        gp_data = (content).split(",")
        gp_name = gp_data[0].split("\"")[1]
        gp_price = gp_data[2]
        print  gp_name , gp_price
        gp_price ='18'
        if gp_name =="奥瑞德":
            if  float(gp_price) > 17.0:
                send_email(gp_name+"  ", gp_price)
		print '1+1=2'
        if gp_name =="中国石化":
            if  float(gp_price) > 20.0:
                send_email(gp_name+"  ", gp_price)


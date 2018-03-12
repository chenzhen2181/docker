# -*- coding: utf-8 -*-
import scrapy
import sys

from email.mime.text import MIMEText
import smtplib
from send_email import send_email
import read_data
import is_send_email
from gupiao.items import GupiaoItem
reload(sys)
sys.setdefaultencoding('utf-8')
is_send_email._init()                                                     #初始化
class GpSpider(scrapy.Spider):
    name = "gp"
    url = 'http://hq.sinajs.cn/list='                                    #新浪实时股票数据接口
#    gp_full_code = {'奥瑞德':'600666','中国石化':'600028'}
#    gp_code =(gp_full_code['中国石化'],gp_full_code['奥瑞德'])
    gp_code = read_data.gp_code
#    print gp_code
    group_gp_url = ()
    for each in gp_code:
#        gp_url = url +'sh'+''.join(each)      #sh:沪市
        gp_url = url +''.join(each)
        group_gp_url =group_gp_url + (gp_url,)
#    print group_gp_url
    start_urls = group_gp_url

    def parse(self, response):
        content = response.body.decode('gbk')
        gp_url_data = (content).split(",")
#        gp_url_name = gp_url_data[0].split("\"")[1]                        #提取网站中股票名称
        gp_url_code = gp_url_data[0].split("hq_str_")[1].split("=")[0]      #提取网站中股票代码
#        print gp_url_code
        gp_url_now_price = gp_url_data[2]                                       #提取网站中股票当前价格
        gp_url_yesterday_price = gp_url_data[1]                                 #提取网站中股票昨天价格
        gp_url_date = gp_url_data[-3]
        item = GupiaoItem()

#        print  gp_url_code , gp_url_now_price ,is_send_email.is_send_emial_list[str(gp_url_code)]
        if gp_url_code in read_data.gp_code and not  is_send_email.is_send_emial_list[str(gp_url_code)]:   #判断1、网站上的股票代码是否属于我们需要的股票代码；2、判断该股票代码没发送email
            num = read_data.gp_code.index(gp_url_code)    #查找网站中股票代码在数据json中对应的股票序号
            print  is_send_email.is_send_emial_list[str(gp_url_code)]
            print  type(is_send_email.is_send_emial_list[str(gp_url_code)])
            print   str(gp_url_code)
          #  print str(is_send_email.IS_sent_email[gp_url_code])
            if read_data.gp_value_max[num] != "" :                          #判断数据json中的最大值是否为空值
                if (float(gp_url_now_price) >=  float(read_data.gp_value_max[num])) or  (float(gp_url_now_price) <= float(read_data.gp_value_min[num])):
                    send_email(read_data.gp_name[num] + "  ", gp_url_now_price)
                    is_send_email.is_send_emial_list[str(gp_url_code)] = True
                    is_send_email.change_value(is_send_email.is_send_emial_list)
#                    print "a"+ str(is_send_email.is_send_emial_list[str(gp_url_code)])
                    item['gp_w_code'] = gp_url_code
                    item['gp_w_name'] = read_data.gp_name[num]
                    item['gp_w_price'] = gp_url_now_price
                    item['gp_w_is_sendemail'] = True
                    item['gp_w_date'] = gp_url_date
                    yield item

                    #IS_sent_email[gp_url_code] = True
                    #list = {read_data.gp_name[num],gp_url_code,gp_url_now_price,True}
                    #write_data.write_json_data(list)
                  #  os.system('/etc/init.d/cron stop')                      #停止cron服务
#                print read_data.gp_value_max[num], gp_url_now_price ,read_data.gp_value_min[num]
            if (float(gp_url_now_price) >= float(gp_url_yesterday_price) * (1+float(read_data.gp_percent[num]))) or (float(gp_url_now_price) <= float(gp_url_yesterday_price) * (1-float(read_data.gp_percent[num]))):
                send_email(read_data.gp_name[num] + "  ", gp_url_now_price + "当前价格变化超过" + read_data.gp_percent[num])
                is_send_email.is_send_emial_list[str(gp_url_code)] = True
                is_send_email.change_value(is_send_email.is_send_emial_list)
#                print  "a"+ str(is_send_email.is_send_emial_list[str(gp_url_code)])
                item['gp_w_code'] = gp_url_code
                item['gp_w_name'] = read_data.gp_name[num]
                item['gp_w_price'] = gp_url_now_price
                item['gp_w_is_sendemail'] = True
                item['gp_w_date'] = gp_url_date
                yield item








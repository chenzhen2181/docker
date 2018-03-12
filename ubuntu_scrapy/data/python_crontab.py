# -*- coding: utf-8 -*-

from crontab import CronTab
import os
'''
59 23 * * * /home/oracle/scripts/alert_log_archive.sh >/dev/null 2>&1
crontab 文件中每个条目中各个域的意义和格式：
第一列 分钟： 1——59
第二列 小时： 1——23(0表示子夜)
第三列 日 ： 1——31
第四列 月 ： 1——12
第五列 星期： 星期0——6(0表示星期天，1表示星期一、以此类推)
第六列 要运行的命令
我们暂且用C1、C2、C3、C4、C5、C6代表这六列，前面五列通过组合方式来决定执行脚本的频率，最小频率为每分钟执行一次，其中Cn可以用 * ; */n ; T1-T2; a,b,c; 四种形式来表示：
当 C1 为 * 时表示每分钟都要执行脚本，C2 为 * 时表示每小时都要执行程式，依次类推.....
当 C1 为 T1-T2 时表示从第 T1 分钟到第 T2 分钟这段时间内要执行，C2 为 T1-T2 时表示从第 T1 到第 T2 小时都要执行，依次类推....
当 C1 为 */n 时表示每 n 分钟的时间间隔执行一次，C2 为 */n 表示每隔n小时的间隔执行一次，依次类推.....
当 C1 为 a, b, c,... 时表示第 a, b, c,... 分钟要执行，C2 为 a, b, c,... 时表示第 a, b, c...个小时要执行，依次类推....
下面列举几个例子供大家参考
1： 59 23 * * * /home/oracle/scripts/alert_log_archive.sh >/dev/null 2>&1
表示每天23点59分执行脚本/home/oracle/scripts/alert_log_archive.sh
2: */5 * * * * /home/oracle/scripts/monitoring_alert_log.sh >/dev/null 2>&1
表示每5分钟执行一次脚本/home/oracle/scripts/monitoring_alert_log.sh
3： 0 20 * * 1-5 mail -s "**********" kerry@domain.name < /tmp/maildata
周一到周五每天下午 20:00 寄一封信给 kerry@domain.name
..............................................
关于 >/dev/null 2>&1 的解释：
0表示键盘输入
1表示标准输出
2表示错误输出.
'''



# 股票爬虫：

gupiao_cron  = CronTab(user=True)                                                               #定时启动股票程序
gupiao_job = gupiao_cron.new(command = 'cd /data/gupiao && python2.7 /data/gupiao/main_gp.py > /data/mylog.log 2>&1')                #执行command命令
gupiao_job.setall('* * * * *')                                                               #每天9点-16点，每分钟运行
gupiao_job.set_comment("gupiao_0.1")
gupiao_job.enable()
gupiao_cron.write()

gupiao_init_cron = CronTab(user=True)                                                           #定时初始化
gupiao_init_job = gupiao_init_cron.new(command = 'cd /data/gupiao && python2.7 /data/gupiao/gupiao/spiders/__init__.py > /data/mylog_sendeamil_init.log 2>&1')
gupiao_init_job.setall('*/5 * * * *')                                                       #每天9点-16点，每半小时运行
gupiao_init_job.set_comment("gupiao_0.1")
gupiao_init_job.enable()
gupiao_init_cron.write()

#在shell中通过命令crontab -l查看，是否创建成功：

#清除定时语句
# os.system('sed -i \'/gupiao_0.1/d\' /var/spool/cron/crontabs/root')						#删除/var/spool/cron/root中包含"every minute"的行;\'为转义的'
# 或在shell中通过命令sed -i '/gupiao_0.1/d' /var/spool/cron/crontabs/root  删除/var/spool/cron/root中包含"gupiao_0.1"的行
os.system('ln -s /usr/local/bin/scrapy /usr/bin/scrapy ')               #建立软链接，避免系统找不到scrapy
os.system('/etc/init.d/cron start')                     #启动cron服务


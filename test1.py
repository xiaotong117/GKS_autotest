#!/usr/bin/python2.7.5
#encoding=utf-8

from appium import webdriver
import requests,time,unittest,os,base64

PKG_name = "com.pp.infonew1"
TITLE = "天气温馨提示"


class sdkBaseTest(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'  # 手机平台
        desired_caps['platformVersion'] = '4.1'  # 安卓版本，这里要根据自己手机进行修改
        desired_caps['deviceName'] = '16a94b82'  # 设备名称，通过adb devices获取
        desired_caps['appPackage'] = PKG_name  # 要打开的app名称
        desired_caps['appActivity'] = 'com.getui.demo.GetuiSdkDemoActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep(5)
        cid = self.driver.find_element_by_id(PKG_name + ":id/tvclientid").text
        appidm = self.driver.find_element_by_id(PKG_name + ":id/tvappid").text
        appid = appidm.split("=")[1].strip()

        print("cid = " + cid)
        print("appid = " + appid)

    def tearDown(self):
        self.driver.quit()

    def test_push_notification(self):
        message = '{"action":"pushmessage","appkey":"110000","appid":"WDRtfrJBuS8vdjf1UHmAS9","id":"cmdid","messageid":"11111","taskid":"TASK_ID","push_info":{"action_key":"确定","badge":"1","sound":"cow.caf","message":"message"},"action_chains":[{"notifyStyle":1,"second_icon_url":"@url:http://s1.hao123img.com/res/images/search_logo/image.png ","logo_url":"http://s1.hao123img.com/res/images/search_logo/image.png ","stype":"notification","actionid":"1","logo":"demo.png","isFloat":true,"text":"这个是图片","do":"100","title":"测试","timestamp":true},{"actionid":"100","type":"null"}]}'
        url = "http://192.168.10.29:8090/login.htm"
        url2 = 'http://192.168.10.29:8090/pushTest.htm?' + 'clientID=' + cid.decode('utf-8') + '&clientData=' + message.decode('utf-8')
        mycookie = {'username': 'admin', 'password': '111111'}
        s = requests.session()
        s.post(url, data=mycookie)
        r = s.post(url2)
        list = r.text.split(':')
        taskID = list[1].strip()
        print("taskID = " + taskID)
        taskID = "DoLx4RU28M7RCtaRm18O17"

        # 验证（推送和验证最好分开，但后面要用到taskID的值，不知如何传值）
        # 1.下拉查看通知
        score = 0
        self.driver.open_notifications()
        title = self.driver.find_elements_by_class_name('android.widget.TextView')
        for t in title:
            if TITLE.decode('utf-8') in t.text:
                score += 1
                t.click()
                break

        #2.截图过程
        name = "notification"
        if not os.path.exists("./screenshots/"):
            # os.mkdir("./test_reports/screenshots/")   报错：[Error 3] :”系统找不到该路径”
            # mkdir只能在已存在的文件夹里创建子文件夹。如果想实现程序想要的直接创建多级目录的目标，则需要另外一个函数“makedirs”
            os.makedirs("./screenshots/")
            self.driver.get_screenshot_as_file("./screenshots/"  + name + "_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".png")
            #截图失败，不是同一级目录

        # 3.查看日志
        path = "/sdcard/libs/" + PKG_name + "." + time.strftime("%Y-%m-%d", time.localtime()) + ".log" #文件路径/sdcard/libs/com.pp.infonew1.2018-06-21.log
        logsfile = self.driver.pull_file(path)
        logs = base64.b64decode(logsfile).decode('utf-8')#先解码byte转字符串，再用utf-8编码
        print(logs)
        SUCCESS_LOG = taskID.decode('utf-8') + "|1"
        # print("SUCCESS_LOG = " + SUCCESS_LOG)
        # for line in logs:
        #     print(line)
        #     if SUCCESS_LOG.decode('utf-8') in line:
        #         score += 1
        #         break
        if SUCCESS_LOG.decode('utf-8') in logs:
            score += 1


        if score > 1:
            print("验证成功！")
        else :
            print("验证失败...")
            print(score)



if __name__ == "__main__":
    unittest.main()



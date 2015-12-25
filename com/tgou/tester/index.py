# coding=UTF-8

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time


class IndexTester:
    __driver = ""
    __page_name = "首页"
    __sleep = 2

    def __init__(self, webdriver):
        print "======================%s测试初始化========================" % self.__page_name
        print "=========================加载驱动=========================="
        self.__driver = webdriver

    """
    访问首页
    """
    def __visit_index(self):
        print "=========================访问%s==========================" % self.__page_name
        url = "http://m.51tiangou.com/index.html"
        print "%sURL: %s" % (self.__page_name, url)
        print "----------------------------------------------------------"
        self.__driver.get(url)
        print "等待%s加载中................." % self.__page_name
        print "----------------------------------------------------------"
        WebDriverWait(self.__driver, 10).until(
                expected_conditions.presence_of_element_located(
                        (By.XPATH, "//*[@id='index_banner']/div/div[1]/ul/li/a"))
        )
        print "%s加载完毕" % self.__page_name

    """
    返回活动列表的标题/链接
    """
    def __fetch_activity(self):
        print "========================获取活动列表========================"
        activities = self.__driver.find_elements_by_xpath("//*[@id='index_banner']/div/div[1]/ul/li/a")
        activity_metas = []
        if len(activities) > 0:
            print "-------------------------取得活动: %d条----------------------" % len(activities)
            for activity in activities:
                url = activity.get_attribute("href")
                image = activity.find_element_by_tag_name("img")
                title = image.get_attribute("title")
                activity_meta = {"title": title, "url": url}
                activity_metas.append(activity_meta)
                print "%s: %s" % (title, url)
        else:
            print "活动列表为空"
        return activity_metas

    """
    循环访问活动
    """
    def __visit_activity(self, activity_metas):
        if len(activity_metas) > 0:
            print "-------------------------访问活动页------------------------"
            for activity_meta in activity_metas:
                print "活动:", activity_meta["title"], "URL:", activity_meta["url"], "停留:", self.__sleep,"秒"
                self.__driver.get(activity_meta["url"])
                time.sleep(int(self.__sleep))
                self.__driver.back()
                time.sleep(int(self.__sleep))
                print "----------------------------------------------------------"

    """
    测试执行入口
    """
    def execute(self):
        try:
            self.__visit_index()
            activity_metas = self.__fetch_activity()
            self.__visit_activity(activity_metas)
        except Exception, data:
            print "==========================发生异常========================="
            print Exception, data
        print "==========================测试%s结束=======================" % self.__page_name
        print ""

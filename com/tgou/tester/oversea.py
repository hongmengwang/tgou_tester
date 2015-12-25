# coding=UTF-8

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time


class OverSeaTester:
    __driver = ""
    __page_name = "跨境直购"
    __sleep = 2

    def __init__(self, webdriver):
        print "======================%s测试初始化========================" % self.__page_name
        print "=========================加载驱动=========================="
        self.__driver = webdriver

    """
    访问跨境直购
    """
    def __visit_index(self):
        print "=========================访问%s==========================" % self.__page_name
        url = "http://m.51tiangou.com/overseas/index.html"
        print "%sURL: %s" % (self.__page_name, url)
        print "----------------------------------------------------------"
        self.__driver.get(url)
        print "等待%s加载中................." % self.__page_name
        print "----------------------------------------------------------"
        WebDriverWait(self.__driver, 10).until(
                expected_conditions.presence_of_element_located(
                        (By.XPATH, "//*[@id='muYingList']/section/ul/a"))
        )
        print "%s加载完毕" % self.__page_name

    """
    返回母婴热卖列表的标题/链接
    """
    def __fetch_mother_baby(self):
        print "========================获取母婴热卖列表========================"
        mother_babies = self.__driver.find_elements_by_xpath("//*[@id='muYingList']/section/ul/a")
        mother_baby_metas = []
        if len(mother_babies) > 0:
            print "-------------------------取得列表: %d条----------------------" % len(mother_babies)
            for activity in mother_babies:
                url = activity.get_attribute("href")
                dt = activity.find_element_by_tag_name("dt")
                title = dt.text
                activity_meta = {"title": title, "url": url}
                mother_baby_metas.append(activity_meta)
                print "%s: %s" % (title, url)
        else:
            print "母婴热卖列表为空"
        return mother_baby_metas

    """
    循环访问母婴热卖
    """
    def __visit_mother_baby(self, mother_baby_metas):
        if len(mother_baby_metas) > 0:
            print "-------------------------访问活动页------------------------"
            for mother_baby_meta in mother_baby_metas:
                sleep = 2
                print "活动:", mother_baby_meta["title"], "URL:", mother_baby_meta["url"], "停留:", sleep,"秒"
                self.__driver.get(mother_baby_meta["url"])
                time.sleep(int(sleep))
                self.__driver.back()
                time.sleep(int(sleep))
                print "----------------------------------------------------------"

    """
    下拉倒浏览器底部
    """
    def __scroll_to_bottom(self):
        print "==========================滚动到底部========================="
        script_command = "window.scrollTo(0, document.body.scrollHeight);"
        self.__driver.execute_script(script_command)
        print "----------------------------停留%d秒--------------------------" % self.__sleep
        time.sleep(int(self.__sleep))

    """
    测试执行入口
    """
    def execute(self):
        try:
            self.__visit_index()
            mother_baby_metas = self.__fetch_mother_baby()
            self.__visit_mother_baby(mother_baby_metas)
            self.__scroll_to_bottom()
        except Exception, data:
            print "==========================发生异常========================="
            print Exception, data
        print "==========================测试%s结束=======================" % self.__page_name
        print ""

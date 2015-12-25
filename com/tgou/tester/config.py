#coding=UTF-8

from selenium import webdriver
import os


class TgouTesterConfig:

    def __init__(self):
        print "========================TgouDriver初始化========================"

    """
    返回当前工程绝对路径
    """
    @staticmethod
    def __get_enviroment_path():
        current_path = os.getcwdu()
        project_path = current_path[0:current_path.find("com")]
        return project_path

    """
    返回错误存储路径
    """
    @staticmethod
    def get_error_path():
        environment_path = TgouTesterConfig.__get_enviroment_path()
        error_path = environment_path + "error/"
        return error_path

    """
    返回firefox浏览器驱动
    """
    @staticmethod
    def get_firefox_driver():
        print "=====================获取Firefox浏览器驱动======================="
        print ""
        driver = webdriver.Firefox()
        return driver

    """
    返回chrome浏览器驱动
    """
    @staticmethod
    def get_chrome_driver():
        print "====================获取Chrome浏览器驱动====================="
        print ""
        chrome_driver_path = TgouTesterConfig.__get_enviroment_path() + "chromedriver"
        driver = webdriver.Chrome(chrome_driver_path)
        return driver

    """
    关闭传入的浏览器
    """
    @staticmethod
    def close(driver):
        print "=========================关闭浏览器==========================="
        print "关闭浏览器中................."
        print "------------------------------------------------------------"
        try:
            driver.quit()
            print "关闭浏览器成功"
        except Exception, error:
            print "关闭浏览器发生异常", Exception, error

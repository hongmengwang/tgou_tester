# coding=UTF-8

from com.tgou.tester.index import IndexTester
from com.tgou.tester.oversea import OverSeaTester
from com.tgou.tester.config import TgouTesterConfig
import os
import time

driver = None
try:
    """
    获取chrome驱动
    """
    driver = TgouTesterConfig.get_chrome_driver()

    """
    测试首页
    """
    index_tester = IndexTester(driver)
    index_tester.execute()

    """
    测试跨境直购物
    """
    oversea_tester = OverSeaTester(driver)
    oversea_tester.execute()

except Exception, error:
    """
    判断异常图片路径是否存在,不存在则创建
    """
    error_path = TgouTesterConfig.get_error_path()
    if not os.path.exists(error_path):
        os.makedirs(error_path)
    """
    根据当前时间戳保存jpg图片
    """
    error_file = error_path + str(int(time.time())) + ".jpg"
    driver.get_screenshot_as_file(error_file)
    print "===========================发生异常=========================="
    print Exception, error
finally:
    """
    关闭浏览器
    """
    TgouTesterConfig.close(driver)

from selenium.webdriver import Remote
from selenium.webdriver.chrome import options
from selenium.common.exceptions import InvalidArgumentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class ReuseChrome(Remote):

    def __init__(self, command_executor, session_id):
        self.r_session_id = session_id
        Remote.__init__(self, command_executor=command_executor, desired_capabilities={})

    def start_session(self, capabilities, browser_profile=None):
        """
        重写start_session方法
        """
        if not isinstance(capabilities, dict):
            raise InvalidArgumentException("Capabilities must be a dictionary")
        if browser_profile:
            if "moz:firefoxOptions" in capabilities:
                capabilities["moz:firefoxOptions"]["profile"] = browser_profile.encoded
            else:
                capabilities.update({'firefox_profile': browser_profile.encoded})

        self.capabilities = options.Options().to_capabilities()
        self.session_id = self.r_session_id
        self.w3c = False

id = 'fa69d2e9b2dbb525f79575126bfe883f'
url = 'http://127.0.0.1:53619'
driver = ReuseChrome(command_executor=url, session_id=id)
wait = WebDriverWait(driver, 10) #等待的最大时间
Min=20

driver.get("https://detail.damai.cn/item.htm?spm=a2oeg.search_category.0.0.1412545dZWwe9s&id=603647548586&clicktitle=%E8%8A%B1%E7%B2%A5%E2%80%9C%E4%B8%A4%E7%A2%97%E4%B8%89%E7%99%BE%E2%80%9D%E5%85%A8%E5%9B%BD%E5%B7%A1%E6%BC%94%20%E5%8C%97%E4%BA%AC%E7%AB%99")
print("1")
driver.find_element_by_xpath("/html[@class='ks-webkit537 ks-webkit ks-chrome77 ks-chrome']/body/div[@class='perform']/div[@class='w1200 box flex']/div[@class='flex1']/div[@class='hd']/div[@class='cont']/div[@class='order']/div[@class='perform__order__box']/div[@class='perform__order__select']/div[@class='select_right']/div[@class='select_right_list']/div[@class='select_right_list_item sku_item'][3]").click()
print("2")
def buy():
    start = time.clock()
    try:
        # 获取搜索点击按钮
        submit = wait.until(
            #判断该元素是否可以点击
            EC.element_to_be_clickable((By.XPATH,"/html[@class='ks-webkit537 ks-webkit ks-chrome77 ks-chrome']/body/div[@class='perform']/div[@class='w1200 box flex']/div[@class='flex1']/div[@class='hd']/div[@class='cont']/div[@class='order']/div[@class='perform__order__box']/div[9]/div[@class='buybtn']"))
        )
        submit.click()
    except Exception:
        print("Not found!")
    end = time.clock()
    print(end-start)
    start = time.clock()
    print("3")
    try:
        submit = wait.until(
            # 判断该元素是否可以点击
            EC.element_to_be_clickable((By.XPATH,"/html[@class='ks-webkit537 ks-webkit ks-chrome77 ks-chrome']/body/div[@class='w1200']/div[@id='container']/div[@id='confirmOrder_1']/div[@class='dm-ticket-buyer']/div[@class='ticket-buyer-select']/div[@class='next-row next-row-no-padding buyer-list']/div[@class='next-col buyer-list-item']/label"))
        )
        submit.click()
    except Exception:
        print("Not found!")

    end = time.clock()
    print(end-start)
    start = time.clock()

    print("4")
    try:
        submit = wait.until(
            # 判断该元素是否可以点击
            EC.element_to_be_clickable((By.XPATH,"/html[@class='ks-webkit537 ks-webkit ks-chrome77 ks-chrome']/body/div[@class='w1200']/div[@id='container']/div[@id='confirmOrder_1']/div[@class='dm-ticket-buyer']/div[@class='ticket-buyer-select']/div[@class='next-row next-row-no-padding buyer-list']/div[@class='next-col buyer-list-item']/label/span[@class='next-checkbox-label']"))
        )
        submit.click()
    except Exception:
        print("Not found!")

    end = time.clock()
    print(end-start)
    start = time.clock()
    print("5")

    try:
        submit = wait.until(
            # 判断该元素是否可以点击
            EC.element_to_be_clickable((By.XPATH,"/html[@class='ks-webkit537 ks-webkit ks-chrome77 ks-chrome']/body/div[@class='w1200']/div[@id='container']/div[@id='confirmOrder_1']/div[@class='submit-wrapper']/button[@class='next-btn next-btn-normal next-btn-medium']"))
        )
        submit.click()
    except Exception:
        print("Not found!")

    end = time.clock()
    print(end-start)
    start = time.clock()
    print("6")

while 1:
        if Min == time.localtime().tm_min:
            print("开始抢票")
            buy()
            print("抢票成功")
# driver.find_element_by_xpath("/html[@class='ks-webkit537 ks-webkit ks-chrome77 ks-chrome']/body/div[@class='perform']/div[@class='w1200 box flex']/div[@class='flex1']/div[@class='hd']/div[@class='cont']/div[@class='order']/div[@class='perform__order__box']/div[@class='perform__order__select']/div[@class='select_right']/div[@class='select_right_list']/div[@class='select_right_list_item sku_item'][2]/div[@class='skuname']")
# driver.find_element_by_xpath("/html[@class='ks-webkit537 ks-webkit ks-chrome77 ks-chrome']/body/div[@class='perform']/div[@class='w1200 box flex']/div[@class='flex1']/div[@class='hd']/div[@class='cont']/div[@class='order']/div[@class='perform__order__box']/div[7]/div[@class='buybtn']").click()
#/html[@class='ks-webkit537 ks-webkit ks-chrome77 ks-chrome']/body/div[@class='w1200']/div[@id='container']/div[@id='confirmOrder_1']/div[@class='dm-ticket-buyer']/div[@class='ticket-buyer-select']/div[@class='next-row next-row-no-padding buyer-list']/div[@class='next-col buyer-list-item']/label/span[@class='next-checkbox-label']
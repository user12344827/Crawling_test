from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def initialize_driver():
    """初始化 WebDriver 並設定無頭模式"""
    chrome_options = Options()
    chrome_options.add_argument("headless")  # 無頭模式
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    return driver

def crawl_websites(driver, test_urls):
    """爬取網站並取得截圖"""
    list_test_report = []
    
    for index in range(len(test_urls)):
        dict_test_report = {"item": "", "response": "", "screenshot": ""}
        
        driver.get(test_urls[index])
        dict_test_report["screenshot"] = snapshot(driver, index)
        
        list_test_report.append(dict_test_report)
    
    return list_test_report

# 保存網頁截圖
def snapshot(driver, path):
    """儲存網頁截圖"""
    driver.save_screenshot("./" + str(path) + ".png")
    return str(path) + ".png"
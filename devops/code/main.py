from dotenv import load_dotenv
from req import api_test
from reports import load_test_plan, generate_report
from crawler import initialize_driver, crawl_websites
from db import drop_and_create, insert_data

load_dotenv()
drop_and_create()

# 讀取測試計畫
test_urls = load_test_plan()

# 初始化 WebDriver
driver = initialize_driver()

# 執行爬蟲取得截圖
list_test_report = crawl_websites(driver, test_urls)

# 填充 API 測試結果
for index, report in enumerate(list_test_report):
    report["item"], report["response"] = api_test(test_urls[index])

# 產生測試報告
generate_report(list_test_report)

# 插入資料
insert_data(list_test_report)

# 關閉 WebDriver
driver.quit()
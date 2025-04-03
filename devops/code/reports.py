import csv
from datetime import datetime

# python 開 csv
def load_test_plan():

    # 用來儲存所有擷取到的 URL
    urls =[]
	
    with open('general.csv', 'r',encoding='utf-8') as file:
        reader = csv.reader(file)
		
		# 跳過表頭
        next(reader)
		
		# 擷取每一列中的第二個欄位（URL）
		
        for row in reader:
        	# 假設 URL 是第二列，即 row[1]
            url = row[1]
            urls.append(url)
    return urls

def generate_report(output_files):
    timestamp = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    filename = f'report-{timestamp}.csv'
        
    # 打開每個檔案進行寫入
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['item', 'response', 'screenshot'])
            
        # 寫入標題
        writer.writeheader()
            
        # 寫入資料
        writer.writerows(output_files)
        
    print(f"Report saved as {filename}")  # 顯示生成的文件名


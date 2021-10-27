import time, os, ftplib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

pathDownload = r"C:\Users\Asus\Documents\Cisco\projetos\Python\2\temp\\"

prefs = {"profile.default_content_settings.popups": 0,
        "download.default_directory": pathDownload,
        "directory_upgrade": True}

options = Options()
options.add_experimental_option('prefs', prefs)
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")

driver= webdriver.Chrome(options=options, service_log_path='NUL',executable_path=r'./chromedriver.exe')
driver.get('https://dashboards.flowbix.com/grafana/login')

# Section: Login
# 
# Collect login input via XPATH.
sendUsername = driver.find_element(By.XPATH, '/html/body/grafana-app/div/div/react-container/div/div/div[2]/div/div/form/div[1]/div[2]/div/div/input')
sendUsername.send_keys('cliente.licknet')
# Collect password input via XPATH.
sendPassword = driver.find_element(By.XPATH, '/html/body/grafana-app/div/div/react-container/div/div/div[2]/div/div/form/div[2]/div[2]/div/div/input')
sendPassword.send_keys('cliente.licknet1728')
# Collect button submit via XPATH.
sendSubmit = driver.find_element(By.XPATH, '/html/body/grafana-app/div/div/react-container/div/div/div[2]/div/div/form/button').click()

# Section: Entering in board
#
# Collect board
time.sleep(10)
clickBoard = driver.find_element(By.XPATH, '/html/body/grafana-app/div/div/react-container/div/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div/div[2]/div/plugin-component/panel-plugin-dashlist/grafana-panel/ng-transclude/div/div[1]/div/div[2]/a/div/div').click()

#
# 
time.sleep(10)
clickLabel = driver.find_element(By.XPATH, '/html/body/grafana-app/div/div/react-container/div/div[2]/div/div[1]/div/div[2]/div[12]/div/div[1]/div/div[1]').click()

time.sleep(1)
clickInspect = driver.find_element(By.XPATH, '/html/body/grafana-app/div/div/react-container/div/div[2]/div/div[1]/div/div[2]/div[12]/div/div[1]/div/div[1]/div/div/div[2]/ul/li[5]').click()

time.sleep(1)
clickDataOptions = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div').click()

time.sleep(1)
clickApplyPanel = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div[2]/div/div/div/div/div[1]/div/div[2]/div/label').click()

time.sleep(1)
clickDownloadExcelType = driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div[2]/div/div/div/div/div[3]/div/div[2]/div/label').click()

time.sleep(1)
clickDownloadFile = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div[1]/div[1]/button').click()

time.sleep(2)

ftp = ftplib.FTP()
host = "192.168.2.8"
port = 21
ftp.connect(host, port)

try:
    if ftp.login("tin", "123"):
        for item in os.listdir(pathDownload):
            fileRenamed = 'doc_relatorio_sao-mateus.csv'

            os.rename(rf'.\temp\{item}', rf'.\temp\{fileRenamed}')

            try:
                uploadFile = open(rf'.\temp\{fileRenamed}','rb')
                ftp.storbinary(rf'STOR {fileRenamed}', uploadFile)
                uploadFile.close()
                time.sleep(1)
                os.remove(r'C:\Users\Asus\Documents\Cisco\projetos\Python\2\temp\\' + fileRenamed)
                
            except Exception as errorUpload:
                print(errorUpload)

except Exception as e:
    print (e)

driver.close()
import time, os, ftplib, nmap, warnings, pysftp
from cryptography.utils import DeprecatedIn25
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

pathDownload = r"/home/e3/Report//"

prefs = {"profile.default_content_settings.popups": 0,
        "download.default_directory": pathDownload,
        "directory_upgrade": True}

options = Options()
options.add_experimental_option('prefs', prefs)
options.add_argument("--disable-extensions")
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

pathChrome = Service('/home/e3/SeleniumAutoReport/chromedriver')
driver = webdriver.Chrome(service=pathChrome, options=options)
driver.get('https://dashboards.flowbix.com/grafana/login')
print('Please, await...')


# Section: Login
#
# Collect login input via XPATH.
sendUsername = driver.find_element(By.XPATH, '/html/body/grafana-app/div/div/react-container/div/div/div[2]/div/div/form/div[1]/div[2]/div/div/input').send_keys('cliente.licknet')

# Collect password input via XPATH.
sendPassword = driver.find_element(By.XPATH, '/html/body/grafana-app/div/div/react-container/div/div/div[2]/div/div/form/div[2]/div[2]/div/div/input').send_keys('cliente.licknet1728')

# Collect button submit via XPATH.
sendSubmit = driver.find_element(By.XPATH, '/html/body/grafana-app/div/div/react-container/div/div/div[2]/div/div/form/button').click()


# Section: Entering in board
#
# Collect board
time.sleep(13)
clickBoard = driver.find_element(By.XPATH, '/html/body/grafana-app/div/div/react-container/div/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div/div[2]/div/plugin-component/panel-plugin-dashlist/grafana-panel/ng-transclude/div/div[1]/div/div[2]/a/div/div').click()


# Section: Inspect elements.
#
# Collect button drop button for inspect.
time.sleep(13)
clickLabel = driver.find_element(By.XPATH, '/html/body/grafana-app/div/div/react-container/div/div[2]/div/div[1]/div/div[2]/div[12]/div/div[1]/div/div[1]').click()

# Collect button for entering on inspect.
time.sleep(1)
clickInspect = driver.find_element(By.XPATH, '/html/body/grafana-app/div/div/react-container/div/div[2]/div/div[1]/div/div[2]/div[12]/div/div[1]/div/div[1]/div/div/div[2]/ul/li[5]').click()


# Section: Report
#
# Collect button drop data options.
time.sleep(1)
clickDataOptions = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div').click()

# Collect option panel style..
time.sleep(1)
clickApplyPanel = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div[2]/div/div/div/div/div[1]/div/div[2]/div/label').click()

# Collect type download via XPATH.
time.sleep(1)
clickDownloadExcelType = driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div[2]/div/div/div/div/div[3]/div/div[2]/div/label').click()

# Collect button download via XPATH.
time.sleep(1)
clickDownloadFile = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div[1]/div[1]/button').click()
time.sleep(2)

try:
	ftp = ftplib.FTP()
	host = "192.168.2.2"
	user = "root"
	passw= "samba#2020!!"

	warnings.simplefilter('ignore', DeprecatedIn25)
	checkPort = nmap.PortScanner()
	checkPort.scan(host, '21-22')

	try:
		def rename():
			for item in os.listdir(pathDownload):
				fileRenamed = 'doc_relatorio_sao-mateus.csv'
				os.rename(rf'/home/e3/Report/{item}', rf'/home/e3/Report//{fileRenamed}')
				return fileRenamed

		if(checkPort[host]['tcp'][22]['state'] == "closed"):
			ftp.connect(host, 21)
			if ftp.login(user, passw):
				fileRenamed = rename()
				try:
					uploadFile = open(rf'/home/e3/Report/{fileRenamed}','rb')
					ftp.storbinary(rf'STOR {fileRenamed}', uploadFile)
					uploadFile.close()
					time.sleep(1)

					os.remove(r'/home/e3/SeleniumAutoReport/Report/temp//' + fileRenamed)

				except Exception as errorUpload:
					print(errorUpload)
		elif(checkPort[host]['tcp'][21]['state'] == "closed"):
			cnopts = pysftp.CnOpts()
			cnopts.hostkeys = None
			with pysftp.Connection(host, username=user, password = passw, cnopts=cnopts) as sftp:
				fileRenamed = rename()
				sftp.cwd(r'/home/arquivos_licknet_2019/geral/NOC/Relátorios/Analises')
				sftp.put(rf'/home/e3/Report/{fileRenamed}')
				sftp.close()
	except Exception as ErroFTP:
		print(ErroFTP)

except Exception as e:
    print (e)

driver.close()

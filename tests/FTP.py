import ftplib, os

ftp = ftplib.FTP()
host = "192.168.2.8"
port = 21
ftp.connect(host, port)

try:
	ftp.connect(host, 21)

	if ftp.login(user, passw):
		for item in os.listdir(pathDownload):
		fileRenamed = 'doc_relatorio_sao-mateus.csv'
		os.rename(rf'/home/e3/Report/{item}', rf'/home/e3/Report//{fileRenamed}')
		try:
			uploadFile = open(rf'/home/e3/Report/{fileRenamed}','rb')
			ftp.storbinary(rf'STOR {fileRenamed}', uploadFile)
			uploadFile.close()
			time.sleep(1)

except Exception as e:
    print (e)

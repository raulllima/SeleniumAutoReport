import ftplib, os

ftp = ftplib.FTP()
host = "192.168.2.8"
port = 21
ftp.connect(host, port)

try:
    if ftp.login("tin", "123"):
        for item in os.listdir('./temp'):
            fileRenamed = 'doc_relatorio_sao-mateus.csv'

            os.rename(rf'.\temp\{item}', rf'.\temp\{fileRenamed}')

            try:
                uploadFile = open(rf'.\temp\{fileRenamed}','rb')
                ftp.storbinary(rf'STOR {fileRenamed}', uploadFile)
                uploadFile.close()
            
                os.remove(r'C:\Users\Asus\Documents\Cisco\projetos\Python\2\temp\\' + fileRenamed)
                
            except Exception as errorUpload:
                print(errorUpload)

except Exception as e:
    print (e)
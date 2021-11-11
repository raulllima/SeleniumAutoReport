import warnings, pysftp
from cryptography.utils import DeprecatedIn25
warnings.simplefilter('ignore', DeprecatedIn25)

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

passw = "samba#2020!!"

with pysftp.Connection(host="192.168.2.2", username="root", password = passw, cnopts=cnopts) as sftp:
	sftp.cwd(r"/home/arquivos_licknet_2019/geral/NOC/Relátorios/Analises")
	sftp.put(r"/home/e3/Report/doc_relatorio_sao-mateus.csv")
	sftp.close()

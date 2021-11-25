import nmap

checkPort = nmap.PortScanner()
checkPort.scan('192.168.2.2', '21-22')
print(checkPort['192.168.2.2']['tcp'][21]['state'])

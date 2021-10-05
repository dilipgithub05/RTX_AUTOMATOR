import subprocess
import optparse

parser =optparse.OptionParser()

parser.add_option("-d","--domain",dest="domain",help="used to enter Domain")

(options, arguments) = parser.parse_args()

domain = options.domain


with open('domain.txt','w') as f:
		result =subprocess.run(["assetfinder", domain], stdout=f, stderr=subprocess.PIPE, text=True) 
result.stdout

print("DOMAIN FOUNDED ")

cmd = "cat domain.txt | httpx"
with open('http_domain.txt','w') as u:
	ps = subprocess.Popen(cmd,shell=True,stdout=u,stderr=subprocess.STDOUT)
ps.stdout
print("HTTPX CONVERTING DONE")

cmd = "cat http_domain.txt | gau"
with open('url.txt','w') as v:
	ps = subprocess.Popen(cmd,shell=True,stdout=v,stderr=subprocess.STDOUT)
ps.stdout
print("URL COLLECTED")

cmd = "cat http_domain.txt | aquatone -scan-timeout 500 -screenshot-timeout 300000 -http-timeout 30000"
with open('aquatone.txt','w') as z:
	ps = subprocess.Popen(cmd,shell=True,stdout=z,stderr=subprocess.STDOUT)
ps.stdout
print("SCREENSHOT SUCCESSFULLY TAKEN")


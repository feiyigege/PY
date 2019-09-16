import urllib


url = "http://www.baidu.com"

req = urllib.Request(url)
print (req)

res_data = urllib.urlopen(req)
res = res_data.read()
print (res)

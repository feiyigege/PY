import hashlib
while 1:
    user_input = input('输入你要加密的字符>>')
    data = hashlib.md5()
    data.update(user_input.encode(encoding='utf-8'))
    print('MD5加密前为 ：' + user_input)
    print('MD5加密后为 ：' + data.hexdigest())

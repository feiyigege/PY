import hashlib
while 1:
    user_input = input('������Ҫ���ܵ��ַ�>>')
    data = hashlib.md5()
    data.update(user_input.encode(encoding='utf-8'))
    print('MD5����ǰΪ ��' + user_input)
    print('MD5���ܺ�Ϊ ��' + data.hexdigest())

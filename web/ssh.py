import socket

client=socket.socket()
client.connect(("192.168.1.194",22))

while True:
    cmd=input(">>:").strip()
    if len(cmd)==0:
        continue
    client.send(cmd.encode())
    rec_cmd_size=client.recv(1024)
    #rec_cmd_size=client.recv(1024)   #每次接收可能不是1024，总之，服务端发多少，客户端收多少
    print("接收到的命令结果原大小：",rec_cmd_size)
    client.send("已经准备好接收，server可发送".encode())
    rec_size=0
    rec_data=b''
    while rec_size < int(rec_cmd_size.decode()):
          data=client.recv(1024)
          rec_size+=len(data)
          rec_data+=data
    else:
        print("cmd has received done",rec_size)
        print(rec_data.decode())
client.close()
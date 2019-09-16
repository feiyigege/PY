import sys, os  
  
  
def myspawn(cmdline):  
    argv = cmdline.split()  
    if len(argv) == 0:  
        return   
    program_file = argv[0]  
    pid = os.fork()  
    if pid < 0:  
        sys.stderr.write("fork error")  
    elif pid == 0:  
        # child  
        os.execvp(program_file, argv)  
        sys.stderr.write("cannot exec: "+ cmdline)  
        sys.exit(127)  
    # parent  
    pid, status = os.waitpid(pid, 0)  
    ret = status >> 8  # 返回值是一个16位的二进制数字，高8位为退出状态码，低8位为程序结束系统信号的编号  
    signal_num = status & 0x0F  
    sys.stdout.write("ret: %s, signal: %s\n" % (ret, signal_num))  
    return ret  
  
  
def ssh(host, user, port=22, password=None):  
    if password:  
        sys.stdout.write("password is: '%s' , plz paste it into ssh\n" % (password))  
    cmdline = "ssh %s@%s -p %s " % (user, host, port)  
    ret = myspawn(cmdline)  
  
  
if __name__ == "__main__":  
    host = ''  
    user = ''  
    password = ''  
    ssh(host, user, password=password)  
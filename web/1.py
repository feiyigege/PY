import ssh

myclient = ssh.SSHClient()

myclient.set_missing_host_key_policy(ssh.AutoAddPolicy())

myclient.connect("192.168.227.128", port=22, username="root", password="toor")

stdin, stdout, stderr = client.exec_command("ls -l")

print stdout.read()
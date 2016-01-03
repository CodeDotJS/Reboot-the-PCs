import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:

    for i in range(ip1, ip2): # IP(s) : replace the ip1 and ip2 with your ip ranges

        ip=str(i)

        if(ip!="you ip"): # protect your pc

            try:

                print '......'+ip

                ssh.connect('********'+ip, username='user',password='your password')

                stdin, stdout, stderr = ssh.exec_command("reboot")

            except:

                print "ip not there"

except:

    error=1

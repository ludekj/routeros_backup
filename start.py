import paramiko
from scp import SCPClient
import datetime
import time as t

time = datetime.date.today()

ip = '192.168.1.1'
user = 'xxx'
psw = 'xxx'


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=ip, username=user , password=psw )
stdin, stdout, stderr = ssh.exec_command(f'/export file={time}.rsc')

t.sleep(5)

sftp = SCPClient(ssh.get_transport())
sftp.get(f"{time}.rsc")
sftp.close

t.sleep(5)

sh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=ip, username=user , password=psw )
stdin, stdout, stderr = ssh.exec_command(f'/file remove "{time}.rsc"')

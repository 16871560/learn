__author__ = 'root'

#_*_coding:utf-8_*_

import paramiko,time

import sys,os

start=time.clock()
host='192.168.1.41'
user='root'
password='123.com'
cmd='/sbin/ifconfig eth0'
newpass='32122.com'
connect=paramiko.SSHClient()

connect.load_system_host_keys()
connect.set_missing_host_key_policy(paramiko.AutoAddPolicy())
connect.connect(host,22,user,password,timeout=3)



stdin,stdout,stderr=connect.exec_command("/bin/echo %s | /usr/bin/passwd --stdin %s;/bin/echo 'ok' ;/usr/sbin/userdel" %(newpass,'james') )

spent_time=(time.clock()-start)/1000.0

print 'total spend :',spent_time

for line in (stdout.read(),stderr.read()):
    print line




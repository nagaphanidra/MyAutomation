import telnetlib 

import time 

import sys 

 

HOST = "72.190.26.89" 

user = "admin" 

password = "ciscocisco" 

port = "32769" 

 

telnet = telnetlib.Telnet(HOST,port) 

 

telnet.read_until(b"Username: ") 

telnet.write(user.encode('ascii') + b"\n") 

telnet.read_until(b"Password: ") 

telnet.write(password.encode('ascii') + b"\n") 

telnet.write(b"!PYTHON AUTOMATED SCRIPT! START !\n") 

time.sleep(1) 

telnet.write(b"show clock\n") 

time.sleep(1) 

telnet.write(b"term len 0\n") 

time.sleep(1) 

telnet.write(b"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n") 

telnet.write(b"show ip interface brief | i up\n") 

time.sleep(1) 

telnet.write(b"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n") 

telnet.write(b"show interfaces status | i connected\n") 

time.sleep(1) 

telnet.write(b"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n") 

telnet.write(b"show interfaces description | i up\n") 

time.sleep(1) 

telnet.write(b"!PYTHON AUTOMATED SCRIPT! ENDED !\n") 

 

str_all = telnet.read_very_eager() 

f = open("op.txt", "wb") 

f.write(str_all) 

f.close() 

op1 = open("op.txt") 

content = op1.readline 

print(content) 


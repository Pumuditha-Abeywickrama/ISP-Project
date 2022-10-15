#!/usr/bin/env python

import http.server
import socketserver

print """
	*--------------------------------------*
	|       programmed by : mwmt           |    
	*--------------------------------------*
       _     __             _     __  ____  
      || \  // | \ \     / || \  // |  ||   
      ||  \//  |  \_\/\_/  ||  \//  |  || 
	
	           SimpleHTTPServer
	           ----------------

"""

port = 4444

server = http.server.SimpleHTTPRequestHandler
request = socketserver.TCPServer(("",port),server)
print("server is up ....",port)
request.serve_forever()
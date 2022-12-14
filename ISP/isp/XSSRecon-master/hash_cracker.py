#!/usr/bin/env python

print """
	*--------------------------------------*
	|       programmed by : mwmt           |    
	*--------------------------------------*
       _     __             _     __  ____  
      || \  // | \ \     / || \  // |  ||   
      ||  \//  |  \_\/\_/  ||  \//  |  || 
	
	            python hacking
	            --------------
"""
import hashlib
from optparse import *

def hashing(word, algorithm):
	""" algorithms available: ['md4', 'md5', 'sha1', 'sha256' .... etc] """
	hash_type = hashlib.new(algorithm)
	hash_type.update(word)
	return hash_type.hexdigest()


parser = OptionParser("""

#Usage:

        python cracker.py -w <hash> -t <type> -f <word list file>

#Example:

	python cracker.py -w 7052cad6b415f4272c1986aa9a50a7c3 -t md5 -f wordlist.txt
""")
parser.add_option("-w",dest="ha_sh",type="string",help="enter hash string")
parser.add_option("-t",dest="ty_pe",type="string",help="enter type the hash")
parser.add_option("-f",dest="fi_le",type="string",help="enter file word list")
(options,args) = parser.parse_args()
if options.ha_sh == None or options.ty_pe == None or options.fi_le == None:
    print(parser.usage)
    exit(0)
else:
    ha_sh = str(options.ha_sh)
    ty_pe = str(options.ty_pe)
    fi_le = str(options.fi_le)

    read_list = open(fi_le,'r')
    for word in read_list:
    	word = word.strip("\n")
    	result = hashing(word, ty_pe)
    	print("Testing: "+word)
    	if ha_sh == result:
    		print ("\nHash Found: [ {} ] >> word: [ {} ]".format(result,word))
    		exit(0)
	else:
		continue

print("\n\thash not found :(\n")

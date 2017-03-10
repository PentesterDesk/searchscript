#!/usr/bin/python

import socket
import urllib
import urllib2
import os, re
import sys
import cookielib



def cls():

	if os.name == "nt":
		os.system('cls' and 'color a')
	else:
		os.system('clear')

cls()

banner = '''
\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
\t\t| Bing Search script
\t\t| Coded By: Pranav venkat
\t\t| usage: python search.py 
\t\t| Enter any dork: inurl:login.action, site:.com php?id= etc.
\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

print(banner)


def main():
	try:
		searchString = raw_input("Enter Dork or search string: \t")
		cj = cookielib.CookieJar()
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

		shawdow=urllib.quote(searchString,'')
		uniqueSet=set()
		next = 1
		while(next<=101): #you can increase this value depending on your requirement
			url = "http://www.bing.com/search?q=" + shawdow + "&first="+str(next)+"&FORM=QBRE"
			data = urllib2.Request(url)
			box = opener.open(data).read()
			next = next+10
			b = re.findall('<h2><a href="\S+', box)
			for bing in b:				
				x = bing.replace('<h2><a href="https://', "").replace('<h2><a href="http://', "").replace('/"', "").replace('"', "") #this will strip https http /" "
				'''if not x.find(searchString)==1:'''
				print(x)
				uniqueSet.add(x)			
		f= open('nww5.txt', 'w') #full url will be written ( you can skip next step if you want full url )
		for i in uniqueSet:
			f.write(i+"\n")
		f.close()
		f= open('nww5.txt','r')
		removeString = raw_input("Enter the string to be removed: \t") # just put / , which will remove whole other part of url
		f1= open('result.txt', 'w') #only domain name will be present
		for line in f:
			text=line
			head,sep,tail=text.partition(removeString)
			f1.write(head + "\n")
		f1.close()
		f.close()
		
		
	except urllib2.HTTPError:
		pass

'''	except socket.gaierror:
		print ""
		print "Please Enter Valid Domain-Name or IP-Address"
		print "" '''
if __name__ == '__main__':
	main()

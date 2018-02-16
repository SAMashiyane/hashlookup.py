#!/usr/bin/python
import json
import urllib
print"***************************************************"
print"*      Priv8 online Hashlist Cracker              *"
print"*         Coded by SAM355                         *"                      
print"*              ashiyane.org                       *"
print"***************************************************"
print" - Copy all your hashes to hashlist.txt file"
print" - Run hashlookup.py"
print" - Tell us if you enjoyed the result or if you have any other idea ;)"
print" Sali_blue@yahoo.com"

dbs=['md5cracker.org','tmto','md5.net','md5decryption.com','i337.net','md5pass','authsecu','md5crack','md5.my-addr.com','md5online.net']
api="http://md5cracker.org/api/api.cracker.php?database=%s&hash=%s"

def getResult(db,md5):
	result=json.loads(urllib.urlopen(api %(db,md5)).read())
	if result['status'] == True : 
		return result['result'];
	else: 
		return result['message']
	

md5s=open("hashlist.txt","r")
for md5 in md5s:
	md5=md5.strip()
	print('\n\n/'+38*'-'+'\\\n|Hash: '+md5+'|\n|'+38*'-'+'|')
	if len(md5) == 32 :
		print('|Database'+((20-len('Database'))*' ')+'|      Result     |\n|'+38*'-'+'|')
		for db in dbs:
			print('|'+db+((20-len(db))*' ')+'| '+getResult(db,md5))
		print(38*'-')

	else:
		if len(md5) != 0 :
			print('Unsupported length (%i), this script only supports MD5 hashes.' % len(md5))
md5s.close()
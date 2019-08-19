import os, time
import bitlyapi

aa='\033[1;37m'
bb='\033[1;32m'
cc='\033[1;36m'
def generate():
   try:
       url='https://api.whatsapp.com/send?phone='
       num=raw_input(bb+'\n[]'+aa+'Your number(ex:628): ')
       user = 'o_7k0e0ofhp7'
       api = 'R_bdfa2f0ef8384a39b659b3927cee619f'
       b = bitlyapi.BitLy(user, api)
       longurl = url+num
       response = b.shorten(longUrl=longurl)
       time.sleep(2)
       print (bb+'[]'+aa+'Link: '+cc+response['url'])
       print (bb+'[]'+aa+'Generate your live chat successfully')
       print (bb+'[]'+aa+'Follow my instagram @khazulyusseryy')
   except KeyboardInterrupt:
       print (bb+'[]'+aa+'Goodbyee')

if __name__=='__main__':
     #banner
       os.system('cls' if os.name=='nt' else 'clear')
       print (bb+'   _  _ _  _ ____ ___ ____ _    _ __ _ _  _')
       print (cc+'   |/\| |--| |--|  |  ==== |___ | | \| |-:_')
       print ('\x1b[5;32;41m	[*]WhatsLink Generate by me[*]\x1b[0m')
       generate()

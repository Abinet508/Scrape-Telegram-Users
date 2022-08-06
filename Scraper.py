from telethon import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser, InputPeerUserFromMessage
from telethon.errors.rpcerrorlist import (PeerFloodError, UserNotMutualContactError ,
                                          UserPrivacyRestrictedError, UserChannelsTooMuchError,
                                          UserBotError, InputUserDeactivatedError)
from telethon.tl.functions.channels import InviteToChannelRequest
import time, os, sys, json
import  csv


wt = (
   '''
                                                  
  [[ye]]*   )                              (        
[[re]]` )  /(    )        (      )         )\    )  
 [[ye]]( )(_))( /(   (    )\    (      (  ((_)( /(  
[[re]](_(_()) )(_))  )\ )((_)   )\  '  )\  _  )(_)) 
[[gr]]|_   _|((_)_  _(_/( (_) _((_))  ((_)| |((_)_  
 [[gr]]| |  / _` || ' \))| || '  \()/ _ \| |/ _` | 
  |_|  \__,_||_||_| |_||_|_|_| \___/|_|\__,_| 
           version : 1.0
github.com/Abinet508 [[re]][DOnt forget to leave a star]
   '''
)
COLORS = {
   "re": "\u001b[31;1m",
   "gr": "\u001b[32m",
   "ye": "\u001b[33;1m",
}
re = "\u001b[31;1m"
gr = "\u001b[32m"
ye = "\u001b[33;1m"
def colorText(text):
   for color in COLORS:
       text = text.replace("[[" + color + "]]", COLORS[color])
   return text
if sys.version_info[0] < 3:
    telet = lambda :os.system('pip install -U telethon')
elif sys.version_info[0] >= 3:
    telet = lambda :os.system('pip3 install -U telethon')

telet()
time.sleep(1)

sessionc=0

if os.path.isfile('getmem_log.txt'):
    with open(r'getmem_log.txt',encoding='UTF-8') as r:
        data= csv.reader(r,delimiter=",",lineterminator="\n")
      
        if data.line_num==0:    
            api_id = input('Enter api_id: ')
            api_hash = input('Enter api_hash: ')
            with open('getmem_log.txt', 'w') as a:
                a.write(api_id + "," + api_hash)
        
        for line in data:
            api_id=line[0]
            api_hash=line[1]
            if sessionc%10==9:
                sessionc+=1
                print(sessionc)
            client = TelegramClient('anon0', api_id, api_hash)     
            
        
            while True:
            
                async def main():
                    print(gr+"Logged in with session :"+str(sessionc-1))   
                    
                    chats = []
                    channel = []
                    result = await client(GetDialogsRequest(
                        offset_date=None,
                        offset_id=0,
                        offset_peer=InputPeerEmpty(),
                        limit=200,
                        hash=0
                    ))
                
                    chats.extend(result.chats)
                    for a in chats:
                        try:
                            if True:
                                channel.append(a)
                        except:
                            continue

                    a = 0
                    print('')
                    print('')
                    print(ye+'which group you would like to get members from ?')
                    
                    for i in channel:
                        print(gr+'['+str(a)+']', i.title)
                        a += 1
                    if False:
                        print(ye+'Ok. skipping...')
                        continue
                    else: 
                    
                        op = input(ye+'Enter the number of the group from the list: ')

                        opt = int(op)
                        print('')
                        print(ye+'[+] Getting members of '+channel[opt].title)
                        time.sleep(1)
                        target_group = channel[opt]
                        all_participants = []
                        mem_details = []
                        a=open('members.txt', 'r') 
                        result=a.readlines() 
                        if result==[]:
                            pass

                        all_participants = await client.get_participants(target_group,aggressive=True)
                        for user in all_participants:
                            try:

                                if user.id in result:
                                    pass
                                else:
                                    if user.username:
                                        username = user.username
                                    else:
                                        username = ""
                                    if user.first_name:
                                        firstname = user.first_name
                                    else:
                                        firstname = ""
                                    if user.last_name:
                                        lastname = user.last_name
                                    else:
                                        lastname = ""

                                    new_mem = {
                                        'uid': user.id,
                                        'username': username,
                                        'firstname': firstname,
                                        'lastname': lastname,
                                        'access_hash': user.access_hash
                                    }
                                    mem_details.append(new_mem)
                            except ValueError:
                                continue
                        a.close()
                        with open('members.txt', 'a') as w:
                            json.dump(mem_details, w)
                        time.sleep(1)
                        print(ye+'Please wait.....')
                        time.sleep(3)
                        done = input(gr+'[+] Members scraped successfully. (Press enter to Exit)')
                        await client.disconnect()
                with client:
                    if not client.is_user_authorized:
                            continue
                    else:
                            
                            client.loop.run_until_complete(main())


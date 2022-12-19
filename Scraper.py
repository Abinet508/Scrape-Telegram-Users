from telethon import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser, InputPeerUserFromMessage
from telethon.errors.rpcerrorlist import (PeerFloodError, UserNotMutualContactError ,
                                          UserPrivacyRestrictedError, UserChannelsTooMuchError,
                                          UserBotError, InputUserDeactivatedError)
from telethon.tl.functions.channels import InviteToChannelRequest
import time, os, sys, json
from decouple import Config,RepositoryEnv
from qrcode import QRCode
path=os.path.dirname(__file__)

qr = QRCode()
DOTENV_FILE=os.path.join(path,'Environments\.env') 
print(DOTENV_FILE)
config = Config(RepositoryEnv(DOTENV_FILE))
Password = config('Password')
phone_number = config('phone_number')

def gen_qr(token:str):
    qr.clear()
    qr.add_data(token)
    qr.print_ascii()

def display_url_as_qr(url):
    print(url)  # do whatever to show url as a qr to the user
    gen_qr(url)



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
        
async def main(client: TelegramClient):
                    if(not client.is_connected()):
                        await client.connect()
                    
                    print(str( client.get_me(input_peer= True)))
                    if(await client.get_me()==None):
                        qr_login = await client.qr_login()
                        print(client.is_connected())
                        r = False
                        try:
                            while not r:
                                display_url_as_qr(qr_login.url)
                                # Important! You need to wait for the login to complete!
                                try:
                                    r = await qr_login.wait()
                                    #print(r)
                                    try:
                                        await client.sign_in(password=Password)
                                    except:
                                        pass    
                                except:
                                    await qr_login.recreate()
                        except:
                            pass         

                    try:
                        print(gr+"Logged in with session :"+str(client.get_me(input_peer= True)))   
                        print('')
                        chats = []
                        channels = []
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
                                    channels.append(a)
                            except:
                                continue

                        a = 0
                       
                       
                        if result==[]:
                            pass
                        for channel in channels:
                            mem_details = []
                            with open('members.json', 'r') as newfile:
                                    result=json.load(newfile)
                            mem_details=[user["uid"] for user in result]
                            try:
                                print(gr+'================================================================')  
                                print(gr+'================================================================')
                                print(gr+'['+str(a)+']', channel.title)
                                print('================================================================')
                                

                                opt = int(a)
                                a += 1
                               
                                print(ye+'[+] Getting members of '+channels[opt].title)
                                time.sleep(1)
                                target_group = channels[opt]
                                all_participants = []
                            

                                all_participants = await client.get_participants(target_group,aggressive=True)
                                for user in all_participants:
                                    try:

                                        if user.id in mem_details:
                                            print("user: %s is already added" % user.username)
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
                                            result.append(new_mem)
            #                                 with open("members.json", "w") as file:
            # json.dump(data, file)
                                            #mem_details.append(new_mem)
                                    except ValueError:
                                        continue
                                
                                with open("members.json", "w") as file:
                                    json.dump(result, file,indent=4)
                                # with open('members.txt', 'a') as w:
                                #     json.dump(mem_details, w)
                                time.sleep(1)
                                print(ye+'Please wait ...')
                                print(ye+'Writing {} members to a file ...'.format(channel.title))
                                time.sleep(3)
                                print(ye+'================================================================')
                                print('')
                            except Exception as e:
                                print(e)
                                pass     
                    except Exception as e:
                        print(e)
                    finally:
                        await client.disconnect()    

api_id = '4849078'
api_hash = 'bd5f7c2c5ca67f09ed0d536826c05b7b'  
phone = "251937875246" #obviously I have the correct values instead of the * signs                   
client = TelegramClient('Sessions//Scrapersession',api_id,api_hash)                     
client.loop.run_until_complete(main(client))
time.sleep(300)  
# with open('members.json', 'r') as a:
#     data=json.load(a)
# entry={'uid': 355784428, 'username': 'Yonii6693', 'firstname': 'yonii', 'lastname': '', 'access_hash': 8244220150412500864}  
# data.append(entry)
# 3. Write json file
# with open("members.json", "w") as file:
#     json.dump(data, file)
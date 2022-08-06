from telethon import TelegramClient
from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.types import InputPhoneContact
from telethon.tl.functions.contacts import ImportContactsRequest
import csv,os,sys,json
re = "\u001b[31;1m"
gr = "\u001b[32m"
ye = "\u001b[33;1m"
################################################
group_id = 263549607 

################################################
sessionc=1
#countsesion=[]
if os.path.isfile('getmem_log.txt'):
    with open(r'getmem_log.txt',encoding='UTF-8') as r:
        data= csv.reader(r,delimiter=",",lineterminator="\n")
      
            #next(data, None)
            #else:
            #   api_id = input('Enter api_id: ')
            #  api_hash = input('Enter api_hash: ')
            # with open('getmem_log.txt', 'w') as a:
                #    a.write(api_id + "," + api_hash)
        
        for line in data:
         if data.line_num!=sessionc:
             continue
         else: 
            if data.line_num>82:  
                #sys.exit()
                break
              
            print(gr +str(data.line_num)+" "+line[0])  
            api_id=line[0]
            api_hash=line[1]
            if sessionc%10==9:
               sessionc+=1
               print(sessionc)
            client = TelegramClient('anon'+str(sessionc), api_id, api_hash)     
            
               #continue
            sessionc+=1
            phone_numbers=[]
            with open('phone_numbers.csv',encoding='UTF-8') as r:
                data= csv.reader(r,delimiter=",",lineterminator="\n")
                for line in data:
                    phone_numbers.append(line[0])
            assert client.connect()
            for number in phone_numbers:
            # add user to contact
                contact = InputPhoneContact(client_id=0, phone=number, first_name=str(number), last_name="")
                result = client.invoke(ImportContactsRequest([contact]))
                # ---------------------------------------
                # add contact to your group
                try:
                 client(AddChatUserRequest(user_id=result.users[0], fwd_limit=0, chat_id=group_id))
                except Exception as e: 
                    print(re+"Error:"+e)
                # ---------------------------------------

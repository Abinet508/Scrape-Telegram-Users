# ```Scrape-Telegram-Users```

## Telegram script to scrape users from Telegram groups

## Requirements
### ** Prerequisites

``
* Python 3.6+
* Telegram API Id and API hash
* Telethon
* QRCode
* python-decouple
``
### Additional Requirements
``
* Create two folders in the root folder named `Environments` and `Sessions`.
* In the `Environments` folder create a file named `.env`
* Inside `.env` create to variables:
- Password=put your password here if you enable two-step verification
- phone_number=put your phone number here.

> Note that phone_number and password are variables that needs to be placed inside the `.env` file separated by new line and they will be used when creating a new session.
 - place
``

### Installation

`

* pip install Telethon
* pip install python-decouple
* pip install qrcode

`

## Usage

``
* after finished setting up your environment 

- Run  SessionCreater.py this will create unlimited session for you and make sure not to duplicate same session. This will cause flooding issue.   
    - Create a different session and rename this session to `Scrapersession` and this session will be used to scrape telegram members. use telegram account that have a lot public and private groups. 
   
- Then run scraper.py. 
 - wait until all groups are scraped.
 - no need to run scraper.py again unless you join new groups 

- and finally run `myadd.py` and this will add all the scraped members to your group if you intend to add members to same group uncomment this line #if a.title=="Awash bank": and replace it with your own group title.   

``

> 
-----------------------------------------
-----------------------------------------
> Author: Abinet Tesfu.

-----------------------------------------
-----------------------------------------

> You can find me on [Telegram](https://t.me/Abinet_tes) or [Github](github.com/Abinet508).
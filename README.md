<h1 align="center">VJ Video Player</h1>
<p align="center">
  <a href="https://github.com/VJBots/VJ-Video-Player">
    <img src="https://i.ibb.co/Yz4y12n/photo-2025-06-16-10-05-31-7516486294654943252.jpg" alt="Cover Image" width="550">
  </a>
</p>  
  <p align="center">
   </strong></a>
    <br><b>
    <a href="https://github.com/VJBots/VJ-Video-Player/issues">Report a Bug</a>
    |
    <a href="https://github.com/VJBots/VJ-Video-Player/issues">Request Feature</a></b>
  </p>



### **🏚️ About :**

<p align="center">
    <a href="https://github.com/VJBots/VJ-Video-Player">
        <img src="https://i.ibb.co/ZJzJ9Hq/link-3x.png" height="100" width="100" alt="VJ Video Player Logo">
    </a>
</p>
<p align='center'>
  <b><i>This bot is as like terabox, mdisk, pdisk etc bot. This bot stream your file or video on website with the help of telegram bot and channel. User can create his account on this bot and can earn money by generating and sharing link. Bot uses telegram cloud (telegram channel) to store file or video. This bot came with site customisation and with quality option.</i></b>
</p>

### 🌐 See How Bot & Website Look Like

<b><details><summary>Tap On Me For Demo Bot</summary></b>

<img src="https://i.ibb.co/RT6Dkzx6/photo-2025-06-17-07-58-16-7516824579164078084.jpg" alt="Bot Demo">
<img src="https://i.ibb.co/3978cnqt/photo-2025-06-17-07-58-16-7516824720897998868.jpg" alt="Bot Demo">
<img src="https://i.ibb.co/N2w6Nktz/photo-2025-06-17-07-58-16-7516824759552704536.jpg" alt="Bot Demo">
<img src="https://i.ibb.co/21pFTrGy/photo-2025-06-17-07-58-17-7516824793912442904.jpg" alt="Bot Demo">
<img src="https://i.ibb.co/23MB89XG/photo-2025-06-17-07-58-17-7516824858336952336.jpg" alt="Bot Demo">
<img src="https://i.ibb.co/fYfvsZ48/photo-2025-06-17-07-58-17-7516824884106756120.jpg" alt="Bot Demo">
<img src="https://i.ibb.co/60zNbkp0/photo-2025-06-17-07-58-17-7516824909876559896.jpg" alt="Bot Demo">
</details>


### **🔧 How To Deploy :**

- <u><b><i>Either you could locally host, VPS, Koyeb, Render, Seenode, Heroku or Any where this repo support.</i></b></u>

### **👨‍💻 Click On This Drop-Down And Get More Details**

<br>
<details>
  <summary><b>Deploy on Heroku</b></summary>

- <b>Fork This Repo
- Click on Deploy Easily
- Press the below button to Fast deploy on Heroku</b>


   [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
- <b>Go to <a href="#mandatory-vars">variables tab</a> for more info on setting up environmental variables.</b></details>

<details><summary><b>Deploy To Koyeb</b></summary>
<br>
<b>The fastest way to deploy the application is to click the Deploy to Koyeb button below.</b>
<br>
<br>
<b>Go to https://uptimerobot.com/ and add a monitor to keep your bot alive.</b>
<br>
<br>

[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?type=git&repository=github.com/VJBots/VJ-Video-Player&branch=main&name=VJ-Video-Player)
</details>

<details><summary><b>Deploy To Render</b></summary>
<br>
<b>
Use these commands:
<br>
<br>
• Build Command: <code>pip3 install -U -r requirements.txt</code>
<br>
<br>
• Start Command: <code>python3 bot.py</code>
<br>
<br>
Go to https://uptimerobot.com/ and add a monitor to keep your bot alive.
<br>
<br>
Use these settings when adding a monitor:</b>
<br>
<br>
<img src="https://telegra.ph/file/a79a156e44f43c9833b50.jpg" alt="render template">
<br>
<br>
<b>Click on the below button to deploy directly to render ↓</b>
<br>
<br>
<a href="https://render.com/deploy?repo=https://github.com/VJBots/VJ-Video-Player/tree/main">
<img src="https://render.com/images/deploy-to-render-button.svg" alt="Deploy to Render">
</a>
</details>

<details><summary><b>Deploy To VPS</summary>


`git clone https://github.com/VJBots/VJ-Video-Player`

**Install Packages**

`pip3 install -U -r requirements.txt`

**Edit info.py with variables as given below then run bot**

`python3 bot.py`

</b>
</details>


<details>
  <summary><b>Deploy Locally</b></summary>
<br>

```sh
git clone https://github.com/VJBots/VJ-Video-Player
cd bot.py
python3 ./venv
. ./venv/bin/activate
pip install -r requirements.txt
python3 bot.py
```

- **To stop the whole bot,
 do** <kbd>CTRL</kbd>+<kbd>C</kbd>

- **If you want to run this bot 24/7 on the VPS, follow these steps.**
```sh
sudo apt install tmux -y
tmux
python3 bot.py
```
- **now you can close the VPS and the bot will run on it.**

  </details>

<details>
  <summary><b>Deploy Using Docker</b></summary>
<br>
  
**Clone the repository:**
  
```sh
git clone https://github.com/VJBots/VJ-Video-Player
cd bot.py
```
**Build own Docker image:**

```sh
docker build -t file-stream .
```

**Create ENV and Start Container:**

```sh
docker run -d --restart unless-stopped --name fsb \
-v /PATH/TO/.env:/app/.env \
-p 8000:8000 \
video-player
```
- **if you need to change the variables in .env file after your bot was already started, all you need to do is restart the container for the bot settings to get updated:**

```sh
docker restart fsb
```

  </details>

<details>
  <summary><b>Setting Up Things</b></summary>
<br>

**If you're on Heroku, just add these in the Environmental Variables
or if you're Locally hosting, create a file named `.env` in the root directory and add all the variables there.
An example of `.env` file:**

```sh
API_ID = 789456
API_HASH = ysx275f9638x896g43sfzx65
BOT_TOKEN = 12345678:your_bot_token
BACKUP_BOT_TOKEN = 12345678:your_backup_bot_token
LOG_CHANNEL = -100123456789
ADMIN = 2719199
MONGODB_URI = mongodb://admin:pass@192.168.27.1
STREAM_LINK = https://your_app_url.com/
LINK_URL = https://your_blogspot_page_link

# Optional
MULTI_TOKEN1 = 12345678:bot_token_multi_client_1
MULTI_TOKEN2 = 12345678:bot_token_multi_client_2
PORT = 8080
```
</details>


<details>
  <summary><b>Vars And Details</b></summary>

#### 📝 Mandatory Vars :

* `API_ID`: API ID of your Telegram account, can be obtained from [My Telegram](https://my.telegram.org). `int`
* `API_HASH`: API hash of your Telegram account, can be obtained from [My Telegram](https://my.telegram.org). `str`
* `ADMIN`: Your Telegram User ID, Send `/id` to [@missrose_bot](https://telegram.dog/MissRose_bot) to get Your Telegram User ID `int`
* `BOT_TOKEN`: Telegram API token of your bot, can be obtained from [@BotFather](https://t.me/BotFather). `str`
* `LOG_CHANNEL`: ID of the channel where bot will store file or video as work like telegram cloud `int`.
* `MONGODB_URI`: MongoDB URI for saving User Data and Files List created by user. Watch [Video Tutorial](https://youtu.be/DAHRmFdw99o) `str`
* `LINK_URL`: Blogspot Page Link Url For Permanent Link Feature. Watch [Video Tutorial](https://youtu.be/fIQK5wnyQsM) `str`
* `STREAM_LINK`: Your App Url Starting With https and end with / . `str`

#### 🗼 MultiClient Vars :
* `MULTI_TOKEN1`: Add your first bot token. `str`
* `MULTI_TOKEN2`: Add your second bot token. `str`
* `MULTI_TOKENn`: Add your n bot token. (where n is positive integer) `str`

- **You Can Add More Multi Token As Shown Above.**

#### 🪐 Optional Vars :

* `SLEEP_THRESHOLD`: Set global flood wait threshold, auto-retry requests under 60s. `int`
* `SESSION`: Name for the Database created on your MongoDB. Defaults to `TechVJBot`. `str`
* `PORT`: The port that you want your webapp to be listened to. Defaults to `8080`. `int`

</details>

<details>
  <summary><b>How To Use</b></summary>

<br>

:warning: **Before using the  bot, don't forget to add the bot to the `LOG_CHANNEL` as an Admin**
 
#### ‍☠️ Bot Commands :

```sh
/start      : To check the bot is alive or not.
/quality    : To genrate file or video with quality option.
/account    : To check video plays or link clicks and balance.
/update     : To Update Business Name and Telegram channel link
/withdraw   : To Withdraw the balance through upi, bank etc.
/notify     : To inform user that your payment sended successfully or cancelled the payment. [ADMIN]
```

</details>

### **🇮🇳 Series On YouTube**

- ***In Simple These Are Video Tutorial Of How To Create Video Player Website For Free.***

* **Episode 1 : https://youtu.be/fIQK5wnyQsM**
* **Episode 2 : https://youtu.be/SC4uKotZjHE**
* **Episode 3 : https://youtu.be/NkJaO4tionY**
* **Episode 4 : Coming Soon..**

### **❤️ Thanks To :**

- <b>[Tech VJ](https://youtube.com/@Tech_VJ) : Coded Every New Features.</b>




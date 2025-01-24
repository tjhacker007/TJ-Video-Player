import random
import requests
import humanize
import base64
from Script import script
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
from info import LOG_CHANNEL, LINK_URL, ADMIN
from plugins.database import get_visits, get_count, get_withdraw, record_withdraw, record_visit
from urllib.parse import quote_plus, urlencode
from TechVJ.util.file_properties import get_name, get_hash, get_media_file_size
from TechVJ.util.human_readable import humanbytes

async def encode(string):
    string_bytes = string.encode("ascii")
    base64_bytes = base64.urlsafe_b64encode(string_bytes)
    base64_string = (base64_bytes.decode("ascii")).strip("=")
    return base64_string

async def decode(base64_string):
    base64_string = base64_string.strip("=") # links generated before this commit will be having = sign, hence striping them to handle padding errors.
    base64_bytes = (base64_string + "=" * (-len(base64_string) % 4)).encode("ascii")
    string_bytes = base64.urlsafe_b64decode(base64_bytes) 
    string = string_bytes.decode("ascii")
    return string

@Client.on_message(filters.command("start") & filters.incoming)
async def start(client, message):
    rm = InlineKeyboardMarkup([[InlineKeyboardButton("✨ Update Channel", url="https://t.me/VJ_Disk")]])
    await client.send_message(
        chat_id=message.from_user.id,
        text=script.START_TXT.format(message.from_user.mention),
        reply_markup=rm,
        parse_mode=enums.ParseMode.HTML
    )
    return

@Client.on_message(filters.private & (filters.document | filters.video))
async def stream_start(client, message):
    file = getattr(message, message.media.value)
    fileid = file.file_id
    user_id = message.from_user.id
    log_msg = await client.send_cached_media(chat_id=LOG_CHANNEL, file_id=fileid)
    params = {'u': user_id, 'w': str(log_msg.id)}
    url1 = f"{urlencode(params)}"
    link = await encode(url1)
    encoded_url = f"{LINK_URL}?Tech_VJ={link}"
    rm=InlineKeyboardMarkup([[InlineKeyboardButton("🖇️ Open Link", url=encoded_url)]])
    await message.reply_text(text=f"<code>{encoded_url}</code>", reply_markup=rm)

@Client.on_message(filters.private & filters.text & ~filters.command(["account", "withdraw", "notify"]))
async def link_start(client, message):
    if not message.text.startswith(LINK_URL):
        return
    link_part = message.text[len(LINK_URL + "?Tech_VJ="):].strip()
    try:
        original = await decode(link_part)
    except:
        return await message.reply("**Link Invalid**")
    try:
        u, user_id, id = original.split("=")
    except:
        return await message.reply("**Link Invalid**")
    user_id = user_id.replace("&w", "")
    if user_id == message.from_user.id:
        rm=InlineKeyboardMarkup([[InlineKeyboardButton("🖇️ Open Link", url=message.text)]])
        return await message.reply_text(text=f"<code>{message.text}</code>", reply_markup=rm)
    params = {'u': message.from_user.id, 'w': str(id)}
    url1 = f"{urlencode(params)}"
    link = await encode(url1)
    encoded_url = f"{LINK_URL}?Tech_VJ={link}"
    rm=InlineKeyboardMarkup([[InlineKeyboardButton("🖇️ Open Link", url=encoded_url)]])
    await message.reply_text(text=f"<code>{encoded_url}</code>", reply_markup=rm)

@Client.on_message(filters.private & filters.command("account"))
async def show_account(client, message):
    link_clicks = get_count(message.from_user.id)
    if link_clicks:
        # Calculate balance using the reduced link clicks
        balance = link_clicks / 5000.0  # Use floating-point division
        formatted_balance = f"{balance:.2f}"  # Format to 2 decimal places
        response = f"<b>Your Api Key :- <code>{message.from_user.id}</code>\n\nVideo Plays :- {reduced_link_clicks} ( Delay To Show Data )\n\nBalance :- ${formatted_balance}</b>"
    else:
        response = f"<b>Your Api Key :- <code>{message.from_user.id}</code>\nVideo Plays :- 0 ( Delay To Show Data )\nBalance :- $0</b>" 
    await message.reply(response)

@Client.on_message(filters.private & filters.command("withdraw"))
async def show_withdraw(client, message):
    w = get_withdraw(message.from_user.id)
    if w == True:
        return await message.reply("One Withdrawal Is In Process Wait For Complete It")
    link_clicks = get_count(message.from_user.id)
    if not link_clicks:
        return await message.reply("**You Are Not Eligible For Withdrawal.\nMinimum Withdrawal Amount Is $1 Means 5000 Link Clicks.**")
    if link_clicks >= 5000:
        confirm = await client.ask(message.from_user.id, "You Are Going To Withdraw All Your Link Clicks. Are You Sure You Want To Withdraw ?\nSend /yes or /no")
        if confirm.text == "/no":
            return await message.reply("**Withdraw Cancelled By You ❌**")
        else:
            pay = await client.ask(message.from_user.id, "Now Choose Your Payment Method, Click On In Which You Want Your Withdrawal.\n\n/upi - for upi, webmoney, airtm, capitalist\n\n/bank - for bank only")
            if pay.text == "/upi":
                upi = await client.ask(message.from_user.id, "Now Send Me Your Upi Or Upi Number With Your Name, Make Sure Name Matches With Your Upi Account")
                if not upi.text:
                    return await message.reply("**Wrong Input ❌**")
                upi = f"Upi - {pay.text}"
                upi.delete()
            else:
                name = await client.ask(message.from_user.id, "Now Send Me Your Account Holder Full Name")
                if not name.text:
                    return await message.reply("**Wrong Input ❌**")
                number = await client.ask(message.from_user.id, "Now Send Me Your Account Number")
                if not int(number.text):
                    return await message.reply("**Wrong Input ❌**")
                ifsc = await client.ask(message.from_user.id, "Now Send Me Your IFSC Code.")
                if not ifsc.text:
                    return await message.reply("**Wrong Input ❌**")
                bank_name = await client.ask(message.from_user.id, "Now Send You Can Send Necessary Thing In One Message, Like Send Bank Name, Or Contact Details.")
                if not bank_name.text:
                    return await message.reply("**Wrong Input ❌**")
                upi = f"Account Holder Name - {name.text}/n/nAccount Number - {number.text}/n/nIFSC Code - {ifsc.text}/n/nBank Name - {bank_name.text}\n\n"
                name.delete()
                number.delete()
                ifsc.delete()
                bank_name.delete()
            traffic = await client.ask(message.from_user.id, "Now Send Me Your Traffic Source Link, If Your Link Click Are Fake Then You Will Not Receive Payment And Withdrawal Get Cancelled")
            if not traffic.text:
                return await message.reply("**Wrong Traffic Source ❌**")
            balance = link_clicks / 5000.0  # Use floating-point division
            formatted_balance = f"{balance:.2f}"  # Format to 2 decimal places
            text = f"Api Key - {message.from_user.id}\n\n"
            text += f"Video Plays - {link_clicks}\n\n"
            text += f"Balance - ${formatted_balance}/n/n"
            text += upi
            text += f"Traffic Link - {traffic.text}"
            await client.send_message(ADMIN, text)
            record_withdraw(message.from_user.id, True)
            await message.reply(f"Your Withdrawal Balance - ${formatted_balance}/n/nNow Your Withdrawal Send To Owner, If Everything Fullfill The Criteria Then You Will Get Your Payment Within 3 Working Days.")
    else:
        await message.reply("Your Video Plays Smaller Than 10000 Plays, Minimum Payout Is 10000 Video Plays.")
        
@Client.on_message(filters.private & filters.command("notify") & filters.chat(ADMIN))
async def show_notify(client, message):
    count = int(1)
    user_id = await client.ask(message.from_user.id, "Now Send Me Api Key Of User")
    if int(user_id.text):
        sub = await client.ask(message.from_user.id, "Payment Is Cancelled Or Send Successfully. /send or /cancel")
        if sub.text == "/send":
            record_visits(user_id.text, count)
            record_withdraw(user_id.text, False)
            await client.send_message(user_id.text, "Your Withdrawal Is Successfully Completed And Sended To Your Bank Account.")
        else:
            reason = await client.ask(message.from_user.id, "Send Me The Reason For Cancellation Of Payment")
            if reason.text:
                record_visits(user_id.text, count)
                record_withdraw(user_id.text, False)
                await client.send_message(user_id.text, f"Your Payment Cancelled - {reason.text}")
    await message.reply("Successfully Message Send.")
    

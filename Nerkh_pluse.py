import requests
from datetime import date
import csv
import pymysql
from telegram import Bot
import asyncio
import os



url = "https://BrsApi.ir/Api/Market/Gold_Currency.php" # got to (https://brsapi.ir/category/api-financial/)for get API
params = {
    "key": "???"    #Enter your API key
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}


try:
    response = requests.get(url, params=params, headers=headers)
    result=response.json()
except:
    print('ERROR:Not connecting to API')
    exit()


for item in result['currency']:
    if item['symbol']=='USD':
        dollar_symbol='USD'
        dollar_price=item['price']
        dollar_change_value=item['change_value']
        dollar_change_percent=item['change_percent']
    if item['symbol']=='AED':
        derham_symbol='AED'
        derham_price=item['price']
        derham_change_value=item['change_value']
        derham_change_percent=item['change_percent']
    if item['symbol']=='EUR':
        euro_symbol='EUR'
        euro_price=item['price']
        euro_change_value=item['change_value']
        euro_change_percent=item['change_percent']
    if item['symbol']=='GBP':
        pound_symbol='GBP'
        pound_price=item['price']
        pound_change_value=item['change_value']
        pound_change_percent=item['change_percent']
    if item['symbol']=='CAD':
        dollar_canada_symbol='CAD'
        dollar_canada_price=item['price']
        dollar_canada_change_value=item['change_value']
        dollar_canada_change_percent=item['change_percent']
    if item['symbol']=='TRY':
        turkish_symbol='TRY'
        turkish_price=item['price']
        turkish_change_value=item['change_value']
        turkish_change_percent=item['change_percent']
    if item['symbol']=='KWD':
        dinar_symbol='KWD'
        dinar_price=item['price']
        dinar_change_value=item['change_value']
        dinar_change_percent=item['change_percent']
    if item['symbol']=='OMR':
        riyal_symbol='OMR'
        riyal_price=item['price']
        riyal_change_value=item['change_value']
        riyal_change_percent=item['change_percent']

    



for gold in result['gold']:
    if gold['symbol']=='IR_GOLD_18K':
        tala_18_symbol='IR_GOLD_18K'
        tala_18=gold['price']
        tala_18_change_value=gold['change_value']
        tala_18_change_percent=gold['change_percent']
    if gold['symbol']=='IR_GOLD_24K':
        tala_24_symbol='IR_GOLD_24K'
        tala_24=gold['price']
        tala_24_change_value=gold['change_value']
        tala_24_change_percent=gold['change_percent']
    if gold['symbol']=='IR_COIN_BAHAR':
        seke_baharazadi_symbol='IR_COIN_BAHAR'
        seke_baharazadi=gold['price']
        seke_baharazadi_change_value=gold['change_value']
        seke_baharazadi_change_percent=gold['change_percent']
    if gold['symbol']=='IR_COIN_EMAMI':
        seke_emami_symbol='IR_COIN_EMAMI'
        seke_emami=gold['price']
        seke_emami_change_value=gold['change_value']
        seke_emami_change_percent=gold['change_percent']
    if gold['symbol']=='IR_COIN_HALF':
        seke_nim_symbol='IR_COIN_HALF'
        seke_nim=gold['price']
        seke_nim_change_value=gold['change_value']
        seke_nim_change_percent=gold['change_percent']
    if gold['symbol']=='IR_COIN_QUARTER':
        seke_rob_symbol='IR_COIN_QUARTER'
        seke_rob=gold['price']
        seke_rob_change_value=gold['change_value']
        seke_rob_change_percent=gold['change_percent']



for crypto in result['cryptocurrency']:
    if crypto['symbol']=='BTC':
        bitcoin_symbol='BTC'
        bitcoin=crypto['price']
        bitcoin_change_percent=crypto['change_percent']
        bitcoin_market_cap=crypto['market_cap']
    if crypto['symbol']=='ETH':
        etherium_symbol='ETH'
        etherium=crypto['price']
        etherium_change_percent=crypto['change_percent']
        etherium_market_cap=crypto['market_cap']
    if crypto['symbol']=='USDT':
        tetherium_symbol='USDT'
        tetherium=crypto['price']
        tetherium_change_percent=crypto['change_percent']
        tetherium_market_cap=crypto['market_cap']

filename='price.csv'
file_exists=os.path.isfile(filename)
try:
    with open(filename,'a',newline='')as file:      #saving data as CSV
        writer=csv.writer(file)
        if not file_exists:
            writer.writerow(['symbol','price','change_value','change_percent','market_cap','date'])
        date_str=date.today()
        writer.writerow([dollar_symbol,dollar_price,dollar_change_value,dollar_change_percent,'',date_str])
        writer.writerow([derham_symbol,derham_price,derham_change_value,derham_change_percent,'',date_str])
        writer.writerow([euro_symbol,euro_price,euro_change_value,euro_change_percent,'',date_str])
        writer.writerow([pound_symbol,pound_price,pound_change_value,pound_change_percent,'',date_str])
        writer.writerow([dollar_canada_symbol,dollar_canada_price,dollar_canada_change_value,dollar_canada_change_percent,'',date_str])
        writer.writerow([turkish_symbol,turkish_price,turkish_change_value,turkish_change_percent,'',date_str])
        writer.writerow([dinar_symbol,dinar_price,dinar_change_value,dinar_change_percent,'',date_str])
        writer.writerow([riyal_symbol,riyal_price,riyal_change_value,riyal_change_percent,'',date_str])

        writer.writerow([tala_18_symbol,tala_18,tala_18_change_value,tala_18_change_percent,'',date_str])
        writer.writerow([tala_24_symbol,tala_24,tala_24_change_value,tala_24_change_percent,'',date_str])
        writer.writerow([seke_baharazadi_symbol,seke_baharazadi,seke_baharazadi_change_value,seke_baharazadi_change_percent,'',date_str])
        writer.writerow([seke_emami_symbol,seke_emami,seke_emami_change_value,seke_emami_change_percent,'',date_str])
        writer.writerow([seke_nim_symbol,seke_nim,seke_nim_change_value,seke_nim_change_percent,'',date_str])
        writer.writerow([seke_rob_symbol,seke_rob,seke_rob_change_value,seke_rob_change_percent,'',date_str])

        writer.writerow([bitcoin_symbol,bitcoin,'',bitcoin_change_percent,bitcoin_market_cap,date_str])
        writer.writerow([etherium_symbol,etherium,'',etherium_change_percent,etherium_market_cap,date_str])
        writer.writerow([tetherium_symbol,tetherium,'',tetherium_change_percent,tetherium_market_cap,date_str])
except:
    print('ERROR:Faled to save CSV file')




data_rows=[(dollar_symbol,dollar_price,dollar_change_value,dollar_change_percent,None,date_str),
           (derham_symbol,derham_price,derham_change_value,derham_change_percent,None,date_str),
           (euro_symbol,euro_price,euro_change_value,euro_change_percent,None,date_str),
           (pound_symbol,pound_price,pound_change_value,pound_change_percent,None,date_str),
           (dollar_canada_symbol,dollar_canada_price,dollar_canada_change_value,dollar_canada_change_percent,None,date_str),
           (turkish_symbol,turkish_price,turkish_change_value,turkish_change_percent,None,date_str),
           (dinar_symbol,dinar_price,dinar_change_value,dinar_change_percent,None,date_str),
           (riyal_symbol,riyal_price,riyal_change_value,riyal_change_percent,None,date_str),
           (tala_18_symbol,tala_18,tala_18_change_value,tala_18_change_percent,None,date_str),
           (tala_24_symbol,tala_24,tala_24_change_value,tala_24_change_percent,None,date_str),
           (seke_baharazadi_symbol,seke_baharazadi,seke_baharazadi_change_value,seke_baharazadi_change_percent,None,date_str),
           (seke_emami_symbol,seke_emami,seke_emami_change_value,seke_emami_change_percent,None,date_str),
           (seke_nim_symbol,seke_nim,seke_nim_change_value,seke_nim_change_percent,None,date_str),
           (seke_rob_symbol,seke_rob,seke_rob_change_value,seke_rob_change_percent,None,date_str),
           (bitcoin_symbol,bitcoin,None,bitcoin_change_percent,bitcoin_market_cap,date_str),
           (etherium_symbol,etherium,None,etherium_change_percent,etherium_market_cap,date_str),
           (tetherium_symbol,tetherium,None,tetherium_change_percent,tetherium_market_cap,date_str)]




try:
    # connect to MYSQL without specifying a database
    connection = pymysql.connect(    #insert database info 
        host='',
        user='',
        password='',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    
    with connection.cursor() as cursor:
        # create the database if it does not exist
        cursor.execute('CREATE DATABASE IF NOT EXISTS price')
        
        # choose database
        cursor.execute('USE price')
        
        # create table
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS valuehistory (
            id INT AUTO_INCREMENT PRIMARY KEY,
            symbol VARCHAR(20),
            price DOUBLE,
            change_value DOUBLE,
            change_percent DOUBLE,
            market_cap BIGINT,
            date DATE
        )'''
        cursor.execute(create_table_query)
        
        #insert table
        insert_query = '''
        INSERT INTO valuehistory 
        (symbol, price, change_value, change_percent, market_cap, date)
        VALUES (%s, %s, %s, %s, %s, %s)
        '''
        cursor.executemany(insert_query, data_rows)
    
    
    connection.commit()

except Exception as e:
    print(f'ERROR:failed to connect to the database {str(e)}')

connection.close()









#create message with emoji
emoji_map = {
    'USD': '🇺🇸',
    'EUR': '🇪🇺',
    'AED': '🇦🇪',
    'TRY': '🇹🇷',
    'CNY': '🇨🇳',
    'GBP': '🇬🇧',
    'Gold': '🏅',
    'Coin': '🪙',
    'BTC': '₿',
    'ETH': '⚙️',
    'USDT': '💵'
}

message = '📢 <b>گزارش نرخ امروز از ارزیار</b>\n\n'

for row in data_rows:
    symbol, price, change_val, change_pct, market_cap, date = row
    emoji = emoji_map.get(symbol, '💱')

    direction = '➖'
    if change_pct > 0:
        direction = '⬆️'
    elif change_pct < 0:
        direction = '⬇️'

    message += (
        f"{emoji} <b>{symbol}</b>\n"
        f"• قیمت: {price:} تومان\n"
        f"• تغییر: {change_val} تومان ({change_pct:+.2f}٪) {direction}\n"
        f"• مارکت کپ: {market_cap:} تومان\n"
        f"────────────\n"
    )

message += f"\n⏰ <i>تاریخ: {data_rows[0][-1]}</i>"

# ارسال پیام به تلگرام
TOKEN =''
CHANNEL_ID = '@Nerkh_pluse'

bot = Bot(token=TOKEN)

try:
    async def sender():
        await bot.send_message(chat_id=CHANNEL_ID, text=message, parse_mode='HTML')
    asyncio.run(sender())
except:
    print('ERROR: Failed send message to the telegram')
    exit()
    

    










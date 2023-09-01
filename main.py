from twilio.rest import Client
import requests
import datetime

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"




# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

account_sid = "AC76203074a459952d1245a88b821cddd4"
auth_token = "2eaff1cdf93ccd7f433b8be10dc6d9a0"
client = Client(account_sid, auth_token)

# message = client.messages \
#                 .create(
#                      body="Join Earth's mightiest heroes. Like Kevin Bacon.",
#                      from_='+15736335279',
#                      to='+48881248882'
#                  )
#
# print(message.status)



## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey==U0BBUEHQJ10L2UZA')
data = r.json()

td_1d = datetime.timedelta(days=1)
td_2d = datetime.timedelta(days=2)

yesterday_date = datetime.date.today() - td_1d
day_before_yesterday = datetime.date.today() - td_2d

yesterday_price = float(data['Time Series (Daily)'][f'{yesterday_date}']['4. close'])
day_before_yesterday_price = float(data['Time Series (Daily)'][f'{day_before_yesterday}']['4. close'])

if (abs(yesterday_price - day_before_yesterday_price) / day_before_yesterday_price) > 0.05:
    print("Get News")



## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

r2 = requests.get("https://newsapi.org/v2/everything?q=TESLA&apiKey=4b759fc89ab348cfb03445b071385923")
data2 = r2.json()
print(data2)

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""



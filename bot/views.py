from django.http import HttpResponse
from django.shortcuts import render
import os
from twilio.rest import Client
import environ
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import requests
import time
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

# <QueryDict: {'SmsMessageSid': ['SM4cc77334aff21573e5fdb72f7502f055'], 'NumMedia': ['0'], 'ProfileName': ['name'],
#  'SmsSid': ['SM4cc77334aff21573e5fdb72f7502f055'], 'WaId': ['*'], 'SmsStatus': ['received'], 'Body': ['hello'], 'To': ['whatsapp:+14155238886'], 'NumSegments': ['1'], 'ReferralNumMedia': ['0'], 'MessageSid': ['SM4cc77334aff21573e5fdb72f7502f055'], 'AccountSid': ['AC53aa8197de6f7767c509335a6de6588a'], 'From': ['whatsapp:+27*'], 'ApiVersion': ['2010-04-01']} >


@ csrf_exempt
def bot(request):
    if request.POST:
        body = request.POST["Body"]
        sender_name = request.POST["ProfileName"]
        sender_number = request.POST["WaId"]

        # Check if the input is a valid number
        if body.isnumeric():
            print("number")
            if int(body) == 1:
                client.messages.create(
                    body=f'Thanks for subscribing to whatsapp bible we will now send you a bible verse every day.',
                    from_='whatsapp:+14155238886',
                    to=f'whatsapp:+{sender_number}'
                )
            else:
                client.messages.create(
                    body=f'Sorry we have no option for {body}.',
                    from_='whatsapp:+14155238886',
                    to=f'whatsapp:+{sender_number}'
                )
                client.messages.create(
                    body=f'These are the available commands:\n1. Type "1" to subscribe to daily verses.\n2. To read a passage from the bible type the book followed by the scripture, example "Genesis 1:1".\n4. To read a chapter from the bible type the book followed by the chapter, example "Genesis 1".',
                    from_='whatsapp:+14155238886',
                    to=f'whatsapp:+{sender_number}'
                )
        elif not body.isnumeric():
            input = body.lower()
            if input:
                url = f"https://bible-api.com/{input}"
                r = requests.get(url)
                if r.status_code == 200:
                    try:
                        r_json = r.json()
                        client.messages.create(
                            body=r_json["text"],
                            from_='whatsapp:+14155238886',
                            to=f'whatsapp:+{sender_number}'
                        )
                    except Exception as e:
                        print(f'json_data:Error {e}')
                        print(r_json["verses"])
                        verses = r_json["verses"]
                        for verse in verses:
                            client.messages.create(
                                body=f"{verse['verse']}\n{verse['text']}",
                                from_='whatsapp:+14155238886',
                                to=f'whatsapp:+{sender_number}'
                            )
                            time.sleep(3)
                        pass
                else:
                    client.messages.create(
                        body=f'Good day {sender_name}, how can I help you today?',
                        from_='whatsapp:+14155238886',
                        to=f'whatsapp:+{sender_number}'
                    )
                    client.messages.create(
                        body=f'You have reached whatsapp.bible.\nThese are the available commands:\n1. Type "1" to subscribe to daily verses.\n2. To read a passage from the bible type the book followed by the scripture, example "Genesis 1:1".\n4. To read a chapter from the bible type the book followed by the chapter, example "Genesis 1".',
                        from_='whatsapp:+14155238886',
                        to=f'whatsapp:+{sender_number}'
                    )

    # print(r_json)
    return render(request, "bot.html")

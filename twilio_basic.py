#!/usr/bin/env python

from twilio.rest import Client

account_sid = 'ACfbe16d006d5d66d42053f83576c5f621'

auth_token = '6710b3da3488302beb31905455dd2fc3'

client = Client(account_sid, auth_token)

message = client.messages.create(body='lil bitty testerooni n cheese', from_='+19036366042', to='+17632108728')

print(message.sid)

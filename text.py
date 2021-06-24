import os
from twilio.rest import Client
account_sid= os.environ["ACddf1c462ef84471716130fc9678fea66"]
auth_token= os.environ["eb630ddde0266603c3597eef1a58b0f0"]
client=Client(account_sid, auth_token)
client.messages.create(from_="8919170648",body="Hello World",to="7093284871")

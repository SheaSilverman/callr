# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import TwilioRestClient
import config

client = TwilioRestClient(config.account_sid, config.auth_token)
to = "+15555555555"

call = client.calls.create(url="http://example.com/call/say.xml", to=to, from_=config.from_num )
print(call.sid)

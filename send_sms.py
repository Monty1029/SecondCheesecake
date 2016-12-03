from twilio.rest import TwilioRestClient

account_sid = ""
auth_token = ""

client = TwilioRestClient(account_sid, auth_token)

try:
	message = client.messages.create(body="CHESSECAKE",
		to="+",
		from_="+13437004377")

print(message.sid)
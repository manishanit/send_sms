from twilio import rest

account_sid = "AC2cc429c2fab5a6b018e9cf1650eceb7f" # Your Account SID from www.twilio.com/console
auth_token  = "a6a3303812875f555902a55c1ab48607"  # Your Auth Token from www.twilio.com/console

client = rest.TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="My name is anita <3",
    to="+918609131604",    # Replace with your phone number
    from_="+12019772661") # Replace with your Twilio number

print message.sid

from twilio.rest import TwilioRestClient

account_sid = "ACcca8cea6f81d348e4495298141208ff1" # Your Account SID from www.twilio.com/console
auth_token  = "8f4e6a1058b027e2a32838d49e563565"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    body="Hello from Python!!!",
    to="+380636284815",    # Replace with your phone number
    from_="+12673231174") # Replace with your Twilio number

print(message.sid)

import requests

# Your Twilio account SID and auth token
account_sid = "AC442e3ce355352afa300428dbd6cbda4a"
auth_token = "f862489c1275df0b337ca7186bd93d59"

# Your SIP trunk SIP URI
sip_uri = "sip:SD9036a52fc4a584aae1402699df6e3c8d@sip.twilio.com"

# Your custom caller ID
caller_id = "+15555555555"

# Input the 'To' number
to_number = "+94785998242"

# Construct the SIP endpoint URI with the 'sip:' prefix
to_sip_uri = "sip:" + to_number + "@sip.twilio.com"

# The authentication credentials
auth = (account_sid, auth_token)

# The INVITE request data
invite_data = {
    "url": "https://handler.twilio.com/twiml/EHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "to": to_number,  # Use the 'To' parameter with the phone number directly
    "from": sip_uri,  # Use the 'From' parameter with your SIP URI
    "headers": {
        "From": caller_id,
        "Call-ID": "1234567890",
        "CSeq": 1,
        "Content-Type": "application/sdp",
    },
    "body": "v=0\no=SIP 2.0 1234567890 1234567890 IN IP4 192.168.1.100\ns=SIP Example\nc=IN IP4 192.168.1.100\nt=0 0\na=audio m=audio 8000 RTP/AVP 0 0\na=rtpmap:0 PCMA/8000\n",
}

# Send the INVITE request to the Twilio SIP endpoint
response = requests.post(
    f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls.json",
    data=invite_data,
    auth=auth,
)

# Check the status code of the response
if response.status_code == 201:
    print("Call initiated successfully!")
    print(response.json())
else:
    print("Error initiating call:", response.status_code)
    print(response.text)

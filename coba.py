import requests
import json
url0 = 'https://api.thebigbox.id/sms-otp/1.0.0/otp/32/' #PUT
url1 = 'https://api.thebigbox.id/sms-otp/1.0.0/otp/32/verifications' #POST
api_key = "3tqkUH1dNdQznlqCDO3hOWvvvddihjBZ"
header = {
  'Content-type':"application/json",
  'x-api-key':api_key,
  'Accept':'application/json'
}

body0 = {
  "maxAttempt": 2,
  "masking": {
    "accountId": "",
    "senderId": "",
    "password": ""
  },
  "phoneNum": "+6285248475103",
  "expireIn": 3600,
  "content": "Halo ini OTP mu: {{otp}}",
  "digit": 4,
  "callbackUrl": ""
}

body1 = {
  "maxAttempt": 2,
  "otpstr": "6000",
  "expireIn": 3600,
  "digit": 4
}

def makeOTP(key):
  url = 'https://api.thebigbox.id/sms-otp/1.0.0/otp/{key}'.format(key=key)
  return requests.put(url,headers=header,data=json.dumps(body0))

def verifyOTP(key,kode):
  url = 'https://api.thebigbox.id/sms-otp/1.0.0/otp/{key}/verifications'.format(key=key)
  bodyC = {
  "maxAttempt": 2,
  "otpstr": kode,
  "expireIn": 3600,
  "digit": 4
  }
  return requests.post(url,headers=header,data=json.dumps(bodyC))

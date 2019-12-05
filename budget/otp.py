import requests
import json
url0 = 'https://api.thebigbox.id/sms-otp/1.0.0/otp/32/' #PUT
url1 = 'https://api.thebigbox.id/sms-otp/1.0.0/otp/32/verifications' #POST
api_key = "PCutZcxCx9s3QT2sNKc87rS7toHkpL55"
phone = "+6285248475103"
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
  "phoneNum": phone,
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

def setPhone(phoneN):
  global phone
  phone = phoneN
def setApiKey(key):
  global api_key
  api_key = key

def makeOTP(key):
  url = 'https://api.thebigbox.id/sms-otp/1.0.0/otp/{key}'.format(key=key)
  header = { 'Content-type':"application/json", 'x-api-key':api_key, 'Accept':'application/json'}
  body = {
  "maxAttempt": 2,
  "masking": {
    "accountId": "",
    "senderId": "",
    "password": ""
  },
  "phoneNum": phone,
  "expireIn": 3600,
  "content": "Halo ini OTP mu: {{otp}}",
  "digit": 4,
  "callbackUrl": ""
  }
  return requests.put(url,headers=header,data=json.dumps(body))

def verifyOTP(key,kode):
  url = 'https://api.thebigbox.id/sms-otp/1.0.0/otp/{key}/verifications'.format(key=key)
  header = { 'Content-type':"application/json", 'x-api-key':api_key, 'Accept':'application/json'}
  bodyC = { "maxAttempt": 2, "otpstr": kode, "expireIn": 3600, "digit": 4 }
  return requests.post(url,headers=header,data=json.dumps(bodyC))

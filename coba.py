import request 
'https://api.thebigbox.id/sms-otp/1.0.0/otp/96/' PUT
'https://api.thebigbox.id/sms-otp/1.0.0/otp/96/verifications' POSt

{
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

{
  "maxAttempt": 2,
  "otpstr": "6000",
  "expireIn": 3600,
  "digit": 4
}
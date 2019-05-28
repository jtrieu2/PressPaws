import os
import requests
import json 

api_url = 'https://api.sendgrid.com/v3/mail/send'



headers = {
    'content-type': 'application/json',
    'Authorization': 'Bearer ' + os.environ.get('SENDGRID_API_KEY')
}

payload = {

  "personalizations": [
    {
      "to": [
        {
          "email": "jennytrieu10@gmail.com"
        }
      ],
      "subject": "Hello, World!"
    }
  ],
  "from": {
    "email": "jennytrieu10@gmail.com"
  },
  "content": [
    {
      "type": "text/plain",
      "value": "Hello, World!"
    }
  ]
}

r = requests.post(api_url, data=json.dumps(payload), headers=headers)

if (r):
    print(r)
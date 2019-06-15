import os
import json
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_email(recipient_email, event_info):
    message = Mail(
        from_email='jennytrieu10@gmail.com',
        to_emails=recipient_email,
        html_content='<strong>and easy to do anywhere, even with Python</strong>')
    message.dynamic_template_data = {
        'event': event_info['event_name'],
        'date': event_info['event_date'],
        'link': event_info['eventbrite_url'],
        'url': event_info['event_image'],
        'description': event_info['event_description']
    }
    message.template_id = 'd-186eae7726114998b18333322ed1b1fe'
    try:
        sendgrid_client = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sendgrid_client.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)
import resend
from django.conf import settings

resend.api_key = settings.RESEND_API_KEY


def safe_send_mail(subject, message, recipient_list):
    try:
        for recipient in recipient_list:
            response = resend.Emails.send({
                "from": "BB CARE <onboarding@resend.dev>",
                "to": recipient,
                "subject": subject,
                "text": message,
            })

            print("EMAIL SENT:", response)

        return True

    except Exception as e:
        print("EMAIL FAILED:", e)
        return False
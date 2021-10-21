

import time
import random
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

from UserApi.models import User, UserVerification

configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = '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'

api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
    sib_api_v3_sdk.ApiClient(configuration))
subject = "Email Verification"


def send_otp(email):

    if(User.objects.filter(email=email).exists()):
        return(False, "Email Already Exists!")
    otp = str(random.randint(1111, 9999))
    text = "Your OTP for Email Verification is : " + otp

    sender = {"name": "ProjectX", "email": "randomdude@gmail.com"}
    to = [{"email": email, "name": "User"}]

    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        to=to,   sender=sender, subject=subject, text_content=text)

    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        UserVerification(email=email, otp=otp).save()
        return (True, "Email Has been Sent")
    # pprint(api_response)
    except ApiException as e:
        # ("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
        return(False, "Some Error Occurred")

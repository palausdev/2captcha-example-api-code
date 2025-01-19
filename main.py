import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from twocaptcha import TwoCaptcha

api_key = os.getenv('APIKEY_2CAPTCHA', 'YOUR_APIKEY')

solver = TwoCaptcha(api_key)

try:
    result = solver.recaptcha(
        sitekey='6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-',
        url='https://www.google.com/recaptcha/api2/demo') 

except Exception as e:
    sys.exit(e)

else:
    sys.exit('solved: ' + str(result))
import pyqrcode
import png
import pyotp
import sys
from pyqrcode import QRCode

#if python otp.py generate-qr
if str(sys.argv[1]) == 'generate-qr':

    #creates random secret key
    #key = pyotp.random_base32()
    key = 'JBSWY3DPEHPK3PXP'

    #assume user id as 'alice@google.com' and issuer is 'Secure App'. Generate uri
    uri = pyotp.totp.TOTP(key).provisioning_uri(name='alice@google.com', issuer_name='Secure App')

    #generate qr code based off uri
    url = pyqrcode.create(uri)

    # Create and save the png file naming "myqr.png"
    url.png('myqr.png',scale=6)

#if python otp.py get-otp
if str(sys.argv[1]) == 'generate-otp':

    #Generate otp
    #totp = = pyotp.TOTP(key)
    totp = = pyotp.TOTP('JBSWY3DPEHPK3PXP')

    #print to screen the current totp
    print("Current OTP:",totp.now())

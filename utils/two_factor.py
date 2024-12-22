
import pyotp
import qrcode
from io import BytesIO
from base64 import b64encode

class TwoFactorAuth:
    @staticmethod
    def setup_2fa(user):
        secret = pyotp.random_base32()
        user.two_factor_secret = secret
        db.session.commit()
        return TwoFactorAuth.generate_qr(user.email, secret)
        
    @staticmethod
    def verify(user, code):
        if not user.two_factor_secret:
            return False
        totp = pyotp.TOTP(user.two_factor_secret)
        return totp.verify(code)

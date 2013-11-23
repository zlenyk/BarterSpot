SITE_ADDRESS = "localhost"
EMAIL_SUFIX = "barterspot.com"
SMTP_ADDR = 'localhost'


####################
###  VALIDATION  ###
####################

VALIDATION_PREFIX = "noreply"
VALIDATION_EMAIL = VALIDATION_PREFIX + "@" + EMAIL_SUFIX
VALIDATION_ADDRESS_SUFIX = "/users/validate/"
VALIDATION_CODE_LEN = 20
VALIDATION_SUBJECT = "Welcome to BarterSpot!"
VALIDATION_TEXT = """Hello %(username)s!
  In order to help maintain the security of your BarterSpot account,
please verify your email address by clicking the following link:
""" +\
    SITE_ADDRESS + VALIDATION_ADDRESS_SUFIX + \
    """%(hash)s

If you haven't registered for BarterSpot please just ignore this message.

Best regards,
BarterSpot team"""

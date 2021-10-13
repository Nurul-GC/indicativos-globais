from secrets import token_hex


class Config:
    """project's configuration"""
    SECRET_KEY = token_hex(32)
    DEBUG = False

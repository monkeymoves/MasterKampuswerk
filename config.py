class Config(object):
    """
    Common configurations
    """

    # Put any configurations here that are common across all environments

    # SQLALCHEMY_POOL_RECYCLE = 499
    # SQLALCHEMY_POOL_TIMEOUT = 20

class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}


# app.config['OAUTH_CREDENTIALS'= {
#     'facebook': {
#         'id': '837483683053553',
#         'secret': 'bce2321650fbb754b955453e1d10b2f0'
#     },
#     'google': {
#         'id': '838769494183-f2e9i6s0ng8eps3075bfsmlgoo3e7hvk.apps.googleusercontent.com',
#         'secret': '51V_GgfoNr52oB0X9vhVXd3E'
#     },
#     'twitter': {
#         'id': 'dDu5qMg32Rsh94P89UCcQoLJO',
#         'secret': 'EB6LF33hBYjhKsiPqxofG1NN8PFSQ1i007zjdIvDekgCnkbkp7'
#     }
# }
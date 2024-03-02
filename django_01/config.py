"""
# config.py文件相关参数配置
# 文件路径/diango_01/config.py
"""

# 数据库
MYSQL_NAME = 'django_web'
MYSQL_PASSWORD = '1823fengji'
MYSQL_HOST = '10.0.16.2'
MYSQL_PORT = '3306'
MYSQL_USER = 'root'
# 10.0.16.2
# redis
BROKER_URL = 'redis://10.0.16.2:6379/0'
CELERY_RESULT_BACKEND = 'redis://10.0.16.2:6379/0'

# 阿里云短信服务
ALI_ACCESS_KEY_ID = ""
ALI_ACCESS_KEY_SECRET = ""
ALI_SIGN_NAME = ""
ALI_TEMPLATE_CODE = ""

# 七牛云存储
QINIU_ACCESS_KEY = 'FzUhTzQpaRIbFB-lLdMiR2LAO0D3MGln60SvcOCN'
QINIU_SECRET_KEY = 'PoxDRGNbY0IsNP02go8CuGnuvJT0f3w4n6ZlMkn0'
QINIU_BUCKET_NAME = 'sjhfengji'
QINIU_DOMAIN = 'qiniu.hebeu-xyh.cn'

# 百度云点播
BAIDU_CLOUD_USER_ID = ""
BAIDU_CLOUD_USER_KEY = ''

# 支付pypay
PAY_TOKEN = ''
PAY_UID = ''
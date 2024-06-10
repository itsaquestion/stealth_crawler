import logging
import sys

bind = '127.0.0.1:8000'
workers = 1
backlog = 2048
worker_class = 'uvicorn.workers.UvicornWorker'
worker_connections = 1000
timeout = 60
keepalive = 2
errorlog = 'error.log'
accesslog = 'access.log'
loglevel = 'info'
pidfile = 'gunicorn.pid'
daemon = True

# 日志格式
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# 捕获stdout和stderr
capture_output = True

# 将控制台打印重定向到错误日志
def pre_exec(server):
    logger = logging.getLogger(__name__)
    logger.setLevel(loglevel.upper())
    formatter = logging.Formatter(access_log_format)

    # 将控制台打印重定向到错误日志
    sys.stdout = open(errorlog, 'a')
    sys.stderr = sys.stdout

    # 设置日志处理器
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
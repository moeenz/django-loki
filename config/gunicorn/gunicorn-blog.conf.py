import os


# [ Logging ]
logconfig = os.getenv(
    'GC_LOGCONFIG', '/usr/web/confs/gunicorn/gunicorn-logging.conf')
accesslog = os.getenv('GC_ACCESSLOG', '-')
errorlog = os.getenv('GC_ERRORLOG', '-')
statsd_host = os.getenv('GC_STATSD_HOST', None)
statsd_prefix = os.getenv('GC_STATSD_PREFIX', None)


# [ Server Socket ]
bind = ['%s:%s' % (os.getenv('GC_HOST', '0.0.0.0'),
                   os.getenv('GC_PORT', '8000'))]


# [ Worker Processes ]
workers = os.getenv('GC_WORKERS')
timeout = os.getenv('GC_TIMEOUT', 120)

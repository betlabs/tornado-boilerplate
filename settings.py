import os.path
from tornado.options import define


def path(root, *a): return os.path.join(root, *a)


ROOT = os.path.dirname(os.path.abspath(__file__))

define('port', default=8000, help='run on the given port', type=int)
# define('config', default=None, help='tornado config file')
# define('debug', default=False, help='debug mode')

STATIC_ROOT = path(ROOT, 'static')
TEMPLATE_ROOT = path(ROOT, 'templates')

settings = {"debug": True,
            "cookie_secret": "cookie_secret",
            "login_url": "/login",
            "static_path": STATIC_ROOT,
            "template_path": TEMPLATE_ROOT,
            "xsrf_cookies": False}

import tornado.httpserver
import tornado.ioloop
from tornado.options import options
import tornado.web
import tornado.autoreload

from settings import settings
from urls import url_patterns


class TornadoApplication(tornado.web.Application):
    # def start_request(self, server_conn, request_conn):
    #     pass

    def __init__(self):
        tornado.web.Application.__init__(self, url_patterns, **settings)


def main():
    app = TornadoApplication()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()

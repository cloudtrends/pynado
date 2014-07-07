import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
    	url_str = "<a href=\"http://www.tornadoweb.org/en/stable/#hello-world\">click me</a>"
        self.write("Hello, world from " + url_str)

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


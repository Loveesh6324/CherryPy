import cherrypy
import unittest
import threading,urllib

class HelloWorld:

    def index(self):
        return "Hello, world!"
    index.exposed = True

def start_server():
    cherrypy.tree.mount(HelloWorld())
    cherrypy.engine.start()
    cherrypy.engine.block()

def stop_server():
    cherrypy.engine.exit()

class TestHelloWorld(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.server_thread = threading.Thread(target=start_server)
        cls.server_thread.start()

    @classmethod
    def tearDownClass(cls):
        stop_server()
        cls.server_thread.join()

    def test_hello_world(self):
        response = urllib.request.urlopen('http://localhost:8080')
        html = response.read().decode('utf-8')
        self.assertEqual(html, 'Hello, world!')

if __name__ == '__main__':
    unittest.main()

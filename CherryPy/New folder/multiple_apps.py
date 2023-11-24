import cherrypy

class Hello(object):
	@cherrypy.expose
	def index(self):
		return 'Welcome to the multi app demo!'

class World(object):
	@cherrypy.expose
	def index(self):
		return 'Welcome to my World!'


class HelloWorld(object):
	@cherrypy.expose
	def index(self):
		return 'Welcome to HelloWorld!'

class Calculator(object):
	@cherrypy.expose
	def index(self):
		return 'Welcome to the calculator app!'

	@cherrypy.expose
	def sum(self, a, b):
		return 'a + b = {}'.format(int(a) + int(b))



if __name__ == '__main__':
	cherrypy.tree.mount(Hello(),'/')
	cherrypy.tree.mount(World(),'/world')
	cherrypy.tree.mount(HelloWorld(),'/helloworld')
	cherrypy.tree.mount(Calculator(),'/calculator')
	cherrypy.engine.start()
	cherrypy.engine.block()
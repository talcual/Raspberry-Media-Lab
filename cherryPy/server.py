import cherrypy
import glob
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))
from os import listdir
from os.path import isfile, join

onlyfiles = [x.decode('utf-8') for x in listdir("../serx/crossflux") if x.endswith(".mp3")]


class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "Hello World!"

    @cherrypy.expose
    def files(self):
	tmpl = env.get_template('index.html')
        return tmpl.render(navigation=onlyfiles)


cherrypy.config.update({'server.socket_host': 'ip',
                        'server.socket_port': port,
                       })

cherrypy.quickstart(HelloWorld())

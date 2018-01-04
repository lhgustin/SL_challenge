from bottle import route, run, post, get, static_file, request
from SLDao import SLDao
import SLModels

VERSION = 0.1
slDao = SLDao()


@route('/hello')
def hello():
        return "Hello World! V" + str(VERSION)


# I. STATIC SERVING
@get('/')
def home():
        return static_file('index.html', root='../app')


@route('/js/:path#.+#')
def server_static(path):
        print 'static!', path
        return static_file(path, root='../app/static/js')


@route('/css/:path#.+#')
def server_static(path):
        print 'static!', path
        return static_file(path, root='../app/static/css')


@route('/images/:path#.+#')
def server_static(path):
        print 'static!', path
        return static_file(path, root='../app/static/images')


@route('/app/core/:path#.+#')
def server_static(path):
        print 'static!', path
        return static_file(path, root='../app/core')


@route('/app/agency-creator/:path#.+#')
def server_static(path):
        print 'static!', path
        return static_file(path, root='../app/agency-creator')


@route('/app/agency-list/:path#.+#')
def server_static(path):
        print 'static!', path
        return static_file(path, root='../app/agency-list')


@route('/partials/:path#.+#')
def server_static(path):
        print 'static!', path
        return static_file(path, root='../app/partials')


# II. API
@get('/agencies')
def get_agencies():
        agencies = slDao.find_all_agencies()
        return SLModels.get_json_from_entity(agencies)


@post('/add_agency')
def add_agency():
        agency_json = request.json['agency']
        agency = slDao.add_agency(agency_json)
        return SLModels.get_json_from_entity(agency)


# run the app
run(host='localhost', port=8080)

from bottle import route, run, post, get, static_file, request
from SLDao import SLDao
import SLModels
import json

VERSION = 0.1
slDao = SLDao()


@route('/hello')
def hello():
        return "Hello World! V" + str(VERSION)


# I. STATIC SERVING
@get('/')
def home():
        return static_file('index.html', root='../app')


@route('/static/js/:path#.+#')
def server_static(path):
        print 'static!', path
        return static_file(path, root='../app/static/js')


@route('/static/css/:path#.+#')
def server_static(path):
        print 'static!', path
        return static_file(path, root='../app/static/css')


@route('/static/images/:path#.+#')
def server_static(path):
        print 'static!', path
        return static_file(path, root='../app/static/images')


@route('/bower_components/:path#.+#')
def server_static(path):
        print 'static!', path
        return static_file(path, root='../app/bower_components')


@route('/core/:path#.+#')
def server_static(path):
        print 'static!', path
        return static_file(path, root='../app/core')


@route('/agency-creator/:path#.+#')
def server_static(path):
        print 'static!', path
        return static_file(path, root='../app/agency-creator')


@route('/agency-list/:path#.+#')
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
        results = []
        for agency in agencies:
                results.append(agency.get_dict())
        return json.dumps(results)


@post('/add_agency')
def add_agency():
        agency = slDao.add_agency(request.json['name'],
                                  request.json['description'],
                                  int(request.json['grade']),
                                  request.json['tags'])
        return json.dumps(agency.__str__())


# run the app
run(host='localhost', port=8080)

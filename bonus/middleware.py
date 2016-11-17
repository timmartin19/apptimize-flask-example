from myapp.manage import app


def header_injection_middleware(environ, start_response):
    environ['some-extra-header'] = 'blah'
    return app(environ, start_response)

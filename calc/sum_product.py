from cgi import parse_qs
from template2 import html

def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    a = d.get('a', [''])[0]
    b = d.get('b', [''])[0]
    c = 0


    if '' not in [a,b]:
        a, b = int(a), int(b)
        for i in range(b):
            c = c+a
    sum = a+b
    product = c


    response_body = html % {
        'sum' : sum,
        'product' : product,
    }

    start_response('200 OK', [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ])
    return [response_body]

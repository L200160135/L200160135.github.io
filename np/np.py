from urllib.request import Request
from urllib.parse import urlparse   ##URLs
from urllib.parse import urljoin    ##PATH
from urllib.parse import parse_qs   ##QUERY STRINGS
from urllib.parse import quote      ##URL ENCODING
from urllib.parse import urlencode  ##URL ENCODING
from urllib.parse import urlunparse ##URL ENCODING
from urllib.request import urlopen
response = urlopen('http://www.debian.org')



def start():
    print ("---- MENU HTTP----")
    print ("[1.] request & response")
    print ("[2.] http headers")
    print ("[3.] user agents")
    print ("[4.] redirects")
    print ("[5] URLs")
    print ("[6] Paths and relative URLs")
    print ("[7] Query Strings")
    print ("[8] URL encoding")
    print ("[0.] keluar")
    pilih = input("pilih : ")
    if pilih == '1':
        menu()
    elif pilih == '2':
        header()
    elif pilih == '3':
        user()
    elif pilih == '4':
        redirect()
    elif pilih == '5':
        urls()
    elif pilih == '6':
        path()
    elif pilih == '7':
        query()
    elif pilih == '8':
        encoding()
    elif pilih == '0':
        exit()

def menu():
    response = urlopen('http://www.debian.org')
    print ("---- MENU ----")
    print ("[1.] Request")
    print ("[2.] Response.readline")
    print ("[3.] Response Object")
    print ("[4.] Response.read")
    print ("[5.] Status codes")
    print ("[0.] kembali")
    pilih = input("pilih : ")

    if pilih =='1':
	
        print (response)
        menu()
    elif pilih == '2':
        print (response.readline())
        menu()
    elif pilih == '3':
        print (response.url)
        menu()
    elif pilih == '4':
        print (response.read(50))
        print (response.read)
        menu()
    elif pilih == '5':
        print (response.status)
        menu()
    elif pilih == '0':
        start()
    else:
        print ("MAAF PERMINTAAN TIDAK SESUAI")
        menu()

def header():
    print ("--- MENU ---")
    print ("[1.] Http header")
    print ("[2.] Customizing request")
    print ("[0.] kembali")
    pilih = input("pilih : ")

    if pilih == '1':
        response = urlopen('http://www.debian.org')
        print (response.getheaders())
        header()
    elif pilih == '2':
        req = Request('http://www.debian.org')
        req.add_header('Accept-Language', 'sv')
        response = urlopen(req)
        print (response.readlines()[:5])
        header()        
    elif pilih == '0':
        start()
    else:
        print ("MAAF PERMINTAAN TIDAK SESUAI")
        header()
def user():
    print ("--- MENU ---")
    print ("[1.] user agents")
    print ("[0.] kembali")
    pilih = input("pilih : ")

    if pilih == '1':
        req = Request('http://www.python.org')
        urlopen(req)
        print (req.get_header('User-agent'))
        user()
    elif pilih == '0':
        start()
    else:
        print ("MAAF PERMINTAAN TIDAK SESUAI")
        user()
def redirect():
    print ("--- MENU ---")
    print ("[1.] redirect")
    print ("[2.] redirect_dict")
    print ("[0.] kembali")
    pilih = input("pilih : ")

    if pilih == '1':
        req = Request('http://www.gmail.com')
        response = urlopen(req)
        print (response.url)
        redirect()
    elif pilih == '2':
        req = Request('http://www.gmail.com')
        response = urlopen(req)
        print (req.redirect_dict)
        redirect()
    elif pilih == '0':
        start()
    else:
        print ("MAAF PERMINTAAN TIDAK SESUAI")
        redirect()

def urls():
    result = urlparse('http://www.python.org/dev/peps')
    print ("---- MENU ----")
    print ("[1] Result")
    print ("[2] Result.netloc")
    print ("[3] Result.path")
    print ("[4] urlparse('http://www.python.org:8080/')")
    print ("[0] kembali")

    pilih = input("Pilih : ")

    if pilih == '1':
        print (result)
        urls()
    elif pilih == '2':
        print (result.netloc)
        urls()
    elif pilih == '3':
        print (result.path)
        urls()
    elif pilih == '4':
        print (urlparse('http://www.python.org:8080/'))
        urls()
    elif pilih == '0':
        start()
    else:
        print ("MAAF PERMINTAAN TIDAK SESUAI")
        urls()

def path():
    print ("---- MENU ----")
    print ("[1] urlparse('http://www.python.org/')")
    print ("[2] urlparse('../images/tux.png')")
    print ("[3] urljoin('http://www.debian.org', 'intro/about')")
    print ("[4] urljoin('http://www.debian.org/intro/', 'about')")
    print ("[5] urljoin('http://www.debian.org/intro', 'about')")
    print ("[6] urljoin('http://www.debian.org/intro/about', '/News')")
    print ("[7] urljoin('http://www.debian.org/intro/about/', '../News')")
    print ("[8] urljoin('http://www.debian.org/intro/about/', '../../News')")
    print ("[9] urljoin('http://www.debian.org/intro/about', '../News')")
    print ("[10] urljoin('http://www.debian.org/about', 'http://www.python.org')")
    print ("[0] kembali")

    pilih = input("Pilih : ")

    if pilih == '1':
        print (urlparse('http://www.python.org/'))
        path()
    elif pilih == '2':
        print (urlparse('../images/tux.png'))
        path()
    elif pilih == '3':
        print (urljoin('http://www.debian.org', 'intro/about'))
        path()
    elif pilih == '4':
        print (urljoin('http://www.debian.org/intro/', 'about'))
        path()
    elif pilih == '5':
        print (urljoin('http://www.debian.org/intro', 'about'))
        path()
    elif pilih == '6':
        print (urljoin('http://www.debian.org/intro/about', '/News'))
        path()
    elif pilih == '7':
        print (urljoin('http://www.debian.org/intro/about/', '../News'))
        path()
    elif pilih == '8':
        print (urljoin('http://www.debian.org/intro/about/', '../../News'))
        path()
    elif pilih == '9':
        print (urljoin('http://www.debian.org/intro/about', '../News'))
        path()
    elif pilih == '10':
        print (urljoin('http://www.debian.org/about', 'http://www.python.org'))
        path()
    elif pilih == '0':
        start()
    else:
        print ("MAAF PERMINTAAN TIDAK SESUAI")
        path()

def query():
    print ("---- MENU ----")
    print ("[1] urlparse('http://docs.python.org/3/search.html?q=urlparse&area=default')")
    print ("[2] parse_qs(result.query)")
    print ("[3] parse_qs(result.query)")
    print ("[0] kembali")

    pilih = input("pilih: ")

    if pilih == '1':
        print(urlparse('http://docs.python.org/3/search.html?q=urlparse&area=default'))
        query()
    if pilih  == '2':
        result = urlparse('http://docs.python.org/3/search.html?q=urlparse&area=default')
        print(parse_qs(result.query))
        query()
    if pilih == '3':
        result = urlparse('http://docs.python.org/3/search.html?q=urlparse&q=urljoin')
        print(parse_qs(result.query))
        query()
    if pilih == '0':
        start()
    else:
        print ("MAAF PERMINTAAN TIDAK SESUAI")
        query()


def encoding():
    print ("---- MENU ----")
    print ("[1] quote('A duck?')")
    print ("[2] query_enc")
    print ("[3] urlunparse(('http', netloc, path_enc, '', query_enc, ''))")
    print ("[4] quote(path)")
    print ("[5] quote(path)")
    print ("[0] kembali")

    pilih = input("Pilih : ")

    path = 'pypi'
    path_enc = quote(path)
    query_dict = {':action': 'search', 'term': 'Are you quite sure this is a cheese shop?'}
    query_enc = urlencode(query_dict)
    netloc = 'pypi.python.org'
        
    if pilih == '1':
        print(quote('A duck?'))
        encoding()
    if pilih == '2':
        print (query_enc)
        encoding()
    if pilih == '3':  
        print (urlunparse(('http', netloc, path_enc, '', query_enc, '')))
        encoding()
    if pilih == '4':
        path = '/images/users/+Zoot+/'
        print (quote(path))
        encoding()
    if pilih == '5':
        username = '+Zoot/Dingo+'
        path = 'images/users/{}'.format(username)
        print (quote(path))
        encoding()
    if pilih == '0':
        start()
    else:
        print ("MAAF PERMINTAAN TIDAK SESUAI")
        encoding()

start()


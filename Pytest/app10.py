import pytest

def run():
    print("+" + 80*"-" + "Lab 10"+ 80*"-" + "+")
class BadHTTPVersion(Exception):
    pass
class BadRequestTypeError(Exception):
    pass
class store_HTTP:
    def __init__(self, request):
        request = request.split(" ")
        self.type = request[0]
        self.path = request[1]
        self.protocol = request[2]
def reqstr2obj(request_string):
    if isinstance(request_string, str) is False:
        raise TypeError
    if len(request_string.strip().split(" ")) != 3:
        return None
    httpResult = store_HTTP(request_string)
    if httpResult.protocol not in ['HTTP1.0','HTTP1.1','HTTP2.0']:
        raise BadHTTPVersion
    if httpResult.path.startswith('/') == False:
        raise ValueError("It can't start with '/'")
    if httpResult.type not in ['GET','PUT','DELETE','TRACE','OPTIONS', 'PATCH', 'POST', 'CONNECT','HEAD']:
        raise BadRequestTypeError
    return httpResult

def test_1():
    with pytest.raises(TypeError):
        reqstr2obj(555)

def test_2():
    assert isinstance(reqstr2obj("GET / HTTP1.1"), store_HTTP)

def test_3():
    test_sequence = reqstr2obj("GET / HTTP1.1")
    assert test_sequence.protocol == "HTTP1.1"
    assert test_sequence.type == "GET"
    assert test_sequence.path == "/"

def test_4():
    new_req = "PUT /index HTTP2.0"
    test_different_args = reqstr2obj(new_req)
    new_req_split = new_req.split(" ")
    assert test_different_args.protocol == new_req_split[2]
    assert test_different_args.path == new_req_split[1]
    assert test_different_args.type == new_req_split[0]

def test_5():
    assert reqstr2obj("PUT PUT / HTTP2.0") == None
    assert reqstr2obj("PUT / HTTP 2.0") == None
    assert reqstr2obj("POST HTTP1.1") == None
    assert reqstr2obj("PUT") == None

def test_6():


if __name__=="__main__":
    run()
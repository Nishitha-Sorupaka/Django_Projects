from django.http import HttpResponse
class FirstMiddleWare(object):
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        print('This line printed by Middleware-1 before processing the request')
        response = self.get_response(request)
        print('This line printed by Middleware-1 after processing the request')
        return response

class SecondMiddleWare(object):
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        print('This line printed by Middleware-2 before processing the request')
        response = self.get_response(request)
        print('This line printed by Middleware-2 after processing the request')
        return response




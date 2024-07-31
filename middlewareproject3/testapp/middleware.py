from django.http import HttpResponse
class ErrorMessageMiddleware(object):
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        #return HttpResponse("<h1>Currently we are facing some technical issue...please try after some time</h1>")
        return HttpResponse(f'<h1>Currently we are facing some technical issue. <br>Technical Error Class Name: {exception.__class__.__name__} <br>Error Message: {exception}</h1>')
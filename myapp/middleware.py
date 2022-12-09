import datetime
class myappmiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        print('myappmiddleware')
        response = self.get_response(request)
        response.set_cookie('last_access_time',datetime.datetime.now())
        return response 

           
      
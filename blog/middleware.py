class TraceIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("Middleware called")
        ip = request.META.get('REMOTE_ADDR')
        print(f"IP: {ip}")  
        response = self.get_response(request)
        return response
    

class LogUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            print(f"Logged in user: {request.user.clientname}") 
        else:
            print("Anonyms User")
        response = self.get_response(request)
        return response
    

    
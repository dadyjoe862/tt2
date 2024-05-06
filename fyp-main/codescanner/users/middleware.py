from django.shortcuts import redirect

class RestrictPageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and request.path == '/users/login/':
            # Redirect authenticated users away from the login page
            return redirect('users/dashboard')

        response = self.get_response(request)
        return response

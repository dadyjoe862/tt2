from django.shortcuts import render, redirect, HttpResponse
from .forms import createUserForm
import os
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib import messages
import requests
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Files
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

@csrf_exempt
def upload_files(request):
    if request.method == 'POST' and request.FILES.getlist('files'):
        for uploaded_file in request.FILES.getlist('files'):
            # Handle file saving into the database
            file_name = uploaded_file.name
            file_path = os.path.join(settings.MEDIA_ROOT, settings.UPLOAD_DIR, file_name)
            file_extension = file_name.split('.')[-1].lower()
            
            # Determine the language based on the file extension
            if file_extension == 'py':
                language = 'Python'
            elif file_extension == 'php':
                language = 'PHP'
            else:
                language = 'Unknown'

            # Save the file information into the database
            file_object = Files(name=file_name, path=file_path, extension=file_extension, language=language)
            print( file_object)
            file_object.save()

        # You can return some response to acknowledge successful upload
        response = {'message': 'Files uploaded successfully'}
        return JsonResponse(response)

    # Return error response if files were not uploaded
    response = {'error': 'No files uploaded or invalid request method'}
    return JsonResponse(response, status=400)








# This view redirects the user to GitHub for authentication
def github_login(request):
    # Redirect the user to GitHub OAuth authorization URL
    github_authorization_url = 'https://github.com/login/oauth/authorize'
    client_id = 'abf51e0f50b882c3fc8e'
    redirect_uri = 'http://127.0.0.1:8000/dashboard'  # Redirect URI configured in GitHub app settings
    scope = 'repo'  # Scope to access repositories
    return redirect(f'{github_authorization_url}?client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}')



# This view handles the callback from GitHub after user authentication
def github_callback(request):
    # Extract the authorization code from the callback URL
    code = request.GET.get('code')
    
    # Exchange the authorization code for an access token
    token_url = 'https://github.com/login/oauth/access_token'
    client_id = 'abf51e0f50b882c3fc8e'
    client_secret = 'e72c50553f8dc31fb678e2c32860a0df008704a4'
    redirect_uri = 'http://127.0.0.1:8000/dashboard'  # Redirect URI configured in GitHub app settings
    
    payload = {
        'client_id': client_id,
        'client_secret': client_secret,
        'code': code,
        'redirect_uri': redirect_uri
    }
    
    headers = {
        'Accept': 'application/json'
    }
    
    # Make a POST request to exchange the code for an access token
    response = requests.post(token_url, data=payload, headers=headers)
    
    if response.status_code == 200:
        # Extract the access token from the response
        access_token = response.json().get('access_token')

        # Display success message
        messages.success(request, 'Successfully connected to GitHub')
        
        # Store the access token in the session
        request.session['github_access_token'] = access_token
        
        # Redirect the user to the view that fetches GitHub repositories
        return redirect('github_repositories')
    else:
        # Handle errors
        return HttpResponse('Error retrieving access token from GitHub', status=response.status_code)
    


# This view fetches repositories of the authenticated user from GitHub
# This view fetches repositories of the authenticated user from GitHub
def github_repositories(request):
    # Retrieve the access token from the session after OAuth authentication
    access_token = request.session.get('github_access_token')
    
    # Check if the access token exists
    if access_token:
        # Set up the headers for GitHub API request
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Accept': 'application/vnd.github.v3+json'
        }
        
        # Make a GET request to GitHub API to fetch user repositories
        response = requests.get('https://api.github.com/user/repos', headers=headers)
        print(response.status_code)
        
        # Check the response status code
        if response.status_code == 200:
            # Parse the JSON response to extract repositories
            repositories = response.json()
            # Pass repositories to the template
            return render(request, 'users/dashboard.html', {'repositories': repositories})
        else:
            # Handle API request errors
            return HttpResponse('Error fetching repositories', status=response.status_code)
    else:
        # Redirect the user to log in with GitHub if the access token is not found
        return redirect('github_login')




# Create your register view here ====================================================================
@never_cache
def register(request):
        form = createUserForm()
        if request.method == 'POST':
            form = createUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                return redirect('users-login') 
        context = {'registerForm':form}
        return render(request,'users/register.html', context = context)


@never_cache
def loginForm(request):
        if request.user.is_authenticated:
        # If user is already logged in, redirect to dashboard
            return redirect('users-dashboard')
        else:
            if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')

                user = authenticate(request, username=username, password= password)

                if user is not None:
                    login(request, user)
                    request.session['username'] = username
                    return redirect('users-dashboard')
                else:
                    context['error'] = 'Invalid username or password'
                    return redirect('users-login')
        context = {}
        return render(request, 'users/login.html', context = context)



def logoutUser(request):
    # Destroying session on logout
    if 'username' in request.session:
        del request.session['username']
    logout(request)
    return redirect('users-login')


@ login_required(login_url='users-login')
@never_cache
def dashboard(request):
 if request.user.is_authenticated:

    return render(request, 'users/dashboard.html')
 else:
    return render(request, 'users/login.html')



@login_required(login_url='users-login')
@never_cache
def scan(request):
    if request.user.is_authenticated:
        return render(request, 'users/scan.html')
    else:
        return render(request, 'users/login')


@login_required(login_url='users-login')
@never_cache
def profile(request):
     if request.user.is_authenticated:
        return render(request,'users/profile.html')
     else:
        return render(request, 'users/login')
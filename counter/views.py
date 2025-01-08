from django.shortcuts import redirect, render
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
# 9on/5HqzxszKHlYS/PobNg==IT0FLIw6SF6Qp5Hs 
# Create your views here.
def home(request):

    import json
    import requests
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
        api_request = requests.get (api_url + query, headers={'X-Api-Key': '9aB02x2/LcFga/NR4mHtBg==sXJtSHspoeqSBjQt'}, params={'q': query})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "Oops! There was an error"
            print(e)
        return render(request, 'home.html',{'api':api})
    else : 
        return render(request,'home.html',{'query':'Enter a valid query'})

def signup_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()
            return redirect('home')  # Redirect to the home page
    else:
        form = UserRegistrationForm()

    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Replace 'home' with the name of your home view URL pattern
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def custom_logout(request):
    logout(request)  # Logs out the user
    return redirect('home')  # Redirect to the home page
   

# This is the home view for the Food Calorie Counter app. It renders the home page.


# # app/user_profile/views.py

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# # Locals

# # Create your views here.

# USER LOGIN
def login_view(request):
	# Let the logged in user go directly to the home page.
	if request.user.is_authenticated:
		messages.info(request, f'{request.user.username } You Have Already Login ;)')
		return redirect('page:home')

	context = dict()

	if request.method == "POST":
		# print(request.POST)
		username = request.POST.get('username')
		password = request.POST.get('password')
		# print(username, password)
		
		if len(username) < 6 or len(password) < 6:
			messages.warning(request, f'Please Enter the Username and Password Correctly.. It must not be less than 6 characters..')
			return redirect('user_profile:login')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			messages.success(request, f'{request.user.username } You are logged in')
			return redirect('page:home')
			
	return render(request, 'user_profile/login.html', context)


# USER LOGOUT
def logout_view(request):
	messages.info(request, f'{request.user.username} Signed Out')
	logout(request)
	return redirect('page:home')


# USER REGISTER
def register_view(request):
    return render(request, 'user_profile/register.html')

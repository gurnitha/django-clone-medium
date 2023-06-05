# # app/user_profile/views.py

# # Django and third parties modules
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login

# # Locals

# # Create your views here.

# def login_view(request):
# 	context = dict()
# 	if request.method == "POST":
# 		# print(request.POST)
# 		username = request.POST.get('username')
# 		password = request.POST.get('password')
# 		print(username, password)
# 		# Bu bilgileri dogru aldik mi?
# 		user = authenticate(request, username=username, password=password)
# 		if user is not None:
# 			login(request, user)
# 			# login oldugunu kullaniciya belli edelim!
# 			return redirect('page:home')
# 	return render(request, 'user_profile/login.html', context)



from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


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
		print(username, password)
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, f'{request.user.username } You are logged in')
			return redirect('page:home')
			
	return render(request, 'user_profile/login.html', context)
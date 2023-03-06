from django.shortcuts import render

# Create your views here.

def signin_view(request):
	return render(request, "login.html", {"page":"Sign In Page"})

def signup_view(request):
	return render(request, "signup.html", {"page":"Sign Up Page"})

def Err404_view(request):
	return render(request, "error-404.html", {"page":"Error 404 Page"})

def Err500_view(request):
	return render(request, "error-500.html", {"page":"Error 500 Page"})

def origin_view(request):
	return render(request, "firstpage.html", {"page":"Origin Point Page"})

def feed_view(request):
	return render(request, "feed.html", {"page":"Feed Page"})

def profile1_view(request):
	return render(request, "1profile.html", {"page":"Profile 1st person view Page"})

def profile3_view(request):
	return render(request, "3profile.html", {"page":"Profile 3rd person view Page"})

from django.shortcuts import render
from .forms import SignUpForm

# Create your views here.
def home(request):
	title = 'Sign Up'
	# if request.user.is_authenticated():
	# 	title = 'My Title %s' %(request.user)
	
	#add form
	form = SignUpForm(request.POST or None)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()

	context = {
		"title" : title,
		"form" : form,
	}
	return render(request, "home.html", context)

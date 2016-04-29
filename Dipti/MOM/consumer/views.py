# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.template import loader
from datetime import date
from django.views.generic import ListView

from .models import Producer, Dish

from .forms import SearchForm

def index(request):
    
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            zipcode = form.cleaned_data['zipcode']
            date = form.cleaned_data['date']
            # redirect to a new URL:
            return HttpResponseRedirect('/consumer/results/zip/' + str(zipcode) + '/date/' + str(date) +'/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()

    return render(request, 'consumer/index.html', {'form': form})


class ResultsView(ListView):
    
    template_name = "consumer/results_text.html"
    model = Producer
    context_object_name = 'results_list'
    #current_producer = ''

    def get_context_data(self, **kwargs):
        context = super(ResultsView, self).get_context_data(**kwargs)
        context['dishes_list'] = Dish.objects.filter(date=self.kwargs['query_date'])  #, producer__name=self.name) Note: the remaining commented logic is taken to template.
        return context

    def get_queryset(self, **kwargs):
        qs = super(ResultsView, self).get_queryset(**kwargs)        #default
        #zip = self.request.GET.get('query_zip', '')
        producers_list = qs.filter(zipcode=int(self.kwargs['query_zip']))
        return producers_list
 



'''
def index(request):
	# Code for index page
	# JUST INCLUDE the index.html template here.
    last_zip = Producer.objects.order_by('zipcode')[:5]
    output = ','.join([p.name for p in last_zip])
    # return HttpResponse("Hello, world. You're at the index of MOM-consumer")
    return HttpResponse(output)


class ResultView(ListView):

	context_object_name = 'results_list'
	#template_name = 'consumer/results_text.html'
	## FIGURE OUT HOW TO SEND PARAMETERS TO TWO FILTERS BELOW
	queryset = Producer.objects.filter(zipcode=94608, dish__date='2016-04-12')

	def get_resultP_data(self, **kwargs):
		
		
		resultP = super(ResultView, self).get_resultP_data(**kwargs)

		return HttpResponse("resultP is %s" % (resultP))

		for currP in resultP:
			resultP['dish'] = Dish.objects.filter(date='2016-04-12', producer__name=currP.name)
			print resultP
			#return resultP  

'''

################## MORE EXAMPLES FOR REFERENCE ###############

'''
def results_text(request, query_zip, query_date):
	
	
	NEED CREATE A LIST OF OBJECTS TO BE SENT TO THE TEMPLATE WHICH WILL INSERT IT INTO HTML

	resultP=Producer.objects.filter(zipcode=94608, dish__date='2016-04-12')
	
	for currP in resultP:
    	print currP.name
    	print currP.address
    	resultDish = Dish.objects.filter(date='2016-04-12', producer__name=currP.name)
    		print resultDish

	'''

'''
Advanced Class Based views

class IndexView(ListView):
   	context_object_name = 'home_list'    
   	template_name = 'contacts/index.html'
   	queryset = Individual.objects.all()

   	def get_context_data(self, **kwargs):
        	context = super(IndexView, self).get_context_data(**kwargs)
        	context['roles'] = Role.objects.all()
        	context['venue_list'] = Venue.objects.all()
        	context['festival_list'] = Festival.objects.all()
        	# And so on for more models
        	return context
'''

	#return HttpResponse("Requested zip is %s and date is %s AND currP is %s" % (query_zip, query_date, pname))
	#return HttpResponse("Requested zip and date")

'''
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
'''

from django.shortcuts import render
from credapp import creditCheck
from django.http import HttpResponseRedirect
from .forms import NameForm



def index(request):
    
    form = NameForm()

    return render(request, 'checker/home.html', {'form': form})


def get_result(request):

    if request.method == 'POST':
        
		# create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            cd = form.cleaned_data
            redditor=cd['your_name']
            resultdictionary = creditCheck(redditor)
        else:
        	resultdictionary = {}
        	form = NameForm()
        	return render(request, 'checker/home.html', {'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
        return render(request, 'checker/home.html', {'form': form})	

    return render(request, 'checker/result.html', resultdictionary)
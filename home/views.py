from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
import whois

def home(request):

	context = {

	}

	if request.method == 'POST':

		domainName = request.POST.get('domainName')
		try:
			w = whois.whois(domainName)
			
			context = {
				'data': w
			}
		except (whois.parser.PywhoisError, RuntimeError):
			context = {
				'data': {
					'Error': 'Not found!'
				}
			}
		except Exception as e:
			 context = {
			 	'data': {
			 		'Error': 'Error'
			 	}
			 }

		

	return render(request, 'home/index.html', context)

def result(request):

	return render(request, 'home/result.html')
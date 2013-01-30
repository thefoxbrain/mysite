from django.shortcuts import render_to_response
# from django.template.loader import get_template
# from django.template import Context
# from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("Hello world")
"""	
def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)
"""
	
"""
def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html', {'current_date': now})
"""

def current_datetime(request):
    current_date = datetime.datetime.now()
    return render_to_response('current_datetime.html', locals())

"""	
def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
	return HttpResponse(html)	
"""
	
def hours_ahead(request, hour_offset):
	try:
		hour_offset = int(hour_offset)
	except ValueError:
		raise Http404()
	next_time = datetime.datetime.now() + datetime.timedelta(hours=hour_offset)
	return render_to_response('hours_ahead.html', locals())
	
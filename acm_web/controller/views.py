# Create your views here.
from django.http import HttpResponse
from django.template import loader, RequestContext

import re

def home(request):
    template = loader.get_template('controller/index.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def page(request):
    #    import pudb; pudb.set_trace()
    path = request.path[1:]
    template = loader.get_template('controller/%s' % path)
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

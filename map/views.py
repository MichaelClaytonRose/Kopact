from django.http import HttpResponse
from django.template import RequestContext, loader
from map.models import Location
from django.core.urlresolvers import reverse
from django.views import generic
from django.shortcuts import render_to_response

def index(request, display=True):
    'Display map'
    Locations = Location.objects.all()
    return render_to_response('map/index.html', {'Locations': Locations
    })

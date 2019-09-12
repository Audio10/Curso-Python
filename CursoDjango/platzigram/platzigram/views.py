""" Platzi views"""

#Django
from django.http import HttpResponse

# Utilities
from datetime import datetime
import json

def hello_world(request):
    """ Return a greeting """
    now = datetime.now().strftime('%b %dth, %H:%M hrs')
    return HttpResponse('Oh, hi! Current server time is {now}'.format(now= str(now)))


def sort_integers(request):
    """ Return a json response with sorted integers. """
    # ?numbers = 3, 4, 5, 6
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)

    data= {
        'status' : 'ok',
        'numbers' : sorted_ints,
        'message' : 'Integers sorted successfully'
    }

    # RETORNA data COMO JSON
    return HttpResponse(
        json.dumps(data), 
        content_type='application/json'
    )


def say_hi(request, name, age):
    """ Return a greeting"""

    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello, {}! wellcome to Platzigram'.format(name)
    return HttpResponse(message)

# django
from django.http import HttpResponse

# utils
from datetime import datetime
import json

def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Hello, the current server time is: {now}'.format(now=str(now)))


def sorted_numbers(request) :
    """hi."""
    numbers = request.GET['numbers']
    numbers_list = [int(i) for i in numbers.split(',')]
    sorted_numbers_list = sorted(numbers_list)
    data_dict = {
        'status': 'ok',
        'numbers': sorted_numbers_list,
        'message': 'Integers sorted successfully',
    }
    #import pdb; pdb.set_trace()
    return HttpResponse(
        json.dumps(data_dict, indent=4),
        content_type='application/json'
    )


def validate_age(request, name, age):
    if (age < 12):
        message = "Sorry {} you are not allow here".format(name)
    else:
        message = 'Hi {} welcome to Platzigram'.format(name)

    return HttpResponse(message)

import os
import random
import string
from random import randint
from django.utils import timezone

import requests
from django.conf import settings
from main.middlewares import RequestMiddleware

def get_auto_id(model):
    auto_id = 1
    latest_auto_id = None
    if model.objects.all().exists():
        latest_auto_id = model.objects.all().latest("auto_id")
    if latest_auto_id:
        auto_id = latest_auto_id.auto_id + 1
    return auto_id

def randomnumber(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def generate_form_errors(args,formset=False):
    message = ''
    if not formset:
        for field in args:
            if field.errors:
                message += field.errors 
        for err in args.non_field_errors():
            message += str(err)
                
    elif formset:
        for form in args:
            for field in form:
                if field.errors:
                    message +=field.errors
            for err in form.non_field_errors():
                message += str(err)
    return message


def get_timezone(request):
    if "set_user_timezone" in request.session:
        user_time_zone = request.session['set_user_timezone']
    else:
        user_time_zone = "Asia/Kolkata"
    return user_time_zone


def generate_serializer_errors(args):
    message = ""
    for key, values in args.items():
        error_message = ""
        for value in values:
            error_message += value + ","
        error_message = error_message[:-1]

        # message += "%s : %s | " %(key,error_message)
        message += f"{key} - {error_message} | "
    return message[:-3]
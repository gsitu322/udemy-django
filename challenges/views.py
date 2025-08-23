from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render

# Create your views here.

def monthly_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "January"
    elif month == "february":
        challenge_text = "February"
    elif month == "march":
        challenge_text = "March"
    else:
        return HttpResponseNotFound("Incorrect month provided")

    return HttpResponse(f"Hello, world. {challenge_text}")
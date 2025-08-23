from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render

monthly_challenges = {
    "january": "january",
    "february": "february",
    "march": "march",
    "april": "april",
    "may": "may",
    "june": "june",
    "july": "july",
    "august": "august",
    "september": "september",
    "october": "october",
    "november": "november",
    "december": "december",
}
# Create your views here.

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound('Invalid month provided')

    redirect_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + redirect_month)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound('Invalid month provided')

    return HttpResponse(f"Hello, world. {challenge_text}")
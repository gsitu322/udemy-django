from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.template.loader import render_to_string

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

def _get_months():
    return list(monthly_challenges.keys())

def monthly_challenge_by_number(request, month):
    months = _get_months()

    if month > len(months):
        return HttpResponseNotFound('Invalid month provided')

    redirect_month = months[month - 1]
    redirect_url = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_url)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = render_to_string("challenges/challenge.html")
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>Invalid month provided</h1>")

def index(request):
    response_data = ""
    for month in _get_months():
        redirect_url = reverse('month-challenge', args=[month])
        response_data += f"<a href='{redirect_url}'>{month.capitalize()}</a></br></br>"

    return HttpResponse(response_data)
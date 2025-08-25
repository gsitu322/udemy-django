from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
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
    "december": None,
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
        return render(request, "challenges/challenge.html", {
            "month": month,
            "text": challenge_text,
        })
    except:
        raise Http404('Invalid month provided')

def index(request):
    return render(request, "challenges/index.html", {
        "months": _get_months(),
    })
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

monthly_challenges = {
    "january": "Dry January – no alcohol for the month",
    "february": "Daily journaling – write one page a day",
    "march": "Steps challenge – walk 10,000 steps daily",
    "april": "No social media after 8pm",
    "may": "Try a new hobby or skill each week",
    "june": "Read 20 minutes every day",
    "july": "Hydration challenge – drink 8 glasses of water daily",
    "august": "Declutter – remove 1 item from your home daily",
    "september": "Learn or practice meditation (10 min/day)",
    "october": "No added sugar month",
    "november": "Gratitude challenge – write 3 things you’re thankful for daily",
    "december": "Acts of kindness – do one small kind thing each day",
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
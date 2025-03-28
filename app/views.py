from django.shortcuts import render, get_object_or_404
from .models import Agency
from django.db.models import Q
import requests

from bs4 import BeautifulSoup

# Create your views here.
def search(request):
    query = request.GET.get('query')
    results = []
    if query:
        results = Agency.objects.filter(
            Q(name__icontains=query) |
            Q(short_name__icontains=query)
        ).distinct()
    return render(request, "search.html", {'results': results, 'query': query})

def agency_detail(request, pk):

    agency = get_object_or_404(Agency, pk=pk)

    start_date = request.GET.get('date', '2018-01-01')
    date = request.GET.get('date', '2025-03-01')

    info = {'chapter_length' : {}, 'total_length' : 0, 'book_comparison' : 0, 'past_length' : 0, 'percent_change' : 0}

    # Getting the chapter length for each cfr reference
    for cfr_ref in agency.cfr_references.all():
        st_data = requests.get(f"https://www.ecfr.gov/api/versioner/v1/full/{start_date}/title-{cfr_ref.title}.xml?chapter={cfr_ref.chapter}")
        ch_data = requests.get(f"https://www.ecfr.gov/api/versioner/v1/full/{date}/title-{cfr_ref.title}.xml?chapter={cfr_ref.chapter}")

        st_soup = BeautifulSoup(st_data.content, 'xml')
        ch_soup = BeautifulSoup(ch_data.content, 'xml')

        st_length = len(st_soup.get_text().split())
        ch_length = len(ch_soup.get_text().split())
        
        info['chapter_length'][f"Title: {cfr_ref.title} - Chapter: {cfr_ref.chapter}"] = ch_length
        info['past_length'] += st_length
        info['total_length'] += ch_length
    
    info['book_comparison'] = int(info['total_length'] / 3000)
    info['percent_change'] = int((info['total_length'] - info['past_length']) / info['past_length'] * 100) if info['past_length'] != 0 else 0

    return render(request, 'agency_detail.html', {'agency': agency, 'info': info, 'date' : date})

def home(request):
    return render(request, 'home.html', {"agencies": Agency.objects.all()})

def about(request):
    return render(request, 'about.html', {})
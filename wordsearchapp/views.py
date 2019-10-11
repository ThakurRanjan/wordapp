from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .search import search, sorting
import json

#renders search page.
def search_view(request):
    return render(request, 'search.html', {})

#Return autocomplete results while user types a letter.
def search_autocomplete(request):
    if request.is_ajax():
        query = request.GET.get('term','')
        results = sorting(search(query.lower()), query.lower())
        data = json.dumps(results)
    else:
        data = 'fail'
    type = 'application/json'
    return HttpResponse(data, type)

# Return jsonresponse have the search results(25 words) contain the search word
def getSearchResults(request):
    if request.method == 'GET':
        query = request.GET.get('term')
        if query:
            searchResult = sorting(search(query.lower()), query.lower())
            if len(searchResult) == 0:
                return JsonResponse({'Search_Result': "Word not found."})
            else:
                return JsonResponse({'Search_Result': searchResult})
        else:
            return redirect('/')

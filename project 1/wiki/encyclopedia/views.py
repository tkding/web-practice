from django.shortcuts import render, redirect
from django.urls import reverse

from . import util
import re

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, name):
    entry_content = util.get_entry(name)

    if entry_content is None:
        # Entry does not exist, render error page
        return render(request, 'encyclopedia/error.html', {'message': 'Page not found'})

    # Entry exists, render the page with entry content
    return render(request, 'encyclopedia/entry.html', {
        'name': name, 
        'content': entry_content
    })

def search_results(request):
    query= request.GET.get('q', '')
    entry_content = util.get_entry(query)

    # Entry does not exist
    if entry_content is None:
        # find similar term
        pattern = r".*{}$".format(query)
        matching_entries = [s for s in util.list_entries() if re.search(pattern, s)]
        
        if matching_entries:
            return render(request, 'encyclopedia/search_results.html', {
                'query' : query,
                'entries': matching_entries
            })
        
        else:
            return render(request, 'encyclopedia/no_result.html', {
                'query' : query
            })
            


    # Entry exists, render the page with entry content
    return render(request, 'encyclopedia/entry.html', {
        'name': query, 
        'content': entry_content
    })
    
def create_page(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content', '')
        
        print("Test")
        print(type(request.POST.get('content', '')))
        print(content)
        print()
        
        #check if an entry with the same title alread exists
        if util.get_entry(title):
            return render(request, 'encyclopedia/error.html', {
                'message' : 'Entry with the same title already exists'
            })
            
        #save new entry
        util.save_entry(title, content)
        
        #redirect to the newly created entry's page
        return redirect(reverse('title', args=[title]))
    
    #render the create page form
    return render(request, 'encyclopedia/create_page.html')
    
    
    
    
            
    



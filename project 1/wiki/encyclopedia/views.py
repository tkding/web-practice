from django.shortcuts import render, redirect
from django.urls import reverse

from . import util
import re
import random
import markdown2

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, name):
    entry_content = util.get_entry(name)

    if entry_content is None:
        # Entry does not exist, render error page
        return render(request, 'encyclopedia/error.html', {'message': 'Page not found'})

    entry_html = markdown2.markdown(entry_content)
    # Entry exists, render the page with entry content
    return render(request, 'encyclopedia/entry.html', {
        'name': name, 
        'content': entry_html
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
    
def edit_page(request, name):
    if request.method == "POST":
        content = request.POST.get('content')
        
        # save the updated entry
        util.save_entry(name, content)
        
        # redirect back to entry page
        return redirect(reverse('title', args=[name]))

    # Retrieve the existing entry content
    entry_content = util.get_entry(name)
    
    return render(request, 'encyclopedia/edit_page.html',{
            'name': name,
            'content':entry_content
    })
    
def random_page(request):
    entries = util.list_entries()
    
    # select a random entry from the list
    random_entry = random.choice(entries)
    
    # Redirect to the randomly selected entry's page
    return redirect('title', name=random_entry)
        
            
    



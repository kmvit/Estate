from django.shortcuts import render
from agency.models import Category, Estate, Page
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.generic import ListView, DetailView
from datetime import datetime


def index(request):
    category_list = Category.objects.filter(parent_category__isnull=True)
    estates = Estate.objects.all()
    context_dict = {'categories': category_list, 'estates': estates}
    visits = request.session.get('visits')
    if not visits:
        visits = 0
    reset_last_visit_time = False

    last_visit = request.session.get('last_visit')
    if last_visit:
        last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")
        if (datetime.now() - last_visit_time).seconds > 0:
            # ...reassign the value of the cookie to +1 of what it was before...
            visits = visits + 1
            # ...and update the last visit cookie, too.
            reset_last_visit_time = True
    else:
        # Cookie last_visit doesn't exist, so create it to the current date/time.
        reset_last_visit_time = True
    context_dict = {'estates':estates , 'visits':visits, 'last_visit': last_visit}
    request.session['visits'] = visits
    if reset_last_visit_time:
        request.session['last_visit'] = str(datetime.now())    
    response = render(request, 'agency/index.html', context_dict)
    return response


def category(request, category_name_slug):
    category = Category.objects.get(slug=category_name_slug)
    estates = Estate.objects.filter(category=category)
    context_dict = {'estates': estates, 'category': category}
    return render(request, 'agency/category.html', context_dict)

def search(request):
    errors = [ ]
    if 'price' and 'code' and 'room' in request.GET:
        q = request.GET['price']
        w = request.GET['code']
        r = request.GET['room']
        if not q and not w and not r:
            errors.append('Enter a search term.')
        else:
            newestate = Estate.objects.filter(price__icontains=q, code__icontains=w, room__icontains=r)
            return render_to_response('agency/search_results.html',
            {'newestate': newestate, 'q': q, 'w':w, 'r':r,})
    return render_to_response('agency/search_form.html', {'errors': errors})


class EstateDetailView(DetailView):
    model = Estate
    
    def count(self, **kwargs):

        visits =self.request.session.get('visits')
        if not visits:
            visits = 0
        reset_last_visit_time = False

        last_visit = self.request.session.get('last_visit')
        if last_visit:
            last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")
            if (datetime.now() - last_visit_time).days > 0:
            # ...reassign the value of the cookie to +1 of what it was before...
                visits = visit
                s + 1
            # ...and update the last visit cookie, too.
                reset_last_visit_time = True
        else:
        # Cookie last_visit doesn't exist, so create it to the current date/time.
            reset_last_visit_time = True
        context_dict = {}
        context_dict['last_visit'] = last_visit
        context_dict['visits'] = visits
        self.request.session['visits'] = visits
        if reset_last_visit_time:
            self.request.session['last_visit'] = str(datetime.now())
        response = render(request, 'agency/estate_detail.html', context_dict)
        return response


class PageDetailView(DetailView):
    model = Page



from typing import Any
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Actor,ActorMovie,Movie
from django.urls.base import reverse
from django.http import HttpResponse
from django.db.models import Q
import json
# Create your views here.



# class ActorDetail(DetailView):
#     model = Actor
#     template_name = 'actor_detail.html'

class ActorList(ListView):
    model = Actor
    template_name = 'actor_list.html'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ActorList, self).get_context_data(**kwargs)          
        context['core_actor_url'] = reverse('core:get_actor_json_users')       
        return context


def actor_ajax_request(request):
    data = []
    actor_movie_leading_role_count = 0        
    try:
        actor_query = Actor.objects.all()
        draw = request.GET.get('draw')        
        search_value = request.GET.get('search[value]')        
        filter_value = request.GET.get('filter[filter_value]')                       
        from_ = int(request.GET.get('start'))    
        limit = int(request.GET.get('length'))
                
        if filter_value is not None or filter_value != "":  
            if filter_value == 'all' or filter_value == '':
                actor_query = Actor.objects.all()                
            else:
                actor_query = actor_query.filter(gender__iexact=filter_value)        

        if search_value is not None or search_value != "":
            actor_query = actor_query.filter(Q(full_name__icontains=search_value) | Q(popularity_score__icontains=search_value))

        for i in actor_query[from_ : from_+limit]:            
            actor_movie_count = ActorMovie.objects.filter(actor_id = i.id).count()
            actor_movie_leading_role_count = ActorMovie.objects.filter(actor_id = i.id , is_lead=True).count()                        
            data.append([
                        
                        # f'<a href={reverse("core:actor_detail", kwargs={"slug":i.id})} target="_self">{i.full_name}</a>' ,
                        i.full_name,                      
                        i.age,
                        i.gender,
                        actor_movie_count,
                        actor_movie_leading_role_count,
                        float(i.popularity_score)
                        ])        
        response = {
            "draw": draw,
            "recordsTotal": actor_query.count(),
            "recordsFiltered": actor_query.count(),
            "data": data
        }
    except Exception as e:
        response = {
            "draw": 0,
            "recordsTotal": 0,
            "recordsFiltered": 0,
            "data": [],
            "error_message": str(e)      
        }
    result = json.dumps(response, default=str)    
    return HttpResponse(result, content_type='application/json')

class MovieList(ListView):
    model = Movie
    template_name = 'movie_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MovieList, self).get_context_data(**kwargs)        
        context['core_movie_url'] = reverse('core:get_movie_json_users')       
        return context
    
def movie_ajax_request (request):
    data = []        
    try:
        movie_query = Movie.objects.all()            
        draw = request.GET.get('draw')        
        search_value = request.GET.get('search[value]')       
        filter_value = request.GET.get('filter[filter_value]')         
        from_ = int(request.GET.get('start'))    
        limit = int(request.GET.get('length')) 
        actress_name = ''
        actor_name = ''

        if filter_value is not None or filter_value != "":
            movie_query = movie_query.filter(imdb_rating__icontains=filter_value)
    

        if search_value is not None or search_value!='':            
            movie_query = movie_query.filter(Q(title__icontains=search_value) | Q(imdb_rating__icontains=search_value))            
        
        for i in movie_query[from_:from_+limit]: 
            actor_name =  ActorMovie.objects.filter(movie_id = i.id, actor_id__gender__icontains='male',movie_id__title=i.title).values('actor_id__full_name')
            actress_name = ActorMovie.objects.filter(movie_id = i.id, actor_id__gender__icontains='female',movie_id__title=i.title).values('actor_id__full_name')   
            if actress_name:
                actress_name = actress_name[0]['actor_id__full_name']
            if actor_name:                                         
                actor_name = actor_name[0]['actor_id__full_name']
            data.append([i.title,i.imdb_rating,actor_name,actress_name])        

        response = {
            "draw": draw,
            "recordsTotal": movie_query.count(),
            "recordsFiltered": movie_query.count(),
            "data": data
        }
    except Exception as e:
        response = {
            "draw": 0,
            "recordsTotal": 0,
            "recordsFiltered": 0,
            "data": [],
            "error_message": str(e)     
        }

    result = json.dumps(response, default=str)    
    return HttpResponse(result, content_type='application/json')







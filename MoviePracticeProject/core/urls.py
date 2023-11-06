from django.urls import path,include
from .views import ActorList,actor_ajax_request,movie_ajax_request,MovieList#,ActorDetail

urlpatterns = [    
    path('', ActorList.as_view(), name='movie'),
    path('get_actor_json_users/',
         actor_ajax_request, name='get_actor_json_users'),
     # path('<slug>/',ActorDetail.as_view(), name='actor_detail'),

    path('movie/', MovieList.as_view(), name='movie'),
    path('get_movie_json_users/',
         movie_ajax_request, name='get_movie_json_users'),
    
]

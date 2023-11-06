from django.contrib import admin
from .models import Actor,Movie,ActorMovie

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title','description','date','imdb_rating')
    list_filter = ['title','date','imdb_rating']
    search_fields = ['title','imdb_rating']
    

class ActorAdmin(admin.ModelAdmin):
    list_display = ('full_name','gender','age')
    list_filter = ['full_name','gender','age']
    search_fields = ['full_name','gender','age']


class ActorMovieAdmin(admin.ModelAdmin):
    list_display = ('actor_id','movie_id','is_lead')    


    

admin.site.register(Movie,MovieAdmin)
admin.site.register(Actor,ActorAdmin)
admin.site.register(ActorMovie,ActorMovieAdmin)

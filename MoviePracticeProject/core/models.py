from django.db import models
import uuid

# Create your models here.

class Movie(models.Model):
    id = models.UUIDField( primary_key = True, default = uuid.uuid4, editable = False) 
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField(name="date")
    imdb_rating = models.FloatField()

    def __str__(self) -> str:
        return self.title



class Actor(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    id = models.UUIDField( primary_key = True, default = uuid.uuid4, editable = False)     
    full_name = models.CharField(max_length=50)    
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    age =  models.IntegerField()
    popularity_score = models.DecimalField(max_digits=3, decimal_places=1,null=True,blank=True)


    def __str__(self) -> str:
        return self.full_name
    
    class Meta:
        ordering= ['age']
        

class ActorMovie(models.Model):
    id = models.UUIDField( primary_key = True, default = uuid.uuid4, editable = False) 
    actor_id = models.ForeignKey(Actor,on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie,on_delete=models.CASCADE)
    is_lead = models.BooleanField()



from django.db import models
from django.utils.safestring import mark_safe


class Filme(models.Model):

    movie_title = models.CharField(max_length=50)
    r_date = models.DateField('date released')
    synopsis = models.TextField()
    raitings = models.FloatField()
    poster = models.ImageField(upload_to = "filmes", blank = True, null= True)
    genre = models.CharField(max_length= 255, null= True, blank= True)
    

    
    def __str__(self):
        return self.movie_title

    def image_tag(self):
        if self.poster:
            return mark_safe(f'<img src="{self.poster.url}" style="width: 100px; height:125px;" />')
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'
    

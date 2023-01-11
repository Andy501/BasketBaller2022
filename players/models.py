
from tabnanny import verbose
from django.db import models
from django.urls import  reverse


#https://medium.com/django-rest/django-model-relations-63709bccb72d
#https://docs.djangoproject.com/en/4.0/topics/db/examples/one_to_one/



#TODO V2: DB flat file 2013 MIAMI HEAT Starting 5 saved to remote DB, Local Test DB
class Players(models.Model):
    f_name = models.CharField(verbose_name='First Name', max_length = 50, default="Faux")
    l_name = models.CharField(verbose_name='Last Name', max_length=50, default="Doe")
    number = models.IntegerField(verbose_name='Jersey Number', default=0)
    #shoe = models.URLField()
    #picture = models.ImageField(verbose_name='Player Image', max_length=500, blank=True, null=True)#Images\Player_Images\no_image_available.jpg"

    class Meta:
        db_table = "Ballers"
        verbose_name_plural = "Players"
      

    def __str__(self):
        return f'{self.f_name} {self.l_name} {self.number}'

    def get_url(self):
        return reverse('players:p_details', args=[self.id])



class Points(models.Model):
    player = models.OneToOneField(Players, on_delete=models.CASCADE,  primary_key=True)
    num_games = models.IntegerField()
    tot_points = models.IntegerField( default=0) 
    ppg = models.FloatField(verbose_name='PPG', default=0)
    

    class Meta:
        db_table = "Hoops"
        verbose_name_plural = "Points"
        

    def __str__(self):
        return f'{self.player.f_name} {self.player.l_name} ppg: {self.ppg}'



#one to one because I only want the latest single tweet. New tweets will overwrite the old. per a predefined backend schedule.
#Intentionally not using available twitter API.
#only tweets text
class Tweety(models.Model):
    player = models.OneToOneField(Players, on_delete=models.CASCADE)
    twitter_handle = models.CharField(max_length=100)
    tweet_body = models.CharField(max_length=500)


    class Meta:
        verbose_name_plural = "Tweet"

    def __str__(self):
        return f'{self.player.f_name} {self.twitter_handle}'




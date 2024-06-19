from django.db import models

# Created models 

class Userdetail(models.Model):
    user_id=models.BigAutoField(primary_key=True)
    username=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=30)

class urlModel(models.Model):
    longurl = models.CharField(max_length=5000)
    shorturl = models.CharField(max_length=7)
    count = models.IntegerField(default=0)
    url_user_id=models.ForeignKey(Userdetail,on_delete=models.SET_NULL,null=True,blank=True)
    def __str__(self) -> str:
        return self.shorturl
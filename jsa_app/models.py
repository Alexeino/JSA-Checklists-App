from django.db import models
from django.contrib.auth.models import User
checklist_choices = (
    ('Yes','Y'),
    ('No','N'),
    ('NA','NA')
)

class Question(models.Model):
    title = models.CharField(max_length=200)
    choice = models.CharField(max_length=30,null=True,blank=True)
    
    def __str__(self):
        return self.title
    
class Checklist(models.Model):
    title = models.CharField(max_length=200)
    questions = models.ManyToManyField(Question)
    
    def __str__(self):
        return self.title
    
class JSAChecklist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    checklist = models.ForeignKey(Checklist,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.username} submitted {self.checklist.title}"
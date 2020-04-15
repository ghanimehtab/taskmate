from django.db import models


class TaskList(models.Model):
    Class_name=models.CharField(max_length=50,default="")
    subject_name=models.CharField(max_length=100,default="")
    chapter_name=models.CharField(max_length=300)
    teacher_name=models.CharField(max_length=100,default="")
    link_name = models.URLField(max_length=200,default="")


    def __str__(self):
        return self.chapter_name + "-"+str(self.subject_name)+"-"+str(self.Class_name)


    
    
    
    
    
    
    # Create your models here.

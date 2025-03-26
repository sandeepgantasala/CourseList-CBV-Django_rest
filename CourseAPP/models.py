from django.db import models

# Create your models here.
class Course(models.Model):
    id=models.IntegerField(primary_key=True)
    course_name=models.CharField(max_length=100)
    discription=models.TextField(max_length=500)
    ratings = models.DecimalField(max_digits=5, decimal_places=2)


    def __str__(self):
        return self.course_name+self.discription+self.ratings+self.id
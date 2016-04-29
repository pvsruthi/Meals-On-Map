from django.db import models

# Create your models here.
'''
Reference model classes
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
 '''

class Producer(models.Model):

    def __unicode__(self):              #To display all Producer objects with their names
        return self.name


    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    zipcode = models.IntegerField(default=0)

class Dish(models.Model):
    
    def __unicode__(self):           #To display all Dish objects with their names    
        return self.name

    producer = models.ForeignKey(Producer)
    name = models.CharField(max_length=200)
    rating = models.IntegerField(default=0)
    date = models.DateField('date available')

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.text import slugify

from horses.models import Horse
from showing.models import Discipline

#Types of training actions
class TrainingAction(models.Model):
	training = models.CharField(max_length=50)
	discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.training
	
#Training sessions
class TrainingSession(models.Model):
	type_training = models.ForeignKey(TrainingAction, on_delete=models.CASCADE)
	horse = models.ForeignKey(Horse, on_delete=models.CASCADE)
	value = models.IntegerField()
	timestamp   = models.DateTimeField(auto_now_add=True)

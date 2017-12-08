from django.db import models
from horses.models import Horse

#Disciplines
class Discipline(models.Model):
	discipline = models.CharField(max_length=50)

#Classes for individual disciplines
class ClassName(models.Model):
	discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
	class_name = models.CharField(max_length=50)

#Individual events
class Show(models.Model):
	event = models.CharField(max_length=225,unique=True)
	date = models.DateField()
	run = models.BooleanField(default=False)
	
#Event classes
class ShowClass(models.Model):
	event = models.ForeignKey(Show, on_delete=models.CASCADE)
	class_name = models.ForeignKey(ClassName, on_delete=models.CASCADE)

#Event entries
class ShowEntry(models.Model):
	event = models.ForeignKey(Show, on_delete=models.CASCADE)
	enrty_class = models.ForeignKey(ShowClass, on_delete=models.CASCADE)
	horse = models.ForeignKey(Horse, on_delete=models.CASCADE)
	placing = models.IntegerField(default=0)
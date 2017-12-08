import random
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView

from rest_framework import permissions
from .api.permissions import IsOwnerOrAdminOrReadOnly

from .forms import HorseCreateForm
from .models import Horse, Breed, Color, Stat, Gene, HorseStat, HorseGene

class HorseList(ListView):
    model = Horse
    template_name = 'horse_list.html'  # Default: <app_label>/<model_name>_list.html
    context_object_name = 'horse_list'  # Default: object_list
    title = "Horses"
    paginate_by = 10
    queryset = Horse.objects.all()  # Default: Model.objects.all()

class HorseCreate(CreateView):
	form_class = HorseCreateForm
	model = Horse
	template_name = "form.html"
	
	def get_context_data(self, **kwargs):
         context = super(HorseCreate, self).get_context_data(**kwargs)
         #If you dont call 'super', you wont have the context processor varibles
         #  like 'user'
         context['title'] = "Create Horse" # you can add template variables!
         return context # dont forget to return it!

	def form_valid(self, form):
		 form.instance.owner = self.request.user
		 form.instance.age = '3'

		 ## Get the breed info
		 breed = Breed.objects.get(breed=form.instance.breed)
		 min_height = breed.height_min
		 max_height = breed.height_max
		 form.instance.height = random.uniform(min_height,max_height)
		 form.save()
		 
		 ## Get the stats
		 stat_list = Stat.objects.all()
		 
		 ## Create a new horse-stat relation for each stat
		 for stat in stat_list:
		 	if stat.name == 'Health':
		 		HorseStat.objects.create(horse=form.instance,stat=stat,value=100)
		 	elif stat.name == 'Fitness':
		 		HorseStat.objects.create(horse=form.instance,stat=stat,value=10)
		 	else:
		 		HorseStat.objects.create(horse=form.instance,stat=stat,value=random.uniform(25, 75))
		 
		 ## Get the genes
		 gene_list = Gene.objects.all()
		 
		 # Get the genes for the breed
		 breed_gene_list = Gene.objects.filter(breed__breed=form.instance.breed)
		 
		 ## Create a new horse-gene relation for each stat
		 ## If the breed has the gene, create a randomized genotype with a mix of dominant and recessive.
		 for gene in gene_list:
		 	if gene in breed_gene_list:
		 		HorseGene.objects.create(horse=form.instance,gene=gene,genotype=random.randrange(0, 3))
		 	else:
				## If the breed doesn't have the gene, create a recessive genotype
		 		HorseGene.objects.create(horse=form.instance,gene=gene,genotype=0)

		 ## Phenotype
		 horse_color = form.instance.get_phenotype()
		 form.instance.color = horse_color

		 ## Remove credit or $$ from user account		 
		 
		 ## Save the horse and related objects
		 return super(HorseCreate, self).form_valid(form)
		 
	def form_invalid(self, form):
		 return self.render_to_response(self.get_context_data(form=form))
	
class HorseDetail(DetailView):
	model = Horse
	template_name = 'horse_detail.html' # Default: <app_label>/<model_name>_list.html
	
def horse_update(request, slug=None):
	return render(request, "horse_list.html", context)
	
def horse_delete(request, slug=None):
	return render(request, "horse_list.html", context)
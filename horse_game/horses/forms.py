from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    )

from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, ButtonHolder, Fieldset
from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper

from .models import Horse, Breed, Color
    
User = get_user_model()

class HorseCreateForm(forms.ModelForm):
	name = forms.CharField(
        max_length=Horse._meta.get_field('name').max_length
    )
    
	def __init__(self, *args, **kwargs):
		 super(HorseCreateForm, self).__init__(*args, **kwargs)
			 
		 # If you pass FormHelper constructor a form instance
		 # It builds a default layout with all its fields
		 self.helper = FormHelper(self)
	        
		 # You can dynamically adjust your layout
		 self.helper.layout = Layout(
			 	Div(
				 	Fieldset(
					 	'Create a new horse by filling out the information below.',
					 	'name',
					 	'breed',
					 	'gender',
				 	), 
				 	css_class="row"),
			 	Div(
		 			FormActions(Submit('save', 'Create')),
		 			css_class="row"
		 		)
		 	)
		 self.request = kwargs.pop('request', None)
		 return super(HorseCreateForm, self).__init__(*args, **kwargs)
		 
	class Meta:
		 model = Horse
		 fields = ['name', 'breed', 'gender']
	
		# def save(self):
	# 	horse = super(HorseCreateForm, self).save(commit=False)
	# 	horse.owner = self.user
	# 	horse.age = '3'

	# 	## Get the breed info
	# 	breed = Breed.objects.get(breed=horse.breed)
	# 	min_height = breed.height_min
	# 	max_height = breed.height_max
	# 	horse.height = random.uniform(min_height,max_height)

	# 	horse.save()
		
	# 	## Get the stats
	# 	stat_list = Stat.objects.all()
		 
	# 	## Create a new horse-stat relation for each stat
	# 	for stat in stat_list:
	# 		if stat.name == 'Health':
	# 			HorseStat.objects.create(horse=horse,stat=stat,value=100)
	# 		elif stat.name == 'Fitness':
	# 			HorseStat.objects.create(horse=horse,stat=stat,value=10)
	# 		else:
	# 			HorseStat.objects.create(horse=horse,stat=stat,value=random.uniform(25, 75))

	# 	## Get the genes
	# 	gene_list = Gene.objects.all()

	# 	# Get the genes for the breed
	# 	breed_gene_list = Breed.objects.filter(breed=breed)

	# 	## Create a new horse-gene relation for each stat
	# 	## If the breed has the gene, create a randomized genotype with a mix of dominant and recessive.
	# 	for gene in gene_list:
	# 		if gene in breed_gene_list:
	# 			HorseGene.objects.create(horse=horse,gene=gene,genotype=random.randrange(0, 2))
	# 		else:
	# 			## If the breed doesn't have the gene, create a recessive genotype
	# 			HorseGene.objects.create(horse=horse,gene=gene,genotype=0)

		
	# 	m2m.save()
	# 	return horse
	
	def clean_name(self):
		name = self.cleaned_data['name']
		horse_exists = Horse.objects.filter(name=name).exists()
		
		if horse_exists:
			raise forms.ValidationError(u"This horse name already belongs to another horse!")
		
		return name
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.text import slugify
from itertools import chain

class Breed(models.Model):
	#Defines and stores breeds of horse
	breed = models.CharField(max_length=50)
	genes = models.ManyToManyField('Gene')
	height_min = models.IntegerField(default=13)
	height_max = models.IntegerField(default=17)
	
	def __str__(self):
		return self.breed

class Color(models.Model):
	color = models.CharField(max_length=50)

	def __str__(self):
		return self.color

GENE_EXPRESSION = (
	(0, 'Recessive'),
	(1, 'Dominant'),
)

GENE_TYPE = (
	('base', 'Base'),
	('dilution', 'Dilution'),
	('modifier', 'Modifier'),
	('pattern', 'Pattern'),
)
		
class Gene(models.Model):
	#Defines genes that horses can have
	name = models.CharField(max_length=30)
	location = models.CharField(max_length=10,default='None')
	symbol = models.CharField(max_length=4)
	gene_type = models.CharField(
		max_length=30,
		choices = GENE_TYPE,
		default = 0,
		)
	expression = models.IntegerField(
		choices = GENE_EXPRESSION,
		)
		
	def __str__(self):
		return self.name
  
STAT_TYPE = (
	(0, 'Fixed'),
	(1, 'Flexible'),
) 	

class Stat(models.Model):
	#Defines specific stats that horses can have
	name = models.CharField(max_length=50)
	stat_type = models.IntegerField(
		choices = STAT_TYPE,
		)
	hidden = models.BooleanField(default=False)
	
	def __str__(self):
		return self.name

GENDERS = (
	('stallion', 'Stallion'),
	('mare', 'Mare'),
	('gelding', 'Gelding'),
)

class Horse(models.Model):
	"""
	Horse Model
	Defines the attributes of a horse
	"""
	name = models.CharField(max_length=255,unique=True)
	age = models.IntegerField()
	breed = models.ForeignKey(Breed, default=1, on_delete=models.CASCADE)
	color = models.CharField(max_length=225)
	owner = models.ForeignKey('auth.User', related_name='horses', on_delete=models.CASCADE,default=1)
	gender = models.CharField(
		max_length=25,
		choices = GENDERS,
		default = 'stallion'
		)
	height = models.IntegerField(default=15)
	genes = models.ManyToManyField('Gene', through='HorseGene', related_name='gene_expression')
	stats = models.ManyToManyField('Stat', through='HorseStat', related_name='stats')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return self.name
		
	def get_absolute_url(self):
		return reverse('horses:detail', kwargs={"pk": self.pk})

	def get_admin_url(self):
		return reverse('admin:horses_horse_change', args=(self.pk,))

	@property
	def visible_stats(self):
		qs = self.horse_stat.filter(stat__hidden=False)
		return qs
		
	def show_owner_url(self):
		return reverse("users:detail", kwargs={"username": self.owner})
		
	def show_create_url(self):
		return reverse('horses:create')

	def get_phenotype(self):
		qs = self.genotype.all().values('gene__name','genotype')
		horse_color = 'Color'
		genotype = {} 

		for gene in qs:
			gene_name = gene['gene__name'].lower()
			genotype[gene_name] = gene['genotype']

		
		# Is the horse gray? If it’s gray it will always be gray so we can skip to patterns. 
		if genotype['grey'] > 0:
			horse_color = 'Grey'
		# Is the horse not gray? Move on to base colors. 
		else:

			# If two recessive genes, e.g., chestnut, check the chestnut colors. 
			if genotype['grey'] == 0 and genotype['base'] == 0:
		
				# Does the horse have a dominant cream gene?
				if genotype['cream'] > 0:

					if genotype['cream'] == 1:
						horse_color = 'Palomino'
					elif genotype['cream'] == 2 or genotype['cream'] == 3:
						horse_color ='Cremello'
					elif genotype['cream'] == 4:
						horse_color = 'Pearl Chestnut'
					
				#If there's no cream gene, move on to champagne.
				elif genotype['champagne'] > 0:
					horse_color = 'Gold Champagne'
				#If no dominant champagne allele, check for flaxen.
				else:
					if genotype['flaxen'] > 0:
						horse_color = 'Flaxen Chestnut'
					else:
						horse_color = 'Chestnut'

			#If one or two dominant base alleles, check for bay genes. 
			else:

				#If there's dominant allele at bay/agouti, do the bay colors.
				if genotype['bay'] > 0:

					# Does the horse have a dominant cream gene?
					if genotype['cream'] > 0:
						if genotype['cream'] == 1:
							horse_color = 'Buckskin'
						elif genotype['cream'] == 2 or genotype['cream'] == 3:
							horse_color ='Perlino'
						elif genotype['cream'] == 4:
							horse_color = 'Pearl Bay'
				
					#If there's no cream gene, move on to champagne.
					elif genotype['champagne'] > 0:
						if genotype['bay'] < 6:
							horse_color = 'Amber Champagne'
						else:
							horse_color = 'Sable Champagne'
					else:
						horse_color = 'Bay'
				
				#If there's two recessive alleles at bay/agouti, black colors.
				else:

					# Does the horse have a dominant cream gene?
					if genotype['cream'] > 0:
						if genotype['cream'] == 1:
							horse_color = 'Smokey Black'
						else:
							horse_color ='Smokey Cream'
					#If there's no cream gene, move on to champagne.
					elif genotype['champagne'] > 0:
						horse_color = 'Classic Champagne'
					else: 
						horse_color = 'Black'

				#If the horse is black or bay, check for silver. 
				if genotype['base'] > 0 and genotype['silver'] > 0 and genotype['cream'] == 0 and genotype['champagne'] == 0:
					horse_color = 'Silver '+ horse_color
				else:
					pass


			if genotype['dun'] > 0:
				if horse_color == 'Black':
					horse_color = 'Grullo'
				elif horse_color == 'Chestnut':
					horse_color = 'Red Dun'
				else:
					horse_color = horse_color + ' Dun'
	
		#Patterns
		#If the horse has a dominant gene at the KIT locus...
		# 0: double recessive, 1: dominant + recessive, 2: double dominant
		#Dominant White
		if genotype['white0'] > 0 or genotype['white5'] > 0 or genotype['white10'] > 0 or genotype['white20'] > 0:
			horse_color = horse_color + ' White'
		else:
			pass

		#Tobiano
		if genotype['tobiano'] > 0:
			horse_color = horse_color + ' Tobiano'
		else:
			pass

		#Sabino
		if genotype['sabino1'] > 0 or genotype['sabino2'] > 0:
			horse_color = horse_color + ' Sabino'
		else:
			pass

		#Splash
		if genotype['splash'] > 0 or genotype['splash2'] > 0:
			horse_color = horse_color + ' Splash'
		else:
			pass

		#Frame
		if genotype['frame'] > 0:
			horse_color = horse_color + ' Frame'
		else:
			pass

		#Roan
		if genotype['roan'] > 0:
			horse_color = horse_color + ' Roan'
		else:
			pass

		#Pangare
		if genotype['grey'] == 0 and genotype['pangare'] > 0:
			horse_color = horse_color + ' Mealy'
		else:
			pass

		if genotype['roan'] == 0 and genotype['rabicano'] > 0:
			horse_color = horse_color + ' Rabicano'
		else:
			pass

		return horse_color

class HorseGene(models.Model):
	horse = models.ForeignKey(Horse, related_name='genotype')
	gene = models.ForeignKey(Gene, related_name='genotype')
	genotype = models.IntegerField()
	
	class Meta:
		unique_together = ('horse', 'gene')
	
	def show_genotype_str(self):
		if self.genotype == 0:
			return self.gene.symbol.lower() + self.gene.symbol.lower()
		
		elif self.genotype == 1:
			return self.gene.symbol + self.gene.symbol.lower()
		
		elif self.genotype == 2:
			return self.gene.symbol + self.gene.symbol
		else:
			pass

	def get_base_phenotype(self):
		if self.gene.gene_type == 'base':
			if self.genotype > 0:
				return 'black'
			else:
				return 'chestnut'
		else:
			pass

	def get_modifier_phenotype(self,color):
		if self.gene.gene_type == 'modifier':
			if self.gene.name == 'gray' and self.genotype > 0:
				return 'gray'
			elif self.gene.name == 'bay' and self.genotype > 0 and color != 'chestnut':
				return 'bay'
			elif self.gene.name == 'cream' and self.genotype > 0:
				if color == 'bay':
					if self.genotype == 1:
						return 'buckskin'
					elif self.genotype == 2 or self.genotype > 0 == 3:
						return 'perlino'
					else:
						return 'pearl bay'

				elif color == 'chestnut':
					return 'chestnut'
				else:
					return 'black'
			elif self.gene.name == 'champagne' and self.genotype > 0:
				return 'champagne'
			else:
				return color
		else:
			return color

# What if we do these functions in the order they need to go in and we pass the current color into each one?


class HorseStat(models.Model):
	horse = models.ForeignKey(Horse,  related_name='horse_stat')
	stat = models.ForeignKey(Stat,  default=50, related_name='horse_stat')
	value = models.FloatField(max_length=3)
	
	class Meta:
		unique_together = ('horse', 'stat')

	
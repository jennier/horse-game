from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from horses.models import Horse, Breed, Color, Gene, HorseGene


# class GetAllHorsesTest(TestCase):
# 
#     def setUp(self):
#         self.horse1 = Horse.objects.create(
#                              id = 1, name='Horse', age=3, breed='Arabian', color='Black')
#         self.horse2 = Horse.objects.create(
#                              id = 2, name='Horse 2', age=6, breed='Thoroughbred', color='Bay')
#         self.horse3 = Horse.objects.create(
#                              id = 3, name='Horse 3', age=12, breed='Quarter Horse', color='Grey')
# 
#     def test_get_all_horses(self):
#         response = self.client.get(reverse('horse-list'))
#         horses = Horse.objects.all()
#         serializer = HorseSerializer(horses, many=True)
#         self.assertEqual(response.data, serializer.data)
#         self.assertEqual(response.status_code, 200)
# 
# 
#     def test_get_valid_single_horse(self):
#         response = self.client.get(reverse('horse-detail',kwargs={'pk': self.horse1.pk}))
#         horse = Horse.objects.get(pk=self.horse1.pk)
#         serializer = HorseSerializer(horse)
#         self.assertEqual(response.data, serializer.data)
#         self.assertEqual(response.status_code, 200)
#                                            
#     def test_get_invalid_single_horse(self):
#        response = self.client.get(reverse('horse-detail',kwargs={'pk': 30}))
#        self.assertEqual(response.status_code, 404)

class M2MThroughTest(TestCase):
	
	def setUp(self):
		self.breed1 = Breed.objects.create(breed = 'Arabian')
		self.color1 = Color.objects.create(color = 'Bay')
		self.owner1 = User.objects.create(username = 'admin')
		
		#Create a horse
		self.horse1 = Horse.objects.create(
			name = 'Horse 1', age = 3, gender = 'Mare', height = '15', owner = self.owner1
		)
		
		#Create some genes, where 0 = recessive and 1 = dominant
		self.gene1 = Gene.objects.create(name = 'gene1', symbol = 'G', expression = '0')
		self.gene2 = Gene.objects.create(name = 'gene1', symbol = 'E', expression = '1')
		self.gene3 = Gene.objects.create(name = 'gene1', symbol = 'F', expression = '1')
		
		HorseGene.objects.create(gene=self.gene1, horse=self.horse1, genotype='00')
		HorseGene.objects.create(gene=self.gene2, horse=self.horse1, genotype='01')
		HorseGene.objects.create(gene=self.gene3, horse=self.horse1, genotype='11')
		
	def test_gene_expression(self):
		#What genes does horse1 have?
		horse1_genes = Gene.objects.filter(gene_expression=self.horse1)
		self.assertEqual(list(horse1_genes), [self.gene1, self.gene2, self.gene3])

class HorseCreateTests(TestCase):

	def setUp(self):
		self.breed1 = Breed.objects.create(breed = 'Arabian')
		self.owner1 = User.objects.create(username = 'admin')
		
		self.gray = Gene.objects.create(name = 'gray', symbol = 'G', expression = '0', gene_type='modifier')
		self.base = Gene.objects.create(name = 'base', symbol = 'E', expression = '0', gene_type='base')
		self.bay = Gene.objects.create(name = 'bay', symbol = 'B ', expression = '0', gene_type='modifier')
		self.cream = Gene.objects.create(name = 'cream', symbol = 'Cr', expression = '0', gene_type='modifier')
		self.champagne = Gene.objects.create(name = 'champagne', symbol = 'Ch', expression = '0', gene_type='modifier')
		self.flaxen = Gene.objects.create(name = 'flaxen', symbol = 'F', expression = '0')
		self.silver = Gene.objects.create(name = 'silver', symbol = 'S', expression = '0')
		self.dun = Gene.objects.create(name = 'dun', symbol = 'D', expression = '0')
		self.w0 = Gene.objects.create(name = 'w0', symbol = 'W0', expression = '0')
		self.w5 = Gene.objects.create(name = 'w5', symbol = 'W5', expression = '0')
		self.w10 = Gene.objects.create(name = 'w10', symbol = 'W10', expression = '0')
		self.w20 = Gene.objects.create(name = 'w20', symbol = 'W20', expression = '0')
		self.tobiano = Gene.objects.create(name = 'tobiano', symbol = 'T', expression = '0')
		self.roan = Gene.objects.create(name = 'roan', symbol = 'R', expression = '0')
		self.splash1 = Gene.objects.create(name = 'splash1', symbol = 'Sp1', expression = '0')
		self.splash2 = Gene.objects.create(name = 'splash2', symbol = 'Sp2', expression = '0')
		self.sabino1 = Gene.objects.create(name = 'sabino1', symbol = 'S1', expression = '0')
		self.sabino2 = Gene.objects.create(name = 'sabino2', symbol = 'S2', expression = '0')
		self.frame = Gene.objects.create(name = 'frame', symbol = 'Fr', expression = '0')
		self.pangare = Gene.objects.create(name = 'pangare', symbol = 'P', expression = '0')
		self.rabicano = Gene.objects.create(name = 'rabicano', symbol = 'Ra', expression = '0')
	
	def create_valid_horse(self):
		response = self.client.post('/', data={'name': 'Horse 1', 'gender': 'mare', 'breed': 'Arabian'})
		
	def create_invalid_horse(self):
		pass

class PhenotypeTests(TestCase):

	def setUp(self):
		self.breed1 = Breed.objects.create(breed = 'Arabian')
		self.color1 = Color.objects.create(color = 'Bay')
		self.owner1 = User.objects.create(username = 'admin')
		
		#Create a horse
		self.horse1 = Horse.objects.create(
			name = 'Horse 1', age = 3, gender = 'Mare', height = '15', owner = self.owner1, color = self.color1
		)

		self.grey = Gene.objects.create(name = 'grey', symbol = 'G', expression = '0', gene_type='modifier')
		self.base = Gene.objects.create(name = 'base', symbol = 'E', expression = '0', gene_type='base')
		self.bay = Gene.objects.create(name = 'bay', symbol = 'B ', expression = '0', gene_type='modifier')
		self.cream = Gene.objects.create(name = 'cream', symbol = 'Cr', expression = '0', gene_type='modifier')
		self.champagne = Gene.objects.create(name = 'champagne', symbol = 'Ch', expression = '0', gene_type='modifier')
		self.flaxen = Gene.objects.create(name = 'flaxen', symbol = 'F', expression = '0')
		self.silver = Gene.objects.create(name = 'silver', symbol = 'S', expression = '0')
		self.dun = Gene.objects.create(name = 'dun', symbol = 'D', expression = '0')
		self.w0 = Gene.objects.create(name = 'white0', symbol = 'W0', expression = '0')
		self.w5 = Gene.objects.create(name = 'white5', symbol = 'W5', expression = '0')
		self.w10 = Gene.objects.create(name = 'white10', symbol = 'W10', expression = '0')
		self.w20 = Gene.objects.create(name = 'white20', symbol = 'W20', expression = '0')
		self.tobiano = Gene.objects.create(name = 'tobiano', symbol = 'T', expression = '0')
		self.roan = Gene.objects.create(name = 'roan', symbol = 'R', expression = '0')
		self.splash1 = Gene.objects.create(name = 'splash', symbol = 'Sp1', expression = '0')
		self.splash2 = Gene.objects.create(name = 'splash2', symbol = 'Sp2', expression = '0')
		self.sabino1 = Gene.objects.create(name = 'sabino1', symbol = 'S1', expression = '0')
		self.sabino2 = Gene.objects.create(name = 'sabino2', symbol = 'S2', expression = '0')
		self.frame = Gene.objects.create(name = 'frame', symbol = 'Fr', expression = '0')
		self.pangare = Gene.objects.create(name = 'pangare', symbol = 'P', expression = '0')
		self.rabicano = Gene.objects.create(name = 'rabicano', symbol = 'Ra', expression = '0')

		#0: double recessive, 1: autosomal dominant, 2: homozygous dominant		HorseGene.objects.create(horse = self.horse1, gene = self.gray, genotype = '0')
		HorseGene.objects.create(horse = self.horse1, gene = self.grey, genotype = '1')
		HorseGene.objects.create(horse = self.horse1, gene = self.base, genotype = '1')
		HorseGene.objects.create(horse = self.horse1, gene = self.bay, genotype = '1')
		HorseGene.objects.create(horse = self.horse1, gene = self.cream, genotype = '1')
		HorseGene.objects.create(horse = self.horse1, gene = self.champagne, genotype = '1')
		HorseGene.objects.create(horse = self.horse1, gene = self.flaxen, genotype = '1')
		HorseGene.objects.create(horse = self.horse1, gene = self.silver, genotype = '1')
		HorseGene.objects.create(horse = self.horse1, gene = self.dun, genotype = '1')
		HorseGene.objects.create(horse = self.horse1, gene = self.w0, genotype = '1')
		HorseGene.objects.create(horse = self.horse1, gene = self.w5, genotype = '1')
		HorseGene.objects.create(horse = self.horse1, gene = self.w10, genotype = '1')
		HorseGene.objects.create(horse = self.horse1, gene = self.w20, genotype = '1')
		HorseGene.objects.create(horse = self.horse1, gene = self.tobiano, genotype = '1')
		HorseGene.objects.create(horse = self.horse1, gene = self.roan, genotype = '1')
		HorseGene.objects.create(horse = self.horse1, gene = self.splash1, genotype = '1')
		HorseGene.objects.create(horse = self.horse1, gene = self.splash2, genotype = '1')
		HorseGene.objects.create(horse = self.horse1, gene = self.sabino1, genotype = '1')
		HorseGene.objects.create(horse = self.horse1, gene = self.sabino2, genotype = '1')
		HorseGene.objects.create(horse = self.horse1, gene = self.frame, genotype = '1')
		HorseGene.objects.create(horse = self.horse1, gene = self.pangare, genotype = '1')
		HorseGene.objects.create(horse = self.horse1, gene = self.rabicano, genotype = '1')

	def test_horse_genes(self):
		horse1_genes = Gene.objects.filter(gene_expression=self.horse1)
		self.assertEqual(list(horse1_genes), [self.gene1, self.gene2, self.gene3])

	def test_phenotype(self):
		horse = Horse.objects.get(pk=self.horse1.pk)
		self.assertEqual(horse.get_phenotype(), 'chestnut')

	def test_base(self):
		gene = HorseGene.objects.get(gene=self.base)
		self.assertEqual(gene.get_base_phenotype(), 'chestnut')

	def test_modifier(self):
		gene = HorseGene.objects.get(gene=self.cream)
		self.assertEqual(gene.get_modifier_phenotype('bay'), 'chestnut')




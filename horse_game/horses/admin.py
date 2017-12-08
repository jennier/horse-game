from django.contrib import admin

# Register your models here.
from .models import Horse, Breed, Color, Gene, Stat, HorseGene, HorseStat

class HorseGeneInline(admin.TabularInline):
    model = HorseGene
    extra = 0
    
class HorseStatInline(admin.TabularInline):
    model = HorseStat
    extra = 0
    
class HorseModelAdmin(admin.ModelAdmin):
    list_display = ["name", "breed", "color", "owner"]
    list_filter = ["name", "breed", "color", "owner"]
    search_fields = ["name", "breed", "color", "owner"]
    inlines = (HorseGeneInline,HorseStatInline)
    class Meta:
        model = Horse

admin.site.register(Horse, HorseModelAdmin)

class BreedModelAdmin(admin.ModelAdmin):
    inlines = (HorseGeneInline)
    class Meta:
        model = Breed
        
admin.site.register(Breed)

admin.site.register(Color)

class GeneModelAdmin(admin.ModelAdmin):
	list_display = ['name', 'symbol','expression']
	
	class Meta:
		model = Gene
		
admin.site.register(Gene, GeneModelAdmin)

class StatModelAdmin(admin.ModelAdmin):
	list_display = ['name', 'stat_type', 'hidden']
	
	class Meta:
		model = Stat
	
admin.site.register(Stat, StatModelAdmin)
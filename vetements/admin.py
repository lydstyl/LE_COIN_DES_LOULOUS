from django.contrib import admin
from vetements.models import Article, Sex, Age, TypeCategorie, Categorie, LieuDeStockage, Exclure


# voir admin de crepes bretonne
class ArticleAdmin(admin.ModelAdmin):
	list_display = ['titre', 'sex', 'age', 'prix', 'apercu_presentation','proprietaire', 'date']
	list_filter = ['sex', 'age', 'type_categorie', 'lieu_de_stockage']
	date_hierarchy = 'date'
	ordering = ('date', )
	search_fields = ('titre', 'presentation')
	
	def apercu_presentation(self, article):
		""" 
		Retourne les 40 premiers caractères du contenu de l'article. S'il
		y a plus de 40 caractères, il faut ajouter des points de suspension.
		"""
		text = article.presentation[0:20]
		if len(article.presentation) > 20:
			return '%s...' % text
		else:
			return text

class ExclureAdmin(admin.ModelAdmin):
	list_display = ['exclure', 'id']

class SexAdmin(admin.ModelAdmin):
	list_display = ['nom', 'id']
	ordering = ('id',)
	search_fields = ('nom',)

class AgeAdmin(admin.ModelAdmin):
	list_display = ['nom', 'id']
	ordering = ('nom',)
	search_fields = ('nom',)

class TypeCategorieAdmin(admin.ModelAdmin):
	list_display = ['nom', 'id']
	ordering = ('nom',)
	search_fields = ('nom',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Sex, SexAdmin)
admin.site.register(Age, AgeAdmin)
admin.site.register(TypeCategorie, TypeCategorieAdmin)
admin.site.register(Categorie)
admin.site.register(LieuDeStockage)
admin.site.register(Exclure, ExclureAdmin)

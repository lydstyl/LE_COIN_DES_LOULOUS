from django.db import models


class Article(models.Model):
	titre = models.CharField(max_length=100)
	photo = models. ImageField(null=True, blank=True, upload_to="photos/", max_length=100)
	presentation = models.TextField(null=True, blank=True, default="En bon état")
	
	sex = models.ForeignKey('Sex')
	age = models.ForeignKey('Age')
	
	prix = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2, default=5.00)
	
	type_categorie = models.ForeignKey('TypeCategorie')
	lieu_de_stockage = models.ForeignKey('LieuDeStockage')
	proprietaire = models.CharField(null=True, blank=True, max_length=42, default="Amélie")
	
	date = models.DateTimeField(auto_now_add=True, auto_now=False, 
								verbose_name="Date de parution")

	def __str__(self):
		return "{0} (s.:{1}, a.:{2}, t.:{3})".format(self.titre, self.sex, self.age, self.type_categorie)


class Sex(models.Model):
	nom = models.CharField(max_length=30, default="Mixte")

	def __str__(self):
		return self.nom


class Age(models.Model):
	nom = models.CharField(max_length=30, default="De naissance à 3 ans")

	def __str__(self):
		return self.nom


class TypeCategorie(models.Model):
	nom = models.CharField(max_length=30, default="Pyjama")
	categorie = models.ForeignKey('Categorie')

	def __str__(self):
		return self.nom


class Categorie(models.Model):
	nom = models.CharField(max_length=30, default="Vêtement")

	def __str__(self):
		return self.nom


class LieuDeStockage(models.Model):
	nom = models.CharField(max_length=30, default="Maison Roubaix")

	def __str__(self):
		return self.nom


class Exclure(models.Model):
	exclure = models.CharField(max_length=30, default="a1ea2es2")

	def __str__(self):
		return "id {0}, exclure {1}".format(self.id, self.exclure)

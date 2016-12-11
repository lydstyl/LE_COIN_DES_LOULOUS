from django.shortcuts import render, redirect, get_object_or_404, redirect
from vetements.models import Article, Sex, Age, TypeCategorie, Exclure
from math import ceil
from vetements.forms import FormulaireExclure
from django.views.generic import TemplateView, ListView, DetailView


def formulaire_exclure(request):
	if request.method == 'POST':  # S'il s'agit d'une requête POST
		form = FormulaireExclure(request.POST)  # Nous reprenons les données

		if form.is_valid(): # Nous vérifions que les données envoyées sont valides
			envoi = True
			form.save()
			
			tous_les_objetcts_exlcure = Exclure.objects.all()
			dernier_id = len(tous_les_objetcts_exlcure)
			
			debut_url = "/articles/resultat_exclusions/"
			fin_url = Exclure.objects.get(id=str(len(tous_les_objetcts_exlcure))).exclure
			url_articles_restants = debut_url + fin_url
		
		return redirect(url_articles_restants)

	else: # Si ce n'est pas du POST, c'est probablement une requête GET
		form = FormulaireExclure()  # Nous créons un formulaire vide
	
		dico_id_exclusions = {}
		for article in Article.objects.all():
			sex_nom = article.sex
			sex_id = Sex.objects.get(nom=sex_nom).id
			sex_id = "s" + str(sex_id)
			dico_id_exclusions[sex_nom] = sex_id
			
			age_nom = article.age
			age_id = Age.objects.get(nom=age_nom).id
			age_id = "a" + str(age_id)
			dico_id_exclusions[age_nom] = age_id
			
			type_categorie_nom = article.type_categorie
			type_categorie_id = TypeCategorie.objects.get(nom=type_categorie_nom).id
			type_categorie_id = "t" + str(type_categorie_id)
			dico_id_exclusions[type_categorie_nom] = type_categorie_id
		
		return render(request, 'vetements/formulaire_exclure.html', locals())


class ResultatExclusion(ListView):
	model = Article
	context_object_name = "liste_article"
	template_name = 'vetements/resultat_exclusions.html'
	paginate_by = 2
	
	def get_queryset(self):
		chaine_exclusions = self.kwargs['chaine_exclusions']
		liste_article = Article.objects.all()
		
		liste_exclusion = chaine_exclusions.split("e")
	
		for exclusion in liste_exclusion:
			type_exclusion = exclusion[0]
			if exclusion[0] == 's':
				liste_article = liste_article.exclude(sex=exclusion[1])
			elif exclusion[0] == 'a':
				liste_article = liste_article.exclude(age=exclusion[1])
			else:
				liste_article = liste_article.exclude(type_categorie=exclusion[1])
		
		return liste_article


class TousLesArticles(ListView):
	model = Article
	context_object_name = "listouille"
	template_name = "vetements/les_articles.html"
	paginate_by = 3
	
	def get_queryset(self):
		return Article.objects.all().order_by('-date')
	
	def get_context_data(self, **kwargs):
		context = super(TousLesArticles, self).get_context_data(**kwargs)
		#return Article.objects.filter(age_id=self.kwargs['id_age'])
		# Nous ajoutons la liste des ages, sans filtre particulier
		context['nb_ref'] = len(Article.objects.all())
		return context
	#liste_article = Article.objects.order_by('-date')


class FiltreAgeView(ListView):
	model = Article
	context_object_name = "object_list" #Valeur par defaut.
	#template_name = "vetements/article_list.html" #Valeur par defaut.
	paginate_by = 2
	
	def get_queryset(self):
		# Nous récupérons le contexte depuis la super-classe
		#context = super(PtdrView, self).get_context_data(**kwargs) #Ca serait bien de faire des recherches pour mieux comprendre cette ligne.
		return Article.objects.filter(age_id=self.kwargs['id_age'])
	def get_context_data(self, **kwargs):
		# Nous récupérons le contexte depuis la super-classe
		context = super(FiltreAgeView, self).get_context_data(**kwargs) #Ca serait bien de faire des recherches pour mieux comprendre cette ligne.
		#return Article.objects.filter(age_id=self.kwargs['id_age'])
		# Nous ajoutons la liste des ages, sans filtre particulier
		context['age'] = Age.objects.all()
		return context


class LireArticle(DetailView):
	model = Article
	context_object_name = "article"
	template_name = "vetements/detail.html"

from django.conf.urls import patterns, url, include
from vetements.views import FiltreAgeView, LireArticle, ResultatExclusion, TousLesArticles
from vetements.models import Article

urlpatterns = patterns('vetements.views',
	#/articles/9
	url(r'^(?P<pk>\d+)$', LireArticle.as_view(), name='detail'),

	#/articles/?page=2
	url(r'^$', TousLesArticles.as_view(), name='pages_article'),

	#/articles/formulaire_exclure
	url(r'^formulaire_exclure$', 'formulaire_exclure', name='formulaire_exclure'),
	#/articles/resultat_exclusions/a1ea2es2?page=2
	url(r'^resultat_exclusions/(?P<chaine_exclusions>\w+)$', ResultatExclusion.as_view(), name='resultat_exclusions'),
	
	#/articles/filtre_age/3?page=2
	url(r'^filtre_age/(?P<id_age>\d+)$', FiltreAgeView.as_view(), name='filtre_age')
)

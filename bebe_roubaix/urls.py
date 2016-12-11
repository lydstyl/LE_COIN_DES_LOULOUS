from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf.urls.static import static #Ajouté pour afficher les images avec le serveur de test.
from django.conf import settings #Ajouté pour afficher les images avec le serveur de test.

from django.views.generic import TemplateView

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', TemplateView.as_view(template_name='base.html'), name='home'), #Vue générique sans présence dans views.py
	url(r'^contact$', TemplateView.as_view(template_name='contact.html'), name='contact'), #Vue générique sans présence dans views.py
	url(r'^articles/', include('vetements.urls')),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #Ajouté pour afficher les images avec le serveur de test.

from django.conf.urls import include, patterns, url
from site_details import views 

#from django.views.generic import TemplateView
#from django.core.urlresolvers import reverse

urlpatterns = patterns('', 
	url(r'^$', views.account_settings, name='account_settings'), 
)


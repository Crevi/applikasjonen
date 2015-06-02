from django.conf.urls import include, patterns, url
from site_details import views as site_details_views
from theme import views as theme_views

urlpatterns = patterns('', 
	url(r'^$', site_details_views.account_settings, name='account_settings'), 
	url(r'^(\d+)/$', theme_views.comment_details, name='comment_details'), 
	url(r'^(\d+)/adding_likes/(\d+)$', theme_views.add_likes, name='add_likes'),
	#url(r'^$', views.change_firstname, name='change_firstname'), 
	#url(r'^$', views.change_lastname, name='change_lastname'), 
	#url(r'^$', views.change_email, name='change_email'),	
)


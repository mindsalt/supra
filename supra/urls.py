from django.conf.urls.defaults import *
from django.conf import settings
from supra import settings
from supra import project

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^supra/', include('supra.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# site media
	(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '/Users/ashleyrevlett/Programs/supra5/supra/site_media'}),

    # admin
    (r'^admin/', include(admin.site.urls)),

	# project		
    (r'^project/view/$','supra.project.views.view_all'),
    (r'^project/edit/$','supra.project.events.start_edit'),
    (r'^project/edit/save/$','supra.project.events.save_edit'),
    (r'^project/create/$','supra.project.events.create_project'),
	

)

from django.conf.urls.defaults import *
from django.conf import settings
from supra import settings
from supra import project

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # admin
    (r'^admin/', include(admin.site.urls)),

	# project		
    (r'^project/view/$','supra.project.views.view_all'),
    (r'^project/edit/$','supra.project.events.start_edit'),
    (r'^project/edit/save/$','supra.project.events.save_edit'),
    (r'^project/create/$','supra.project.events.create_project'),	

)

# serve static site media in production environment
if settings.DEBUG:
    urlpatterns += patterns("django.views",
        url(r"%s(?P<path>.*)/$" % settings.MEDIA_URL[1:], "static.serve", {
            "document_root": settings.MEDIA_ROOT,
        })
    )

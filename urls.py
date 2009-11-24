from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template
from supra import settings

admin.autodiscover()

urlpatterns = patterns('',

	# site media paths
	(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
	{'document_root': settings.MEDIA_ROOT}),

    # enable admin urls
	(r'^admin/', include(admin.site.urls)),

	# home url
    (r'^$', 'supra.projecttracker.views.home_index'),	

	# project urls
    (r'^project/$', 'supra.projecttracker.views.project_index'),
    (r'^project/(?P<project_id>\d+)/$', 'supra.projecttracker.views.project_detail'),

	# company urls
    (r'^company/$', 'supra.projecttracker.views.company_index'),
    (r'^company/(?P<company_id>\d+)/$', 'supra.projecttracker.views.company_detail'),

	# person urls
    (r'^person/$', 'supra.projecttracker.views.person_index'),
    (r'^person/(?P<person_id>\d+)/$', 'supra.projecttracker.views.person_detail'),

	# time urls
    (r'^time/$', 'supra.projecttracker.views.time_index'),
    (r'^time/(?P<time_id>\d+)/$', 'supra.projecttracker.views.time_detail'),

	# expense urls
    (r'^expense/$', 'supra.projecttracker.views.expense_index'),
    (r'^expense/(?P<time_id>\d+)/$', 'supra.projecttracker.views.expense_detail'),

	# invoice urls
    (r'^invoice/$', 'supra.projecttracker.views.invoice_index'),
    (r'^invoice/(?P<invoice_id>\d+)/$', 'supra.projecttracker.views.invoice_detail'),

 )


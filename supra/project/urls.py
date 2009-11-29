urlpatterns = patterns('project.views',
    url(r'^$','view_all'),
	url(r'^/(?P<project_id>\d+)/$','view_single'),    
)

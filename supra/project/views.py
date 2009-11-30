from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django import forms
from project.models import *
import supra.settings

### UNIV VARS ###
clients = Company.objects.all()


### PROJECT ###

def view_all(request):		

	all_projects = Project.objects.all()
	form = ProjectForm()
	
	# if request was posted to sort, then sort results
	if request.method == 'POST':	
		sort_by = request.POST['sort_by'] 
		
		if sort_by == 'title':
			return render_to_response('project/index.html', {
				'form': form,
				'all_projects':all_projects.order_by('title')},		
				context_instance = RequestContext(request))
		if sort_by == 'client':
			return render_to_response('project/index.html', {
				'form': form,
				'all_projects':all_projects.order_by('client')},		
				context_instance = RequestContext(request))
		if sort_by == 'category':
			return render_to_response('project/index.html', {
				'form': form,
				'all_projects':all_projects.order_by('category')},		
				context_instance = RequestContext(request))
						
	# otherwise render the normal page, sort by project id	
	return render_to_response('project/index.html', {
		'form': form,
		'all_projects':all_projects.order_by('projectId')},		
		context_instance = RequestContext(request))

	
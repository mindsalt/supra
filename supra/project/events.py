from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django import forms
from project.models import *
import supra.settings

	
def start_edit(request):
	key = request.POST['projectId']
	project = Project.objects.get(projectId=key)
	f = ProjectForm(instance=project)	
	
	return render_to_response('project/edit_form.html', {
		'form': f},		
		context_instance = RequestContext(request))


def save_edit(request):
	# this section is a mess. how to update existing record?
	key = request.POST['projectId']
	old_project = Project.objects.get(projectId=key)
	form = ProjectForm(request.POST, instance=old_project)
	
	if form.is_valid():
		form.save()
		all_projects = Project.objects.all()
		blank_form = ProjectForm()
		
		return render_to_response('project/index.html', {
			'form': blank_form,
			'all_projects':all_projects},		
			context_instance = RequestContext(request))
	else:
		form = ProjectForm(request.POST) # if errors, show bound form w/ error msg
		print form.errors				


def create_project(request):
	all_projects = Project.objects.all()

	# process new project form 
	form = ProjectForm(request.POST)
	if form.is_valid():
		project = form.save(commit=False)
	
		# create ID
		client_code = str(project.client).upper()[:3]
		year = str(datetime.datetime.now())[2:4]
		client_total = len(Project.objects.filter(client=project.client))
		proj_num = client_total + 1
		
		# assign ID and other req'd fields
		project.projectId = client_code + year + str(proj_num)
		project.date_created = datetime.datetime.now()
		project.total_time = 0
		
		project.save()
		return HttpResponseRedirect("/project/view/")

	else:
		form = ProjectForm(request.POST) # if errors, show bound form w/ error msg
		error_message = form.errors			
		return render_to_response('project/index.html', {
			'form': form,
			'all_projects':all_projects,
			'error_message':error_message},		
			context_instance = RequestContext(request))



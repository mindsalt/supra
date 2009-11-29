from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django import forms
from project.models import *
import supra.settings

	
def start_edit(request):
	key = request.POST['projectId']
	project = Project.objects.get(projectId=key)
	f = ProjectForm(instance=project)	
	
	return render_to_response('project/edit_form.html', {
		'form': f,
	})


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
			'all_projects':all_projects
		})
	else:
		form = ProjectForm(request.POST) # if errors, show bound form w/ error msg
		print form.errors				

def create(request):
	return HttpResponse("Here's the created section.")


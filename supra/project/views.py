from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django import forms
from project.models import *
import supra.settings

### UNIV VARS ###
clients = Company.objects.all()


### PROJECT ###

def view_all(request):		

	all_projects = Project.objects.all()

	form = ProjectForm(request.POST)
	
	# if form has been submitted, process it
	if request.method == 'POST':
		
		if form.is_valid():
			form = ProjectForm(request.POST)
			new_project = form.save(commit=False)
			
			# create ID
			client_code = str(new_project.client).upper()[:3]
			year = str(datetime.datetime.now())[2:4]
			client_total = len(Project.objects.filter(client=new_project.client))
			proj_num = client_total + 1
			new_project.projectId = client_code + year + str(proj_num)
			
			# other req'd fields
			new_project.date_created = datetime.datetime.now()
			new_project.total_time = 0
			
			#save the project
			new_project.save()
			
			# redirect to success page
			return HttpResponseRedirect('/project/')
		else:
			form = ProjectForm() # if errors, show unbound form w/ error msg
			print form.errors	
	
	# otherwise render the normal page		
	return render_to_response('project/index.html', {
		'form': form,
		'all_projects':all_projects
	})
	
	
def view_single(request, project_id):
	# this is how we'll edit it
	p = Project.objects.get(pk=1)
	f = ProjectForm(instance=p)
	if f.is_valid():
		f.save()
		return HttpResponse('sucess!')

	return render_to_response('project/single.html', {
		'form': f,
	})

# project form related actions
# def project_companies(request):
		

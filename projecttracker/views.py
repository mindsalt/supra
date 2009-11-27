from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from supra.projecttracker.models import *
from django import forms
from django.core import serializers


### univ vars ##
clients = serializers.serialize("json", Company.objects.filter(company_type='Client'))

# return clients in JSON
def get_clients(request):
	return HttpResponse(clients,mimetype='application/json')



### HOME ###

def home_index(request):
	projects = Project.objects.all()
	companys = Company.objects.all()
	persons = Person.objects.all()

	project_form = ProjectForm()
	company_form = CompanyForm()
	person_form = PersonForm()
	time_form = TimeForm()
	expense_form = ExpenseForm()
	invoice_form = InvoiceForm()

	return render_to_response('index.html', {
		'project_form':project_form,
		'company_form':company_form,
		'person_form':person_form,
		'time_form':time_form,
		'expense_form':expense_form,
		'invoice_form':invoice_form,
	})


### PROJECT ###

def project_index(request):

	# display all projects
	all_projects = Project.objects.all().order_by('title')[:]
	all_clients = clients
	
	# add new project form processing
	if request.method == 'POST': # If the form has been submitted...
		form = ProjectForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass / cleaned_data
            # Process the data in form
			new_project = form.save()
            # redirect after POST to prevent double-save
			return HttpResponseRedirect('../project/')
	else:
		form = ProjectForm() # An unbound form
		print form.errors

	return render_to_response('project/index.html', {
		'all_projects': all_projects,
		'all_clients': clients,
		'form': form,
	})
	
def project_detail(request, project_id):
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
		


### COMPANY ###

def company_index(request):
	all_companies = Company.objects.all().order_by('name')[:]

	if request.method == 'POST': # If the form has been submitted...
		form = CompanyForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
            # Process the data in form
			new_company = form.save()
            # redirect after POST to prevent double-save
			return HttpResponseRedirect('company/index.html')
	else:
		form = CompanyForm() # An unbound form

	return render_to_response('company/index.html', {
		'all_companies': all_companies,
		'form': form,
	})

def company_detail(request, company_id):
	company = get_object_or_404(Company, pk=company_id)
	return render_to_response('company/single.html', {'company': company})
	
	
### PERSON ###
	
def person_index(request):

	# display all projects
	all_persons = Person.objects.all().order_by('name')[:]
	
	# add new project form processing
	if request.method == 'POST': # If the form has been submitted...
		form = PersonForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass / cleaned_data
            # Process the data in form
			new_person = form.save()
            # redirect after POST to prevent double-save
			return HttpResponseRedirect('person/index.html')
	else:
		form = PersonForm() # An unbound form
		print form.errors

	return render_to_response('person/index.html', {
		'all_persons': all_persons,
		'form': form,
	})
	
def person_detail(request, person_id):
	person = get_object_or_404(Person, pk=person_id)
	return render_to_response('person/single.html', {'person': person})
	
	
	
### TIME ###
	
def time_index(request):

	# display all projects
	all_objects = Time.objects.all().order_by('id')[:]
	
	# add new project form processing
	if request.method == 'POST': # If the form has been submitted...
		form = TimeForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass / cleaned_data
            # Process the data in form
			new_object = form.save()
            # redirect after POST to prevent double-save
			return HttpResponseRedirect('time/index.html')
	else:
		form = TimeForm() # An unbound form
		print form.errors

	return render_to_response('time/index.html', {
		'all_objects': all_objects,
		'form': form,
	})
	
def time_detail(request, time_id):
	time = get_object_or_404(Time, pk=time_id)
	return render_to_response('time/single.html', {'time': time})
	
		
	
### EXPENSES ###
	
def expense_index(request):

	# display all projects
	all_objects = Expense.objects.all().order_by('id')[:]
	
	# add new project form processing
	if request.method == 'POST': # If the form has been submitted...
		form = ExpenseForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass / cleaned_data
            # Process the data in form
			new_object = form.save()
            # redirect after POST to prevent double-save
			return HttpResponseRedirect('expense/index.html')
	else:
		form = ExpenseForm() # An unbound form
		print form.errors

	return render_to_response('expense/index.html', {
		'all_objects': all_objects,
		'form': form,
	})
	
def expense_detail(request, expense_id):
	expense = get_object_or_404(Expense, pk=expense_id)
	return render_to_response('expense/single.html', {'expense': expense})
	
		
### INVOICES ###
	
def invoice_index(request):

	# display all projects
	all_objects = Invoice.objects.all().order_by('id')[:]
	
	# add new project form processing
	if request.method == 'POST': # If the form has been submitted...
		form = InvoiceForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass / cleaned_data
            # Process the data in form
			new_object = form.save()
            # redirect after POST to prevent double-save
			return HttpResponseRedirect('invoice/index.html')
	else:
		form = InvoiceForm() # An unbound form
		print form.errors

	return render_to_response('invoice/index.html', {
		'all_objects': all_objects,
		'form': form,
	})
	
def invoice_detail(request, invoice_id):
	invoice = get_object_or_404(Invoice, pk=invoice_id)
	return render_to_response('invoice/single.html', {'invoice': invoice})
	
		
		
	
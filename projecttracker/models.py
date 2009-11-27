from django.db import models
from django import forms
from django.forms import ModelForm
import datetime
from django.http import HttpResponseRedirect, HttpResponse
from django import forms

###### HELPERS

class Activity(models.Model):
	name = models.CharField(max_length=144)
	def __unicode__(self):
		return self.name

class CompanyType(models.Model):
	name = models.CharField(max_length=144)
	def __unicode__(self):
		return self.name	
		
class ProjectCategory(models.Model):
	name = models.CharField(max_length=144)
	def __unicode__(self):
		return self.name	

class ProjectStatus(models.Model):
	name = models.CharField(max_length=56)
	def __unicode__(self):
		return self.name	


###### MAIN DATA MODELS

class Company(models.Model):
	name = models.CharField(max_length=144)
	company_type = models.ForeignKey(CompanyType)
	company_url = models.CharField(max_length=144, blank=True, null=True)
	def __unicode__(self):
		return self.name

class Person(models.Model):
	name = models.CharField(max_length=144)
	company = models.ForeignKey(Company)
	phone = models.CharField(max_length=15, blank=True, null=True)
	email = models.EmailField(max_length=75, blank=True, null=True)	
	def __unicode__(self):
		return self.name

class Project(models.Model):
	client = models.ForeignKey(Company)
	title = models.CharField(max_length=256)
	category = models.ForeignKey(ProjectCategory)
	projectId = models.CharField(max_length=18, unique=True)
	est_time = models.IntegerField(blank=True, null=True)
	total_time = models.IntegerField(blank=True, null=True)
	status = models.ForeignKey(ProjectStatus)
	notes = models.CharField(max_length=500, blank=True, null=True)
	date_created = models.DateTimeField()
	def __unicode__(self):
		return self.title
		
class Time(models.Model):
	person = models.ForeignKey(Person)
	client = models.ForeignKey(Company)
	project = models.ForeignKey(Project)
	date = models.DateField();
	time_spent = models.IntegerField();
	activity = models.ForeignKey(Activity)
	notes = models.TextField(max_length=312)
	billable = models.BooleanField()
	def __unicode__(self):
		return self.activity
			
class Expense(models.Model):
	purchase_date = models.DateField();
	purchased_by = models.CharField(max_length=144)
	client = models.ForeignKey(Company)
	project = models.ForeignKey(Project)
	vendor = models.CharField(max_length=144)
	descrip = models.CharField(max_length=144)
	est_amount = models.IntegerField(blank=True, null=True)
	true_amount = models.IntegerField(blank=True, null=True)	
	bill_amount = models.IntegerField(blank=True, null=True)	
	po_num = models.CharField(max_length=144, unique=True)
	client_po = models.CharField(max_length=144, blank=True, null=True )
	def __unicode__(self):
		return self.po_num

class Invoice(models.Model):
	invoice_num = models.CharField(max_length=18, unique=True)
	title = models.CharField(max_length=144)
	client = models.ForeignKey(Company);
	project = models.ManyToManyField('Project');
	est_amount = models.IntegerField(blank=True, null=True);
	true_amount = models.IntegerField(blank=True, null=True);
	bill_amount = models.IntegerField(blank=True, null=True);
	bill_date = models.DateField(blank=True, null=True);
	paid = models.BooleanField();
	def __unicode__(self):
		return self.invoice_num	


		
###### FORM MODELS
	
class ProjectForm(forms.Form):
	client = forms.ModelChoiceField(queryset=Company.objects.all(), empty_label=None)
	title = forms.CharField(max_length=256)
	category = forms.ModelChoiceField(queryset=ProjectCategory.objects.all(), empty_label=None)
	projectId = forms.CharField(max_length=18)
	est_time = forms.IntegerField()
	total_time = forms.IntegerField()
	status = forms.ModelChoiceField(queryset=ProjectStatus.objects.all(), empty_label=None)
	notes = forms.CharField(widget=forms.Textarea)
	date_created = forms.DateTimeField()
		
		
	
class CompanyForm(ModelForm):
	class Meta:
		model = Company
	
class PersonForm(ModelForm):
	class Meta:
		model = Person
		
class TimeForm(ModelForm):
	class Meta:
		model = Time

class ExpenseForm(ModelForm):
	class Meta:
		model = Expense
		
class InvoiceForm(ModelForm):
	class Meta:
		model = Invoice

		
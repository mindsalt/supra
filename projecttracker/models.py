from django.db import models
from django.forms import ModelForm
import datetime
from django.http import HttpResponseRedirect, HttpResponse

# data models


class Company(models.Model):
	COMPANY_TYPE_CHOICES = (
		(u'Owner Company', u'Owner Company'),
		(u'Client', u'Client'),				
		(u'Vendor', u'Vendor'),
		(u'Other', u'Other'),				
	)
	name = models.CharField(max_length=144)
	company_type = models.CharField(max_length=144, choices=COMPANY_TYPE_CHOICES)
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
	CATEGORY_CHOICES = (
		(u'Identity', u'Identity'),
		(u'Print', u'Print'),		
		(u'Web', u'Web'),
		(u'PR',u'PR'),
		(u'Uncategorized',u'Uncategorized'),
	)
	STATUS_CHOICES = (
		(u'Proposed', u'Proposed'),
		(u'Active', u'Active'),
		(u'Complete', u'Complete'),	
		(u'On Hold', u'On Hold'),			
	)
	client = models.ForeignKey(Company)
	title = models.CharField(max_length=256)
	category = models.CharField(max_length=144, choices=CATEGORY_CHOICES)
	projectId = models.CharField(max_length=18, unique=True)
	est_time = models.IntegerField(blank=True, null=True)
	total_time = models.IntegerField(blank=True, null=True)
	status = models.CharField(max_length=56, choices=STATUS_CHOICES)
	team_members = models.ManyToManyField('Person')
	date_created = models.DateTimeField()
	def __unicode__(self):
		return self.title


class Activity(models.Model):
	name = models.CharField(max_length=144)
	def __unicode__(self):
		return self.name
		
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
		
# form models
class ProjectForm(ModelForm):
	class Meta:
		model = Project
	
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

		
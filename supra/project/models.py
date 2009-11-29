from django.db import models
from django.forms import ModelForm
import datetime

###### HELPERS

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

class Project(models.Model):
	projectId = models.CharField(max_length=18, unique=True, editable=False)
	date_created = models.DateTimeField(editable=False)	
	client = models.ForeignKey(Company)
	title = models.CharField(max_length=256)
	category = models.ForeignKey(ProjectCategory)
	est_time = models.IntegerField(blank=True, null=True)
	total_time = models.IntegerField(blank=True, null=True, editable=False)
	status = models.ForeignKey(ProjectStatus)
	notes = models.TextField(blank=True, null=True)
	def __unicode__(self):
		return self.title
		
		
###### FORM MODELS
	
class ProjectForm(ModelForm):
	class Meta:
		model = Project		

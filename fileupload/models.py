from django.db import models



class Person(models.Model):
	instruction_id	 = models.IntegerField()
	case_ref_no 	 = models.CharField(max_length=100, blank=True)
	client_name		 = models.CharField(max_length=100, blank=True)
	candidate_name 	 = models.CharField(max_length=100, blank=True)
	complete_address = models.CharField(max_length=100, blank=True)
	period_of_stay  =  models.DateField()

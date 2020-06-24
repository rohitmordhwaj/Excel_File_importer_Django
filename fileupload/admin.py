from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Person

@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
	pass
    #list_display = ('id',Instruction_ID', 'Case_Ref_No', 'Client_Name','Candidate_Name','Complete_Address','Period_of_Stay')
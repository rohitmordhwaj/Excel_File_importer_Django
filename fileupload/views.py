from django.shortcuts import render
from django.http import HttpResponse
from .resources import PersonResource
from tablib import Dataset
from .models import Person

def simple_upload(request):
	if request.method == 'POST':
		person_resource = PersonResource()
		dataset = Dataset()
		new_persons = request.FILES['myfile']

		imported_data = dataset.load(new_persons.read(),format='xlsx')
        #print(imported_data)
		for data in imported_data:
			print(data[1])
			value = Person(
        		 data[0],
        		 data[1],
        		 data[2],
        		 data[3],
        		 data[4],
        		 data[5],
        		 data[6],
        		)
			value.save()       
  

	return render(request, 'input.html')
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from web_page_annotation.models import *
import random
import string
# Create your views here.

def index(request):
    #return HttpResponse("<h1>This is web_page_annotation</h1>")
	# Example_Model.objects.all().delete()
	if Annotation_Model.objects.count()==0:
		list_objects = []
		for index in range(0, 10000):
			list_objects.append(
				Annotation_Model(
                    korpus_id="".join( [random.choice(string.digits) for i in range(3)] ),
                    hit="".join( [random.choice(string.digits) for i in range(3)] ),
                    task="".join( [random.choice(string.digits) for i in range(3)] ),
                    ad_mace="".join( [random.choice(string.ascii_lowercase) for i in range(8)] ),
					ad_annotation="".join([random.choice(string.ascii_lowercase) for i in range(8)]),
                    cutoff_mace="".join( [random.choice(string.ascii_lowercase) for i in range(8)] ),
					cutoff_annotation="".join([random.choice(string.ascii_lowercase) for i in range(8)]),
                    loading_mace="".join( [random.choice(string.ascii_lowercase) for i in range(8)] ),
					loading_annotation="".join([random.choice(string.ascii_lowercase) for i in range(8)]),
                    pornographic_mace="".join( [random.choice(string.ascii_lowercase) for i in range(8)] ),
					pornographic_annotation="".join([random.choice(string.ascii_lowercase) for i in range(8)]),
                    popup_mace="".join( [random.choice(string.ascii_lowercase) for i in range(8)] ),
					popup_annotation="".join([random.choice(string.ascii_lowercase) for i in range(8)]),
                    captcha_mace="".join( [random.choice(string.ascii_lowercase) for i in range(8)] ),
					captcha_annotation="".join([random.choice(string.ascii_lowercase) for i in range(8)]),
                    error_mace="".join( [random.choice(string.ascii_lowercase) for i in range(8)] ),
					error_annotation="".join([random.choice(string.ascii_lowercase) for i in range(8)])
				)
			)

		Annotation_Model.objects.bulk_create(list_objects)

	return JsonResponse({})

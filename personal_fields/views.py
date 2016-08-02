from django.http import HttpResponse,HttpResponseRedirect, Http404
from django.conf.urls import url
from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.core.urlresolvers import reverse

from django.utils.timezone import utc
from django.utils import timezone

from .models import Form, Text_field, Text_area, Select_item,  Item_field


# Create your views here.

'''
Lembre-se de adicionar o novo app em mysite/settings.py
'''

def index(request):
	forms = Form.objects.all()
	return render(request, 'personalFields/index.html',{
		'time':timezone.now(),
		'forms' : forms,

		})
	#return HttpResponse("<h1>Welcome to personal fields</h1>")
	
def new_form(request):

	if len(request.POST) > 0:
		try:
			form  = Form()
			form.description = request.POST['form_description']
			form.save()

			return HttpResponseRedirect(reverse('personal_fields:view_form',args=(form.id,)))

		except:
			return render(request,'personalFields/index.html',{
				'error_message': 'Erro while inserting form'
				})
	else:		
		return render(request,'personalFields/createForm.html',{
			})

def new_text_field(request,form_id):

	if len(request.POST):
		try:
			text_field = Text_field()
			text_field.name = request.POST['name']
			text_field.value = request.POST['value']
			text_area.form_id = form_id

			text_field.save()

			return HttpResponseRedirect(reverse('personal_fields:view_form',args=(form_id,)))

		except:
			return render(request,'personalFields/index.html',{
				'error_message': 'Erro while inserting new text field'
				})
	else:
		return render(request,'personalFields/createTextField.html',{
			'form_id': form_id
			})

def new_text_area(request,form_id):

	if len(request.POST):
		try:
			text_area = Text_area()
			text_area.name = request.POST['name']
			text_area.value = request.POST['value']
			text_area.form_id = form_id

			text_area.save()

			return HttpResponseRedirect(reverse('personal_fields:view_form',args=(form_id,)))

		except:
			return render(request,'personalFields/index.html',{
				'error_message': 'Erro while inserting new text area'
				})
	else:
		return render(request,'personalFields/createTextArea.html',{
			'form_id':form_id
			})

def new_select_item(request,form_id):

	if len(request.POST):
		try:
			
			select_item = Select_item()
			select_item.name = request.POST['name']
			select_item.save()

			items = request.POST['items']
			for item in items:
				item_field = Item_field()
				if len(item) > 0:
					item_field.name = item
					item_field.select_item_id = select_item.id
					
					item_field.save()			

			return HttpResponseRedirect(reverse('personal_fields:view_form',args=(form_id,)))

		except:
			return render(request,'personalFields/index.html',{
				'error_message': 'Erro while inserting new text field'
				})
	else:
		return render(request,'personalFields/createSelectItem.html',{
			'form_id': form_id
			})

def view_form(request,form_id):

	#forms = Form.objectsfilter(id=1)
	#$form = Form.objects.get(pk = 1)
	#Entry.objects.all().delete()
	#b.delete()

	#ver making queries pg 102
	

	formModel = get_object_or_404(Form, pk=form_id)
	textFields = [] #Text_field.objects.all()
	textAreas = []
	selectOptions = []

	return render(request,'personalFields/viewForm.html',{
		'form_id': form_id,
		'form': formModel,
		'textFields': textFields,
		'textAreas' : textAreas,
		'selectOptions' : selectOptions
		})


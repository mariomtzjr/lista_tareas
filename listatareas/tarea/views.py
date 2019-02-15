from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse, reverse_lazy
from .forms import TareaForm
from .models import Tarea

# Create your views here.

class tareaPageView(TemplateView):
	template_name = "tarea_list.html"


class tareaCreateView(CreateView):
	model = Tarea
	fields = ['codigo','descripcion']
	template_name = "tarea_form.html"

	def get(self, request):
		tarea_form = TareaForm()
		if request.method == 'POST':
			tarea_form = TareaForm(request.POST)
			if tarea_form.is_valid():
				tarea_form.save()
		else:
			tarea_form = TareaForm()
		return render(request, "tarea_form.html", {'form':tarea_form})

	def get_success_url(self):
            return reverse('tarea_listar')


class tareaListView(ListView):
	model = Tarea
	template_name = "tarea_list.html"


class tareaUpdateView(UpdateView):
	model = Tarea
	template_name = "tarea_list.html"

	def get(self, request, *args, **kwargs):
		tarea = Tarea.objects.get(id=kwargs['id'])
		tarea.estado = not tarea.estado
		tarea.save()

		return HttpResponseRedirect(reverse('tarea_listar'))

class tareaDeleteView(DeleteView):
	model = Tarea
	template_name = "tarea_confirm_delete.html"

	success_url = reverse_lazy('tarea_listar')
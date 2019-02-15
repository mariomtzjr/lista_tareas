from django import forms

class TareaForm(forms.Form):
	codigo = forms.CharField(required=True, max_length=50)
	descripcion = forms.CharField(required=True, max_length=500)
	creacion = forms.DateTimeField()

	codigo.widget.attrs.update({
		'class': 'form-control form-control-lg tarea-codigo',
		'placeholder':'Código de tarea'
	})
	descripcion.widget.attrs.update({
		'class': 'form-control form-control-lg tarea-descripcion',
		'placeholder':'Escribe una tarea aquí'
	})
	creacion.widget.attrs.update({
		'class': 'form-control btn btn-primary btn-agregar-tarea'
	})


from django import forms
from recensioni.models import Recensione, Commento

class ResearchForm(forms.Form):
	titolo = forms.CharField(max_length = 50, 
									label = 'Titolo')
	genere = forms.CharField(max_length = 50, required = False,
						label = 'Genere (opzionale)')
	ncomm = forms.IntegerField(label = 'Numero commenti (opzionale)', 
							required = False)

	
class ReviewForm(forms.ModelForm) :
	class Meta:
		model = Recensione
		fields = Recensione.campi()
		widgets = {}
		for hidden in Recensione.campi_segreti():
			widgets[hidden] = forms.HiddenInput()

class CommentForm(forms.ModelForm) :
	class Meta:
		model = Commento
		fields = Commento.__campi__()
		widgets = {}
		for campoSegreto in Commento.__campisegreti__():
			widgets[campoSegreto] = forms.HiddenInput()

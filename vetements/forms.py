# -*- coding: utf-8 -*-
from django import forms
from vetements.models import Sex, Age, TypeCategorie, Exclure


class FormulaireExclure(forms.ModelForm):
	class Meta:
		model = Exclure

from django import forms
from . import models

# Formulario para cadastrar um Tipo de Despesa
class TipoDespesasForm(forms.ModelForm):
    class Meta:
        model = models.TipoDespesas
        fields = [
            'nome'
        ]

# Formulario para cadastrar um Tipo de Faturamento
class TipoFaturamentoForm(forms.ModelForm):
    class Meta:
        model = models.TipoFaturamento
        fields = [
            'nome'
        ]

# Formulário para cadastrar uma Despesa
class DespesasForm(forms.ModelForm):
    class Meta:
        model = models.Despesas
        fields = [
            'nome',
            'mes',
            'data_vencimento',
            'data_pagamento',
            'valor',
            'fixo',
            'tipo'
        ]

# Formulario para cadastrar um Faturamento
class FaturamentosForm(forms.ModelForm):
    class Meta:
        model = models.Faturamentos
        fields = [
            'nome',
            'mes',
            'data_vencimento',
            'data_pagamento',
            'valor',
            'fixo',
            'tipo'
        ]

# Formulario para cadastrar um Fechamento
class FechamentosForm(forms.ModelForm):
    class Meta:
        model = models.Fechamentos
        exclude = [
            'faturamento',
            'despesas',
            'balanco'
        ]
        widgets = {
            'faturamento': forms.HiddenInput(),
            'despesas': forms.HiddenInput(),
            'balanco': forms.HiddenInput(),
        }



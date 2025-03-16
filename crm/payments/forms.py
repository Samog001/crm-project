from django import forms

from.models import PaymentStructure,PaymentSettleChoices,InstallmentChoices



class PaymentStructureForm(forms.ModelForm):
    
    class Meta:
        
        model = PaymentStructure
        
        exclude =['uuid','active_status','student','fee_to_be_paid']

    one_time_or_installments = forms.ChoiceField(choices=PaymentSettleChoices.choices,widget=forms.Select(attrs={
                                                                                 'class':"block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input",
                                                                                 'id':'one-time-or-installments',
                                                                                 'required':'required'}))
        
    no_of_installments = forms.ChoiceField(choices=InstallmentChoices.choices,widget=forms.Select(attrs={
                                                                                 'class':"block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input",
                                                                                 'required':'required'}))
    
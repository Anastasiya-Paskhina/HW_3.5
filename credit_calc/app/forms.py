from django import forms


class CalcForm(forms.Form):
    initial_fee = forms.IntegerField(label="Стоимость товара")
    rate = forms.IntegerField(label="Процентная ставка")
    months_count = forms.IntegerField(label="Срок кредита в месяцах")

    def clean_initial_fee(self):
        # валидация одного поля, функция начинающаяся на `clean_` + имя поля
        initial_fee = self.cleaned_data.get('initial_fee')
        if not initial_fee or initial_fee < 0:
            raise forms.ValidationError("Стоимость товара не может быть отрицательной")
        return initial_fee

    def clean_all(self):
        # общая функция валидации
        initial_fee = self.cleaned_data.get('initial_fee')
        rate = self.cleaned_data.get('rate')
        months_count = self.cleaned_data.get('months_count')

        if not initial_fee or initial_fee < 0:
            raise forms.ValidationError("Стоимость товара не может быть отрицательной")

        if not rate or rate < 0:
            raise forms.ValidationError("Процентная ставка не может быть отрицательной")

        if not months_count or months_count < 1:
            raise forms.ValidationError("Минимальный срок кредита один месяц")

        return self.cleaned_data



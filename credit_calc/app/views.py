from django.views.generic import TemplateView
from django.shortcuts import render
from .forms import CalcForm


class CalcView(TemplateView):
    template_name = "app/calc.html"

    def get(self, request, *args, **kwargs):
        form = CalcForm(self.request.GET)

        if form.is_valid():
            initial_fee = form.cleaned_data["initial_fee"]
            rate = form.cleaned_data["rate"]
            months_count = form.cleaned_data["months_count"]
            sum_res = initial_fee + initial_fee * rate / 100
            per_month = sum_res / months_count
            return render(
                request,
                self.template_name,
                {'form': form,
                 'sum_res': sum_res,
                 'per_month': round(per_month, 2),
                 }
            )

        return render(
            request,
            self.template_name,
            {'form': form}
        )


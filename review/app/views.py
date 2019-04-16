from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView

from .models import Product, Review
from .forms import ReviewForm


class ProductsList(ListView):
    model = Product
    context_object_name = 'product_list'


class ProductView(DetailView):
    form_class = ReviewForm
    model = Product
    template_name = 'app/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        if self.kwargs['pk'] not in self.request.session['reviewed_products']:
            context['form'] = self.form_class
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        product_pk = self.kwargs['pk']
        if self.request.session['reviewed_products']:
            reviewed_products = self.request.session['reviewed_products']
        else:
            reviewed_products = []
        if form.is_valid():
            Review.objects.create(text=request.POST['text'],
                                  product=Product.objects.get(id=product_pk))
            reviewed_products.append(product_pk)
            self.request.session['reviewed_products'] = reviewed_products
        return redirect(reverse('product_detail', kwargs=self.kwargs))

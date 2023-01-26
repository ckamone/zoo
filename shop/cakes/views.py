from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy

from cakes.tasks import get_request_info

from cakes.models import Cake, CakeType, Ingredient
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView,
    DeleteView,
)
# Create your views here.
# views = controllers

# @login_required
def main_page(request):
    return render(request, 'cakes/index.html')

#def categories_page(request):
#    types = CakeType.objects.all()
#    context = {
#        'types': types
#    }
#    return render(request, 'cakes/categories.html', context=context)

#def products_page(request):
#    cakes = Cake.objects.all()
#    context = {
#        'cakes': cakes
#    }
#    return render(request, 'cakes/products.html', context=context)


class CakeTypeListView(UserPassesTestMixin, ListView):
    model = CakeType

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser


class CakeTypeCreateView(UserPassesTestMixin, CreateView):
    model = CakeType
    fields = '__all__'
    success_url = reverse_lazy('categories_page')

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser


class CakeTypeUpdateView(UserPassesTestMixin, UpdateView):
    model = CakeType
    fields = '__all__'
    success_url = reverse_lazy('categories_page')

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser


class CakeTypeDeleteView(UserPassesTestMixin, DeleteView):
    model = CakeType
    success_url = reverse_lazy('categories_page')

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser


class IngredientListView(UserPassesTestMixin, ListView):
    model = Ingredient

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser


class IngredientCreateView(UserPassesTestMixin, CreateView):
    model = Ingredient
    fields = '__all__'
    success_url = reverse_lazy('ingredients_page')

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser


class IngredientUpdateView(UserPassesTestMixin, UpdateView):
    model = Ingredient
    fields = '__all__'
    success_url = reverse_lazy('ingredients_page')

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser


class IngredientDeleteView(UserPassesTestMixin, DeleteView):
    model = Ingredient
    success_url = reverse_lazy('ingredients_page')

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser


class CakeListView(ListView):
    model = Cake

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['help_text'] = 'help'
        return context


class CakeDetailView(LoginRequiredMixin, DetailView):
    model = Cake


class CakeCreateView(PermissionRequiredMixin, UserPassesTestMixin, CreateView):
    permission_required = 'cakes.create_cake'
    model = Cake
    fields = '__all__'
    success_url = reverse_lazy('cakes_page')

    def post(self, request, *args, **kwargs):
        get_request_info.delay(url=request.path, method=request.method)
        return super().post(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        get_request_info.delay(url=request.path, method=request.method)
        return super().get(request, *args, **kwargs)

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser


class CakeUpdateView(PermissionRequiredMixin, UserPassesTestMixin, UpdateView):
    permission_required = 'cakes.change_cake'
    model = Cake
    fields = '__all__'
    success_url = reverse_lazy('cakes_page')

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser


class CakeDeleteView(PermissionRequiredMixin, UserPassesTestMixin, DeleteView):
    permission_required = 'cakes.delete_cake'
    model = Cake
    success_url = reverse_lazy('cakes_page')

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser
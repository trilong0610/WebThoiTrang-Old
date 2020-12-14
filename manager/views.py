from django.contrib import auth
from django.contrib.auth import decorators
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from product.models import Product
from product.forms import ProductForm,CategoryForm
from supplier.models import Supplier
from supplier.forms import  SupplierForm
from purchase.forms import PurchaseProductForm
from django.contrib.auth.models import User
from datetime import datetime
# Create your views here.
from  django.http import HttpResponse
@decorators.login_required(login_url='/login/')
def home(request):
    perm = ["A"]
    if request.user.has_perm('Product.add_product'):
        perm.append("add_product")
    context = {"perm": perm}
    return render(request, "manager/base.html", context)

# Nhap San Pham Tu NCC
class purchase_product(LoginRequiredMixin,View):
    def get(self, request):
        form = PurchaseProductForm()
        return render(request, "manager/purchase_product.html", {'form':form})
    def post(self,request):
        form = PurchaseProductForm(request.POST)
        form.complete = False
        if form.is_valid():
            form.save()
            return redirect('/manager/')
        else:
            return HttpResponse('Sai Cu Phap')

# Quan Li San Pham
class add_category(LoginRequiredMixin,View):
    def get(self,request):
        category = CategoryForm()
        return render(request, "manager/manage_Action.html", {"add_category": category})
    def post(self,request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/manager/')
        else:
            return HttpResponse("Sai cu phap")
class add_product(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self, request):
            product = ProductForm()
            return render(request, "manager/manage_Action.html", {"add_product": product})
    def post(self,request):
        form = ProductForm(data = request.POST, files= request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/manager/')
        else:
            return HttpResponse("Sai cu phap")
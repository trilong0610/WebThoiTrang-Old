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

# Phan Quyen
class user_Permission(LoginRequiredMixin,View):
    def get(self,request):
        user = User.objects.all()
        app_name_en = {'order.view_order','order.add_order','order.change_order','order.delete_order',
                    'order.view_orderitem','order.add_orderitem','order.change_orderitem','order.delete_orderitem',
                    'order.view_shippingaddress','order.add_shippingaddress','order.change_shippingaddress','order.delete_shippingaddress',
                    'product.view_product','product.add_product','product.change_product','product.delete_product',
                    'product.view_category','product.add_category','product.change_category','product.delete_category',
                    'purchase.view_purchaseproduct','purchase.add_purchaseproduct','purchase.change_purchaseproduct','purchase.delete_purchaseproduct',
                    'supplier.view_supplier','supplier.add_supplier','supplier.change_supplier','supplier.delete_supplier'
                    }
        context = {'user': user, 'app_name_en':app_name_en}
        return render(request, 'manager/user_permission.html', context)
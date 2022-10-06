# from django.shortcuts import render

# # Create your views here.
# from django.contrib.auth.base_user import BaseUserManager

import os
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,FormView
from event import settings
from django.urls import path
from event_management.models import User,Event

from .forms import Addevent, CustomUserCreationForm,CustomAuthenticationForm
from django.contrib.auth.views import LoginView
from django.views.generic import RedirectView,View
from django.contrib.auth import login,authenticate,logout
from django.shortcuts import get_object_or_404, redirect, render,HttpResponseRedirect,HttpResponse
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from pathlib import Path

from django.contrib.auth import REDIRECT_FIELD_NAME, logout as auth_logout
BASE_DIR = Path(__file__).resolve().parent.parent
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("register")
    template_name = "register.html"
# class UserManager(BaseUserManager):
#     use_in_migrations = True

#     def _create_user(self, email, password, **extra_fields):
#         """
#         Creates and saves a User with the given email and password.
#         """
#         if not email:
#             raise ValueError('The given email must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_user(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(email, password, **extra_fields)

#     def create_superuser(self, email, password, **extra_fields):
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self._create_user(email, password, **extra_fields)


class Login(LoginView):

    authentication_form = CustomAuthenticationForm

    form_class = CustomAuthenticationForm

    template_name = 'login.html'

    def form_valid(self, form):

        # remember_me = form.cleaned_data['remember_me']

        login(self.request, form.get_user())

        return super(LoginView, self).form_valid(form)


def index(request):
    # payed_items=OrderDetail.objects.filter(has_paid=True).values('product')
    # data_list=[items['product'] for items in payed_items]
    # data_obj= event_details.objects.filter(id__in=data_list).order_by('-id')
    # p = Paginator(data_obj, 3)
    # page_number = request.GET.get('page')
    # try:
    #     page_obj = p.get_page(page_number)  # returns the desired page object
    # except PageNotAnInteger:
    #     # if page_number is not an integer then assign the first page
    #     page_obj = p.page(1)
    # except EmptyPage:
    #     # if page is empty then return last page
    #     page_obj = p.page(p.num_pages)
    if 'user_id' not in request.session:
        user_obj=None
        # return render(request, "index.html", {'user_obj': user_obj, 'permission': False,'data':page_obj})
        return render(request, "index.html", {'user_obj': user_obj, 'permission': False})
    else:
        user_obj = User.objects.filter(username=request.session['user_id']).values('pk', 'name', 'age', 'address', 'username', 'phonenumber')
        
        # return render(request, "index.html", {'user_obj': user_obj, 'permission': True,'data':page_obj})
        return render(request, "index.html", {'user_obj': user_obj, 'permission': True})

# class LogoutView(RedirectView):
#     """
#     Provides users the ability to logout
#     """
#     url = '/login'

#     def get(self, request, *args, **kwargs):
#         auth_logout(request)
#         return super(LogoutView, self).get(request, *args, **kwargs)



class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')

class AddEventView(LoginRequiredMixin,FormView):
    form_class = Addevent
    success_url = reverse_lazy("/")
    template_name = "addevent.html"
    def post(self, request):
        event_name='none'
        description='none'
        date='none'
        time='none'
        s=[]
        log=Addevent(request.POST)
        if log.is_valid():
            event_name=log.cleaned_data['name']

            description=log.cleaned_data['description']

            date=log.cleaned_data['date']

            time=log.cleaned_data['time']
            event_pic = request.FILES.get('propic')
            if event_pic:
                fs = FileSystemStorage()
                name = fs.save(event_pic.name, event_pic)
                name = 'media/' + name
                path = os.path.join(BASE_DIR, name)
            user=User.objects.get(username=request.user)
            events=Event(name=event_name,description=description,date=date,time=time,user=user,event_image=event_pic)
            events.save()
        else:
            return render(request,'addevent.html',{'register': False})
        return render(request,'index.html',{'register':True})


class EventListView(ListView):
    paginate_by = 3
    model= Event
    template_name = "index.html"
    def get_queryset(self):
    # def get(self, request):
        
        queryset=Event.objects.all()
    #     print(queryset)
        return queryset
    # model = Contact
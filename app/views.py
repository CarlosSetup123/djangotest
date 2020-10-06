from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from . forms  import MyUserForm
from . models import MyUser, Profile

# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"

class SuccessView(TemplateView):
    template_name = "success.html"

class SignUpView(TemplateView):
    template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        form = MyUserForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        '''storage = messages.get_messages(request)
        for m in storage:
            # This iteration is necessary
            pass'''
        form = MyUserForm(request.POST)
        if form.is_valid():
            user = MyUser.objects.create_user(
                    request.POST.get('username'),
                    request.POST.get('email'),
                    request.POST.get('password')
                )
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.phone_number = request.POST.get('phone_number')
            user.save()
            return redirect('user_register')
        return render(request, self.template_name, {'form': form})
'''def user_register(request):

    template = 'register.html'
   
    if request.method == 'POST':
        # instancio MyUserForm
        form = MyUserForm(request.POST)
        # verificar si es un formulario valido
        if form.is_valid():
            if MyUser.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username ya se encuentra registrado.'
                })
            elif MyUser.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email ya se encuentra registrado.'
                })
            else:
                # Crear el usuario
                user = MyUser.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.phone_number = form.cleaned_data['phone_number']
                user.save()
                
                # redireccionar
                return HttpResponseRedirect('registro/success')

   # No post data availabe, let's just show the page.
    else:
        form = MyUserForm()

    return render(request, template, {'form': form})'''
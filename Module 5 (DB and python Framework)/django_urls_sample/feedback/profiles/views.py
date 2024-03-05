from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfileForm
from .models import UserProfile
from django.views.generic.edit import CreateView
from django.views.generic import ListView
# Create your views here.

def storing_file(file):
    with open('temp/image1.jpeg','wb+') as dest:
        for chunk in file.chunks():
            dest.write(chunk)

class CreateProfileView(CreateView):
    template_name='profiles/create_profile.html'
    model=UserProfile
    fields='__all__'
    success_url='/profiles'    #can del form now.
          
class CreateProfileView1(View):
    # def get(self, request): without using django forms
    #     return render(request, "profiles/create_profile.html")

    def get(self,request):
        context=dict()
        form=ProfileForm
        context['form']=form        
        return render(request,'profiles/create_profile.html',context)

    
    def post(self, request):
        context=dict()
        # storing_file(request.FILES["image"])
        # print('->',request.FILES["image"]) #we get complete name here. its not just name but completeobject which we can work with
        # return HttpResponseRedirect('/profiles') 
        
        submitted_form=ProfileForm(request.POST,request.FILES)
        context['form']=submitted_form
        if submitted_form.is_valid():
            #storing_file(request.FILES['image']) removiong helper function because of utilization of models
            profile=UserProfile(image=request.FILES['user_image'])
            profile.save()
            return HttpResponseRedirect('/profiles')
        return render(request,'profiles/create_profile.html',context)       
    
class ProfilesView(ListView):
    template_name='profiles/user_profile.html'
    model=UserProfile
    context_object_name='profiles'
    
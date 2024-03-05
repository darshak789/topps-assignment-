from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView,DetailView
from django.views.generic.edit import FormView,CreateView

# Create your views here.
'''def review(request): # optional
    if request.method == 'POST':
        entered_username=request.POST['username']
        
        if entered_username == "":
            return render(request,'reviews/review.html',{"has_error":True})
        
        print(entered_username)
        return HttpResponseRedirect("/thank-you")
    
    return render(request,'reviews/review.html',{"has_error":False})'''
    
def review_change(request):
        
    if request.method == "POST":
        #existing_model=form.objects.get(pk=1)
        form=ReviewForm(request.POST)     #pass this here as instance=existing_model,now it will prepopulated and can be updated       
        if form.is_valid(): 
            #print(form.cleaned_data)
            """review=Review(user_name=form.cleaned_data['user_name'],
                review_text=form.cleaned_data['review_text'],
                rating=form.cleaned_data['rating'])
                review.save()""" 
           #can update data as well
            form.save() 
            return HttpResponseRedirect('/thank-you')
    else:
        form=ReviewForm() #create a new empty form
    
    return render(request,'reviews/review.html',{"form":form}) #this will rendered in any case


class ReviewView1(View): #changing review defination
    def get(self,request):
        form=ReviewForm() 
        return render(request,'reviews/review.html',{"form":form})
    
    def post(self,request):
        form=ReviewForm(request.POST)
        if form.is_valid(): 
            form.save() 
            return HttpResponseRedirect('/thank-you')
        return render(request,'reviews/review.html',{"form":form})
    
class ReviewView1(FormView): #changing review defination
    form_class=ReviewForm
    template_name='reviews/review.html'
    success_url='/thank-you'
    
    def form_valid(self,form):
        form.save()
        return super().form_valid(form)
    
class ReviewView(CreateView): 
    #delete form class
    model=Review
    #fields='__all__'   
    form_class=ReviewForm
    template_name='reviews/review.html'
    success_url='/thank-you'
    
def thank_you1(request):    #changed this to class conversion
    return render(request,"reviews/thank_you.html")

class ThankYouView1(View): #still works but extending to template view is specific for rendering
    def get(self,request):
        return render(request,"reviews/thank_you.html")

class ThankYouView(TemplateView):
    template_name='reviews/thank_you.html'
    
    # def get_context_data(self, **kwargs: Any) -> dict[str, Any]: returns a dict
    #     return super().get_context_data(**kwargs)
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['msg']='this is context!'
        return context
    
class ReviewListView2(TemplateView): #changed to listview
    template_name='reviews/review_list.html'
    
    def get_context_data(self, **kwargs) :
        context=super().get_context_data(**kwargs)
        reviews=Review.objects.all()
        context['reviews']=reviews
        return context
    
class ReviewListView(ListView):
    template_name='reviews/review_list.html'
    model=Review
    context_object_name='reviews'
    
    # def get_queryset(self) -> QuerySet[Any]:
    #     return super().get_queryset()
    
    def get_queryset(self):
        base_query=super().get_queryset()
        data = base_query.filter(rating__gt=4) #store in new variable and return it
        return data
        

    
class SingleReviewView2(TemplateView):
    template_name='reviews/single_review.html'
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        review_id=kwargs["id"]
        selected_id=Review.objects.get(pk=review_id)
        context['review']=selected_id
        return context
    
class SingleReviewView(DetailView):
    template_name='reviews/single_review.html'
    model=Review
    
    def get_context_data(self, **kwargs: Any):
        context=super().get_context_data(**kwargs)
        loaded_review=self.object
        request=self.request
        favorite_id=request.session.get('fav_review') #safer way to access data is using get method.because this will not throw an error if fav review doesnt exist yet.
        context['is_fav']=favorite_id == str(loaded_review.id)
        return context
        #the value which should be stored in the context uneder is_favorite key,
        #should be then result of the comparison where i compare the fav_id from my session to the id of the loaded review like this.   
    
class AddFavoriteView(View):
    def post(self,request):
        review_id=request.POST["review_id"]
        fav_review=Review.objects.get(pk=review_id) #cant store object in session
        request.session['fav_review']=review_id
        return HttpResponseRedirect('/reviews/' + review_id)
    
    
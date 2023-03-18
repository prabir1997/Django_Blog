from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin # new

# Create your views here.
from django.views.generic import ListView,CreateView,DetailView, UpdateView, DeleteView # new
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy


class HomePageView(LoginRequiredMixin,ListView):
    model= Post
    template_name = 'post_list.html'
  
class BlogDetailView(LoginRequiredMixin,DetailView): # new
    model = Post
    template_name = 'post_detail.html'
    
    
    
    


class CreatePostView(LoginRequiredMixin,CreateView):
    model= Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy("home")
    
    def form_valid(self, form): # new
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
    

class BlogUpdateView(LoginRequiredMixin,UpdateView,UserPassesTestMixin): # new
    model = Post
    template_name = 'post_edit.html'
    fields = ('title', 'cover')
    
    def test_func(self):
        return self.request.user == self.get_object().author
    
    
    
    
class BlogDeleteView(LoginRequiredMixin,DeleteView,UserPassesTestMixin): # new
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
    
    def test_func(self):
        return self.request.user == self.get_object().author

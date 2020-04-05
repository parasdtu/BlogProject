from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from basic_app.forms import PostForm,CommentForm
from django.utils import timezone
from django.urls import reverse,reverse_lazy
from django.views.generic import View,TemplateView,DetailView,CreateView,UpdateView,DeleteView,ListView
from basic_app.models import Post,Comment
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
# def index(request):
#     return render(request,'basic_app/basic_app.html')
#
# def profile_page_reverse(request):
#     return render(request,'basic_app/profile_page.html')
#
# def user_registration(request):
#     registered=False
#
#     #user_form=UserProfileInfo()
#     #profile_form=UserProfileInfoForm()
#
#     if request.method=="POST":
#         user_form=UserInfoForm(request.POST)
#         profile_form=UserProfileInfoForm(request.POST)
#
#         if user_form.is_valid() and profile_form.is_valid():
#             user=user_form.save()
#             user.set_password(user.password)#**************IMPORANT****************
#             user.save()
#
#             profile=profile_form.save(commit=False)
#             profile.user=user
#
#             if 'profile_pic'in request.FILES:
#                 profile.profile_pic=request.FILES['profile_pic']
#
#             profile.save()
#             registered=True
#         else:
#             print(user_form.errors,profile_form.errors)
#
#     else:
#         user_form=UserInfoForm()
#         profile_form=UserProfileInfoForm()
#
#     return render(request,'basic_app/registration.html',
#                 {'user_form':user_form,
#                 'profile_form':profile_form,
#                 'registered':registered})
#
#
# def user_login(request):
#     if request.method=="POST":
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#
#         user=authenticate(username=username,password=password)
#
#         if user:
#             if user.is_active:
#                 login(request,user)
#                 return HttpResponseRedirect(reverse('basic_app:profile_page'))
#             else:
#                 return HttpResponse("Account isn't active")
#         else:
#             return HttpResponse("Invalid login details!")
#     else:
#         return render(request,'basic_app/login.html')
#
# @login_required
# def user_logout(request):
#     logout(request)
#     return HttpResponseRedirect(reverse('index'))
#
# class PostListView(ListView):
#
#     model=models.NewPostModel
#     template_name='basic_app/newpostmodel_list.html'
#
# class MyPosts(DetailView):
#
#     model=models.UserProfileInfo
#     template_name='basic_app/myposts_detail.html'
#
# # class CommentView(DetailView):
# #     model=model.CommentModel
# #     template_name='basic_app/comment_page.html'
#
#
#
# class NewPostCreate(CreateView):
#     fields=("title","text")
#     model=models.NewPostModel
#     template_name='basic_app/newpostcreate.html'

class AboutView(TemplateView):
    template_name='about.html'

class PostListView(ListView):
    model=Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model=Post

class CreatePostView(LoginRequiredMixin,CreateView):
    login_url='/login/'
    redirect_field_name='basic_app/post_detail.html'
    form_class=PostForm
    model=Post

class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url='/login/'
    redirect_field_name='basic_app/post_detail.html'
    form_class=PostForm
    model=Post

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model=Post
    success_url=reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin,ListView):
    login_url='/login/'
    redirect_field_name='basic_app/post_list.html'
    model=Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('create_date')

####################################
####################################

@login_required
def post_publish(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=post.pk)#error aa sakta hai for "post.pk", "pk" ki jagah


@login_required
def add_comment_to_post(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect('post_detail',pk=post.pk)

    else:
        form=CommentForm()
    return render(request,'basic_app/comment_form.html',{'form':form})


@login_required
def comment_approve(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect ('post_detail',pk=comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    post_pk=comment.post.pk ####??????????
    comment.delete()
    return redirect('post_detail',pk=post_pk)

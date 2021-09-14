"""
Views in the the Posts apps
"""
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    FormView,
    ListView,
    UpdateView,
)
from django.views.generic.detail import SingleObjectMixin
from .forms import CommentsForm, PostsForm
from .models import Comment, Post

# Create your views here.


def index():
    """
    Index view
    """
    return HttpResponse("Hello, world. You're at the home page.")


class PostDashboardView(LoginRequiredMixin, ListView):
    """
    A view where user can view the posts that he is author/owner of
    """

    template_name = "Posts/dashboard.html"
    context_object_name = "Posts"
    ordering = ["-date_posted"]

    def get_queryset(self):
        """
        get_queryset is used by ListViews to determine the list
        of objects that are to be displayed.
        """
        return Post.objects.filter(owner=self.request.user)


class PostListView(ListView):
    """
    A view where site visitor can view all the public posts created
    by any user
    """

    template_name = "Posts/home.html"
    context_object_name = "Posts"

    def get_queryset(self):
        """
        Return a list of post objects that are either public or which
        the logged in user is the author of
        """
        if not self.request.user.is_authenticated:
            return Post.objects.filter(is_private=False)

        return Post.objects.filter(
            Q(is_private=False) | Q(owner=self.request.user)
        ).order_by("-date_posted")


class PostDisplayView(DetailView):
    """
    A view that displays that information regarding one post object
    """

    model = Post
    template_name = "Posts/Posts_detail.html"

    def get_context_data(self, *args, **kwargs):
        """
        Returns the context data to be displayed on the detail page
        """
        context = super().get_context_data(*args, **kwargs)
        context["comments"] = Comment.objects.filter(post=self.get_object())
        context["form"] = CommentsForm()
        return context


class PostDetailFormView(SingleObjectMixin, FormView):
    """
    This view is used to display the form and save the comment
    when a POST request is sent
    """

    template_name = "Posts/posts_detail.html"
    form_class = CommentsForm
    model = Post

    def post(self, request, *args, **kwargs):
        """
        Post request is handled in this functions

        Return:
            calls the Post function of FormView class
        """
        if not request.user.is_authenticated:
            return HttpResponseForbidden()

        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        """
        form_valid function of the FormView class is overridden to set
        the author and post attributes

        Return
            calls the form_valid function of the base class
        """
        form.instance.author = self.request.user
        form.instance.post = Post.objects.get(id=self.object.pk)
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        """
        Function redirects user to a specific page after succesful
        comment submission

        Return
            reverse: returns actual url against the url name provided as
            the first argument
        """
        return reverse("Posts-detail", kwargs={"pk": self.object.pk})


class PostDetailView(View):
    """
    Class extends the base View class and
    """

    def get(self, request, *args, **kwargs):
        """
        Function is called when a GET request is made

        return
            Returns a PostDisplayView
        """
        view = PostDisplayView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Function is called when a POST request is made

        return
            Returns a PostDetailFormView
        """
        view = PostDetailFormView.as_view()
        return view(request, *args, **kwargs)


class PostUploadView(LoginRequiredMixin, CreateView):
    """
    PostUploadView extends the Create view and returns a view
    on which user can create a new post
    """

    model = Post
    template_name = "Posts/Posts_create.html"
    form_class = PostsForm

    def form_valid(self, form):
        """
        Method is called when valid form data is posted.
        It has been overridden to add owner (which is the logged in user)
        attributes to the request object before it is saved
        """
        form.instance.owner = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    PostUpdateView is a view that displays a form for editing an
    existing post object, and saving changes made by the user
    """

    model = Post
    template_name = "Posts/Posts_create.html"
    form_class = PostsForm

    def test_func(self):
        """
        test_func in the UserPassesTestMixin is overridden to check if the
        user updating the post was the original author of the post

        Parameters:
            self
        """
        post = self.get_object()
        if post.owner == self.request.user:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    PostDeleteView is a view that displays a confirmation page for
    deleting a post
    """

    model = Post
    success_url = "/"
    template_name = "Posts/Posts_delete.html"

    def test_func(self):
        """
        test_func in the UserPassesTestMixin is overridden to check if the
        user deleting the post was the original author of the post

        Parameters:
            self
        """
        post = self.get_object()
        if post.owner == self.request.user:
            return True
        return False


def logout_view(request):
    """
    Logouts the user

    Parameters:
        request: A HttpRequest object

    Return:
        redirects user to Homepage
    """
    logout(request)
    return redirect("Posts-home")

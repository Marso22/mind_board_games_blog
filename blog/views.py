from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm
from allauth.account.views import SignupView

# Create your views here.


class PostList(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 5
    
    def get_queryset(self):
        category = self.request.GET.get('category')
        if category:
            return Post.objects.filter(category=category, status=1).order_by('-created_at')
        return Post.objects.filter(status=1).order_by('-created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Post.CATEGORY_CHOICES
        context['selected_category'] = self.request.GET.get('category')
        return context

def post_detail(request, slug):
    print("post_detail view called")  # This prints every time the view is loaded

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.filter(approved=True).order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    comment_form = CommentForm()
    comment_pending_approval = False

    if request.method == "POST":
        print("POST request received")  # This prints only for POST requests
        if request.user.is_authenticated:
            comment_form = CommentForm(data=request.POST)
            print("Form errors:", comment_form.errors)  # Shows form validation errors
            if comment_form.is_valid():
                print("Comment form valid, setting message")  # Confirms form is valid
                comment = comment_form.save(commit=False)
                comment.author = request.user
                comment.post = post
                comment.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    'Comment submitted and awaiting approval'
                )
                return HttpResponseRedirect(request.path_info)
        else:
            print("User not authenticated")  # Prints if user is not logged in
            messages.add_message(
                request, messages.ERROR,
                'You must be logged in to comment'
            )

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            "comment_pending_approval": comment_pending_approval,
        },
    )

@login_required
def comment_edit(request, slug, comment_id):
    """
    Edit a comment
    """
    if request.method == "POST":
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        
        # Check if user is the author
        if comment.author == request.user:
            comment_form = CommentForm(data=request.POST, instance=comment)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.approved = False  # Re-approve after edit
                comment.save()
                messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
            else:
                messages.add_message(request, messages.ERROR, 'Error updating comment!')
        else:
            messages.add_message(request, messages.ERROR, 'You can only edit your own comments!')

    return HttpResponseRedirect(f'/posts/{slug}/')

@login_required
def comment_delete(request, slug, comment_id):
    """
    Delete a comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(f'/posts/{slug}/')

class CustomSignupView(SignupView):
    def form_valid(self, form):
        print("CustomSignupView triggered!")  # For debugging
        response = super().form_valid(form)
        messages.success(self.request, "Registration successful! Welcome to Mind Board Games Blog.")
        return response

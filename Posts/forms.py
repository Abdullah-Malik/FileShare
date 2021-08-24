"""
Module contains information regarding the forms that Posts app is using
"""

from django import forms

from .models import Comment, Post


class CommentsForm(forms.ModelForm):
    """
    CommentsForm extends ModelForm class that directly converts
    model to form and returns a form using which comments can be added
    to the posts
    """

    class Meta:
        """
        Meta information of CommentsForm
        """

        model = Comment
        fields = [
            "comment",
        ]


class PostsForm(forms.ModelForm):
    """
    PostsForm extends ModelForm class that directly converts
    model to form and returns a form using new posts can be created
    """

    class Meta:
        """
        Meta information of CommentsForm
        """

        model = Post
        fields = [
            "title",
            "description",
            "uploaded_file",
            "thumbnail_image",
            "file_type",
            "is_private",
        ]
        widgets = {"file_type": forms.RadioSelect()}

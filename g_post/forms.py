from django import forms
from django.utils import timezone
from g_post.models import Post



class AddPostForm(forms.Form):
    BOAST_ROAST_CHOICES = [
        (True, "BOAST"),
        (False, "ROAST")
    ]
    post_type = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=BOAST_ROAST_CHOICES
    )
    post = forms.CharField(widget=forms.Textarea)
  
    
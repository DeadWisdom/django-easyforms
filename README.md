Overview
====================

Django app for easier forms.

Usage, define the form with a save() function:

    class PostForm(EasyForm):
        title = forms.CharField()
        body = forms.CharField(widget=forms.Textarea)
        def save(self):
            return Post.objects.create(self.cleaned_data['title'], self.cleaned_data['body'])

Usage, in the view:

    form = PostForm(request)
    if form.is_valid():
        post = form.save(message="Your post has been created.")
        return redirect("post_detail", post.id)
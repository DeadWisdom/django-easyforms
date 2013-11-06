from django.forms import Form, ModelForm


class EasyForm(Form):
    """
    An easier way of doing forms so that they take requests instead of blank data.  Also handles
    creating a django message, and can be extended later to do other things like trigger signals.

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

    """
    methods = ['post', 'put']

    def __init__(self, request, data = None, instance=None, methods=None, **extra):
        self.methods = methods or self.__class__.methods
        self.request = request
        self.msg = msg
        self.initial = dict(tup for tup in request.GET.items())

        for k, v in extra.items():
            setattr(self, k, v)
        
        kwargs = {'initial': self.initial}
        if instance is not None:
            kwargs.update({'instance': instance})

        if request.method.lower() in self.methods:
            super(EasyForm, self).__init__(data or request.POST, request.FILES, **kwargs)
        else:
            super(EasyForm, self).__init__(**kwargs)

    def is_valid(self):
        if self.request.method.lower() not in self.methods:
            return False
        return super(EasyForm, self).is_valid()

    def save(self, message=None):
        instance = super(EasyForm, self).save()
        if not self.request.is_ajax() and message is not None:
            messages.add_message(self.request, messages.INFO, message)
        return instance


class EasyModelForm(EasyForm, ModelForm):
    """
    EasyForm version for ModelForms.

    Usage, define the form with a save() function:
        class PostForm(EasyForm):
            class Meta:
                model = Post

    Usage, in the view:
        form = PostForm(request)
        if form.is_valid():
            post = form.save(message="Your post has been created.")
            return redirect("post_detail", post.id)
    """
    pass
    

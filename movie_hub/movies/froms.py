from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Movie,Actor

class RegistrationForms(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name","last_name","email"]
    

class MovieForm(forms.ModelForm):
    actor_names = forms.CharField(
        required=True,help_text="give actor names by , seperated (samll letters)"
        )
    

    class Meta:
        model = Movie
        exclude = ["user", "actors", "created_at"]


    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)

        # Check if we are editing an existing movie (it has a primary key) so it won't run in creation cause self.instance.pk=None
        if self.instance and self.instance.pk:
            # Grab all the actor objects for this movie
            actors = self.instance.actors.all()
            
            # Extract their names and join them with a comma
            actor_list = [actor.name for actor in actors]
            
            # Set this string as the initial value for the custom field
            self.fields['actor_names'].initial = ", ".join(actor_list)



    def save(self, commit = True):
        movie = super().save(commit=False)

        if commit:
            movie.save()

            # CLEAR existing actors before saving the new list (ie for current movie it deletes all actors from joining table.)
            movie.actors.clear()

            actor_text = self.cleaned_data.get("actor_names","")

            for name in actor_text.split(","):
                name = name.strip()

                if name:
                    actor_obj,_=Actor.objects.get_or_create(name__iexact=name,defaults={"name":name.title()}) # _ created (true or false) and name__iexact=name (insensitive exact matching from database)
                    # or from default create new actor.
                    movie.actors.add(actor_obj)
            return movie
        


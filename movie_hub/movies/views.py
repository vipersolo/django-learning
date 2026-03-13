from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .froms import RegistrationForms,LoginForm,ProfileEditForm,MovieForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Movie
from django.db.models import Q



# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"your account has been successfully created !!!.")
        return redirect("login_view")
    else:
        form = RegistrationForms()
    return render(request,"movies/register.html",{"form":form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request,username=username,password=password)
            if user is not None: #important if authentication fails what to do , use if to check is not none
                login(request,user)
                return redirect("home")
            else:
                messages.error(request,"invalid credentials!!!")
    else:
        form = LoginForm()
    return render(request,"movies/login.html",{"form":form})

def logout_view(request):
    logout(request)
    return redirect("login_view")


def home(request):
    return render(request,"movies/home.html")


def profile(request):
    return render(request,"movies/profile.html")

def edit_profile(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,"Profile successfully edited.!!!") #needs request to send messages through sessions
            return redirect("profile")
    else:
        form = ProfileEditForm(instance=request.user)
    return render(request,"movies/edit_profile.html",{"form":form})


@login_required
def add_movie(request):
    if request.method == "POST":
        form = MovieForm(request.POST,request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect("movie_list")
    else:
        form = MovieForm()
    return render(request,"movies/add_movie.html",{"form":form})


#rendering movie_list
def movie_list(request):
    movies = Movie.objects.all().order_by('-created_at')
    return render(request,"movies/movie_list.html",{"movies":movies})


#------------------------------------------------------
#Movie editing by checking created user.
#------------------------------------------------------
@login_required
def edit_movie(request,id):
    movie = get_object_or_404(Movie,pk=id)

    if movie.user != request.user:
        return redirect("movie_list")
    
    if request.method == "POST":
        form = MovieForm(request.POST,request.FILES,instance=movie)
        if form.is_valid():
            form.save()
            return redirect("movie_detail",id=movie.id)
    else:
        form = MovieForm(instance=movie)
    return render(request,"movies/edit_movie.html",{"form":form})


#movie detail with id from movie_list
def movie_detail(request,id):
    movie = get_object_or_404(Movie,id=id)
    return render(request,"movies/movie_detail.html",{"movie":movie})


def my_movies(request):
    movies = Movie.objects.filter(user=request.user)
    return render(request,"movies/my_movies.html",{"movies":movies})



#delete movie if user created that movie
def delete_movie(request,id):
    movie = get_object_or_404(Movie,id=id)

    if movie.user == request.user:
        movie.delete()
    
    return redirect("movie_list")

def category_movies(request,id):
    movies=Movie.objects.filter(id=id)

    return render(request,"movies/movie_list.html",{'movies':movies})


def search_movies(request):
    query = request.GET.get("q","")
    category_id = request.GET.get("category","")

    movies = Movie.objects.all()
    if query:
        movies=Movie.objects.filter(Q(title__icontains=query)|Q(actors__name__icontains=query)).distinct()
    
    if category_id:
        movies=movies.filter(category_id=category_id)
    
    context = {
        "movies":movies,
        "query":query,
        "selected_category":category_id
    }

    return render(request,"movies/movie_list.html",{'context':context})



from django.shortcuts import render,redirect
from django.contrib import messages 
from .forms import Bookform,Updatebookform
from .models import Book
from django.contrib.auth  import authenticate,  login, logout
from django.contrib.auth.models import User
# Create your views here.
def home_page(request):
    return render(request, "Home.html")

def add_book(request):
    if request.method=='POST':
        book_form=Bookform(request.POST)
        if book_form.is_valid:
            book_form.save()
            messages.success(request, "New books added....")
            return redirect("Library_system:books_list")
    else:
        book_form=Bookform()
    return render(request,"Add_book.html",{'book_form':book_form})    

def books_list(request):
    books=Book.objects.all()
    return render(request,'Books_list.html',{'books':books})

def edit_books(request):
    edit_books=Book.objects.all()
    return render(request,'Edit_books.html',{'edit_books':edit_books})

def delete_book(request, id):
    db = Book.objects.get(id=id)
    db.delete()
    return redirect("Library_system:edit_books")

def update_book(request,id): 
    book_up = Book.objects.get(id=id)
    if request.method == "POST":
        form = Updatebookform(request.POST or None,instance=book_up)
        if form.is_valid():
            book_up = form.save(commit=False)
            book_up.save()
            messages.success(request, "information has been updated...")
            return redirect("Library_system:edit_books")
    else:
        form = Updatebookform(instance=book_up)
    return render(request, "update_book.html", {'form': form})

def user_signup(request):
    if request.method=="POST":
        # Get the post parameters
        fname=request.POST['fname']
        lname=request.POST['lname']
        username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        # check for errorneous input
        if not username.isalnum():
            messages.error(request," Username should be contain letters and numbers")
            return redirect("Library_system:signup")

        if (pass1!= pass2):
            messages.error(request," Passwords do not match")
            return redirect("Library_system:signup")
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " congratulations! Your account has been created  successfully")
        return redirect("Library_system:home_page")
        
    else:
        return render(request, "signup_page.html")


def user_login(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("Library_system:home_page")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("Library_system:logins")
    else:
        return render(request, "login_page.html")

def user_logout(request):
    logout(request)
    messages.success(request, "you are successfully logged out")
    return redirect("Library_system:home_page")
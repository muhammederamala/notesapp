from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import note_form
from .models import note_model

# Create your views here.

def home_screen_view(request):
	print(request.headers)
	return render(request,'notesapp/home.html',{})

def welcome_view(request):
	print(request.headers)
	return render(request,'notesapp/welcome.html',{})

def sign_up_view(request):
	print(request.headers)
	return render(request,'notesapp/signup.html',{})

def view_my_notes(request):
	print(request.headers)
	my_notes = note_model.objects.filter(user=request.user)
	return render(request,'notesapp/mynotes.html',{'my_notes':my_notes})

def view_all_notes(request):
	print(request.headers)
	all_notes = note_model.objects.all()
	return render(request,'notesapp/allnotes.html',{'all_notes':all_notes})


def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('welcome_view')   

        else:
            # Return an error message  the login credentials are incorrect.
            error_message = 'Invalid username or password.'
            return render(request, 'notesapp/home.html', {'error_message': error_message})
    else:
        return redirect(request, 'login')




def sign_up(request):
    if request.method == 'POST':
        username = request.POST['username']
        # If the user already exists
        if User.objects.filter(username=username).exists():
            user_exists = True
            return render(request, 'notesapp/signup.html', {'user_exists': user_exists})
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            return redirect('home_screen_view')
    return render(request, 'signup.html')



def create_note(request):
	if request.method == 'POST':
		form = note_form(request.POST, request.FILES)
		if form.is_valid():
			text = form.cleaned_data[ 'text']
			audio = form.cleaned_data['audio']
			video = form.cleaned_data['video']

			new_note_model = form.save(commit=True)
			new_note_model.user = request.user
			new_note_model.save()
			my_notes = note_model.objects.filter(user=request.user)
			return redirect('view_my_notes')
		else:
			form = note_form(request.POST)
			print(form.errors)
	else:
		form = note_form()
	return render(request, 'account/createclass.html', {'form': form})

def delete_note(request,note):
	event_to_delete = note_model.objects.get(pk=note)
	event_to_delete.delete()
	return redirect('view_my_notes')

def delete_notes(request,note):
	event_to_delete = note_model.objects.get(pk=note)
	event_to_delete.delete()
	return redirect('view_all_notes')
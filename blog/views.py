from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import RSVP
from .forms import RSVPForm
from django.contrib.auth.decorators import login_required

def contato(request):
    return render(request, 'blog/contato.html')

def home(request):
    return render(request, 'blog/home.html')

def galeria(request):
    return render(request, 'blog/galeria.html')

def rsvp(request):
	if request.method == "POST":
		form = RSVPForm(request.POST)
		post = form.save(commit = 'false')
		post.created_date = timezone.now()
		post.save()
		return redirect('blog.rsvp.html')
	else:
		form = RSVPForm()
	return render(request, 'blog/RSVP.html', {'form': form})

def evento(request):
    return render(request, 'blog/evento.html')

def lista_presentes(request):
    return render(request, 'blog/lista_presentes.html')

def lista_convidados(request):
	lista = RSVP.objects.all().order_by('convidado')
	return render(request, 'blog/lista_convidados.html', {'lista': lista})



# Create your views here.

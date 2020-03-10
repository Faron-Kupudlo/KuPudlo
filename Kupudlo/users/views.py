from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm




def register(request):                              #rejestracja
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():                         #jeśli wszystko git
            form.save()                             #zapisuje
            username = form.cleaned_data.get('username')    #pobiera nazwe użytkownika
            messages.success(request, f'Konto utworzone poprawnie, możesz się zalogować')   #messege, wyświetla się po założeniu konta
            return redirect('index')                                                        #po zalogowaniu odsyła na stronę główną
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

@login_required #blokuje stronę jeśli brak zalogowania - w settings dopisujemy gdzie ma byc wtedy odsyłany użytkownik
def profile(request):                                               #po wejściu w zakładkę edycja profilu można zmienić dane profilu, dodać zdjęcie itd, tu najlepiej obczaić to w kursie, bo nie wytłumaczę dokładnie
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Wprowadzono zmiany profilu')
            return redirect('profile')


    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render (request, 'users/profile.html', context)

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Tizimga muvaffaqiyatli kirdingiz.')
                return redirect('home')  # Home sahifaga yo'naltirish
            else:
                messages.error(request, 'Login yoki parol noto‘g‘ri.')
        else:
            messages.error(request, 'Forma noto‘g‘ri to‘ldirilgan.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



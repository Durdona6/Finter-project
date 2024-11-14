from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm

def contactView(request):
    contacts = Contact.objects.all()  # Barcha contact ma'lumotlarini olish
    form = ContactForm(request.POST or None, initial={'select_service': 'ONE'})  # Formani boshlang'ich qiymatlari bilan yaratish
    if request.method == 'POST':
        if form.is_valid():  # Formani tekshirish
            form.save()  # Ma'lumotlarni saqlash
            return redirect('index')  # So'nggi sahifaga qaytish
    return render(request, 'contact.html', context={
        'contacts': contacts,
        'forms': form,  # Formani konteksta yuborish
    })

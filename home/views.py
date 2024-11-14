from django.shortcuts import render, redirect
from about.models import About
from services.models import Service
from team.models import Team
from .models import Home, Index
from contact_us.models import Contact
from contact_us.forms import ContactForm

def indexView(request):
    home = Home.objects.first()  # Faqat birinchi Home obyekti, ya'ni sayt konfiguratsiyasi
    index = Index.objects.all()
    contacts = Contact.objects.all()  # Barcha contact ma'lumotlarini olish
    form = ContactForm(request.POST or None, initial={'select_service': 'ONE'})  # Formani boshlang'ich qiymatlari bilan yaratish
    if request.method == 'POST':
        if form.is_valid():  # Formani tekshirish
            form.save()  # Ma'lumotlarni saqlash
            return redirect('index')  # So'nggi sahifaga qaytish
    about = About.objects.all()
    services = Service.objects.all()
    team = Team.objects.all()
    return render(request, 'index.html', context={
        'abouts': about,
        'services': services,
        'teams': team,
        'homes': home,  # Home modelidan ma'lumotni uzatish
        'indexs': index,  # Index modelidan ma'lumotni uzatish
        'forms' : form,
        'contacts': contacts,  # Contact modelidan ma'lumotni uzatish
    })

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.conf import settings
from .models import SiteAppearance


def home(request):
    # Mengambil data warna (buat otomatis jika belum ada di database)
    appearance, created = SiteAppearance.objects.get_or_create(id=1)

    context = {
        'bg_color': appearance.background_color
    }
    return render(request, 'home.html', context)


# Decorator ini memastikan hanya user yang login yang bisa mengeksekusi fungsi ini
@login_required
def edit_background(request):
    # Hanya ALLOWED_MEMBERS yang boleh melakukan perubahan
    if request.user.email not in settings.ALLOWED_MEMBERS:
        return HttpResponseForbidden("Anda tidak memiliki izin untuk mengubah tampilan website.")

    if request.method == 'POST':
        new_color = request.POST.get('bg_color')
        if new_color:
            appearance, created = SiteAppearance.objects.get_or_create(id=1)
            appearance.background_color = new_color
            appearance.save()

    return redirect('home')
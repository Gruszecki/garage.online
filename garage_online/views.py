from django.shortcuts import render


# Create your views here.
def dashboard(request):
    # from django.core.mail import send_mail
    #
    # send_mail(
    #     'Subject here',
    #     'Udało się, extr@',
    #     'from@example.com',
    #     ['aptivtrash@gmail.com'],
    #     fail_silently=False,
    # )
    return render(request, 'garage_online/dashboard.html')

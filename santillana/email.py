from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.utils.html import strip_tags


def send_mail(request):

    context = {'userName': request.POST['userName'] ,
               'lastName': request.POST.get("lastName"),
               'phoneNumber': request.POST["phoneNumber"],
               'email': request.POST.get("email"),
               'questions': request.POST.get("questions"),
               }
    
    message = get_template('./santillana/correo.html').render(context)
    plantilla = strip_tags(message)
    msg = EmailMultiAlternatives('Preguntas y Comentarios',
                                plantilla,
                                settings.EMAIL_HOST_USER,
                                ['bperezm@minsait.com',]
                                )

    msg.attach_alternative(message, "text/html")
    
    if msg.send():
        return True
    else:
        return False

from django.core.mail import send_mail
from rest_framework import status
from rest_framework.response import Response
from django.conf import settings
from rest_framework.decorators import api_view

@api_view(['POST'])
def sendEemail(request):
    print(request.data)
    if request.method == 'POST':
        subject = request.data['subject']
        message = request.data['message']
        email = request.data['email']
        # recipient_list = request.data['recipient_list']
        # send_mail(subject, message, [email])
        send_mail(subject, message,from_email=settings.EMAIL_HOST_USER, recipient_list=[email])
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)
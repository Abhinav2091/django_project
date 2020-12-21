from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name= request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        #Check if user already made enquirey
        if request.user.is_authenticated:
            used_id=request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
            if has_contacted:
                messages.error(request,'You have alredy made query for this listing')
                return redirect('/listings/'+listing_id)

        contact =Contact(listing=listing,listing_id=listing_id,name=name,email=email,phone=phone,message=message,user_id=user_id)

        contact.save()

        #Send Email(Subject,message,email from,to)
        send_mail(
            "Property listing enquirey","There has been an inquery for "+listing+". Sign into admin portal for more Info",
            "from email",[realtor_email],
            fail_silently=False
        )

        messages.success(request,'Your request is submitted, a realtor will get back to you.')

        return redirect('/listings/'+listing_id)

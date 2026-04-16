from django.shortcuts import render
from .forms import contactForm
from django.core.mail import send_mail 

# Create your views here.
def about_me_view(request):
    return render(request, 'pages/about_me.html')

def experince(request):
    return render(request, 'pages/experince.html')

def contact_view(request):
    return render(request, 'pages/contact.html')

def contact_view(request):
    # means the from is submitted an not empty 
    # to send email
    if request.method == 'POST':
        form = contactForm(request.POST)
        #collect the data from teh form and send email
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            #Build the full email content
            message_body =(
                f'You have a new email from your portfolio \n'
                f'Name: {name} \n'
                f'Email: {email} \n'
                f'Message: {message} \n'
            )
            try:
                # Send the email using Django's send_mail function
                send_mail(
                    "Email From Portfolio", #subject
                    message_body, #message
                    email, #from email
                    ['jonmaso@gmail.com'],
                )
                form = contactForm()
                return render(request, 'pages/contact.html', {'form': form})
            except Exception as e:
                print(f'Error sending email: {e}')
                return render(request, 'pages/contact.html', {'form': form})
            else: 
                print ("Form is not valid")
                print (form.errors)
                return render(request, 'pages/contact.html', {'form': form})
    else:
        form = contactForm()
        return render(request, 'pages/contact.html', {'form': form})
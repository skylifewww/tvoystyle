from django.views.generic import TemplateView
from django.shortcuts import render_to_response, render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from tvoy_style.forms import *
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context


# from collection.forms import ContactForm

# add to your views
 
 
def contact(request):

    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the 
            # contact information
            template = get_template('contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })
            content = template.render(context)

            email = EmailMessage(
                u"Пришел новый заказ",
                content,
                "Your website" +'',
                ['skylifewww@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('/')

    return render(request, 'contact.html', {
        'form': form_class,
    })


# def thanks(request):
#     return render_to_response('thanks.html')


def index(request):
    form_class = ContactForm

    # return_path_f(request)
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the 
            # contact information
            template = get_template('contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })
            content = template.render(context)

            email = EmailMessage(
                u"Задан новый вопрос",
                content,
                "Your website" +'',
                ['skylifewww@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('/') 
    

    return render(request, 'index.html', {
        'form': form_class,
    })




# class MainView(TemplateView):
#     template_name = 'main.html'


# main = MainView.as_view()




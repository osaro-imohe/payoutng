
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from bs4 import BeautifulSoup
import requests
from django.urls import reverse
from django.shortcuts import render
from .forms import ContactForm
from .models import CustomUser
import datetime
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import get_template
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart







def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        posts = CustomUser.objects.all()
        if form.is_valid():
            print(posts)
            #form.save() -- this is what is used to save the form unquote this to save form to custo user
            request.session['brand'] = form.cleaned_data['brand']
            request.session['model'] = form.cleaned_data['model']
            request.session['email'] = form.cleaned_data['email']
            request.session['your_name'] = form.cleaned_data['your_name']
            form = ContactForm()
            brand = request.POST.get('brand').upper
            model = request.POST.get('model').upper
            brandquote = str(brand)
            modelquote = str(model)
            args = {'form': form, 'posts':posts,}
            url1 ='https://www.ebay.com/sch/i.html?_from=R40&_sacat=0&LH_BIN=1&_nkw='
            url2= '&_dcat=9355&rt=nc&LH_ItemCondition=3000'
            url = (url1 + str(request.POST.get('brand')) + '+' + str(request.POST.get('model')) + url2)
            source = requests.get(url).text
            print(url)
            soup =BeautifulSoup(source, 'lxml')



            total_price = 0
            for post in soup.find_all("li",{"class" : "s-item"}):
                price = post.find_all("span", {"class" : "s-item__price"})[0].text
                price2 = price.strip( '$' )
                price3 = price2.replace(",", "")
                price4 = price3[0:5]
                price5 = float(price4)
                price6 = round(price5)
                total_price = total_price + price6
                average = total_price / 50
                average1= average/100
                rounder = round(average1 * 50)
                quote = rounder * 362
                quote2 = round(quote * 1.6)
                print("₦%d" % quote)
            return render(request, 'quote/home2.html',{'brand':brand,'model':model, 'quote' : quote,'quote2': quote2, 'date':datetime.date.today() + datetime.timedelta(days=1),'date2':datetime.date.today() + datetime.timedelta(days=2),'date3':datetime.date.today() + datetime.timedelta(days=3),})
    else:
        form = ContactForm()
    return render(request, 'quote/home.html', {'form': form})
def offer(request):
    if request.method == 'POST':
        print(request.POST)
        state = request.POST.get('state')
        city = request.POST.get('city')
        address = request.POST.get('address')
        date = request.POST.get('date')
        time = request.POST.get('time') + 'PM'
        number = request.POST.get('number')
        brand = request.session['brand']
        model = request.session['model']
        email = request.session['email']
        your_name = request.session['your_name']
        url1 ='https://www.google.com/maps/place/'
        url = url1 + str(request.POST.get('city')) + ',' + str(request.POST.get('state'))
        source = requests.get(url).text
        soup =BeautifulSoup(source, 'lxml')

        my_email = 'payout.info.ng@gmail.com'
        my_password = 'Juggernaut9901#'
        send_to_email2 = 'osaroimohe98@gmail.com'
        send_to_email = email
        subject = "Your pickup has been confirmed"
        message = "Dear" + " " + your_name + "," + "\n\nThis is a reminder that you have booked for a free Inspection and pickup for your" + " " + brand.upper() + " " + model.upper() + "." + "\n\n Your pickups details:" + "\n Address:" + address + "," + city + "," + state + "\n Appointment Date:" + date + "\n Appointment Time:" + time +"\n\n\nWe look forward to seeing you!"+"\nFor further enquiries, please contact us through the following channels:" + "\n\nPhone:0814-906-7252" + "\nemail: payout.info.ng@gmail.com" + "\n\n\nWarm regards," + "\nPayout Support Team"
        msg = MIMEMultipart()
        msg['payout.info.ng@gmail.com'] = my_email
        msg[email] = send_to_email
        msg['osaroimohe98@gmail.com'] = send_to_email2
        msg['subject'] = subject

        msg.attach(MIMEText(message,'plain'))
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(my_email, my_password)
        text = msg.as_string()
        server.sendmail(my_email,send_to_email,text)
        server.sendmail(my_email,send_to_email2,text)
        server.quit()


        print(url)
        return render(request, 'quote/offer.html', {'state':state, 'address':address,'date':date,'time':time, 'number':number,'email':email, 'your_name':your_name,'brand':brand,'model':model,'city':city,})

    else:
        return redirect('quote:home')


def index(request):
    return render(request, 'quote/home.html')

def about(request):
    return render(request, 'quote/about.html')

def contact(request):
    return render(request, 'quote/contact.html')

def blog(request):
    return render(request, 'quote/blog.html')

def faq(request):
    return render(request, 'quote/faq.html')

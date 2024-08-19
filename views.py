from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from myapp.models import *


def home(request):
    return render(request,"Admin/home.html")


def login(request):
    return render(request,"login.html")

def loginpost(request):
    username=request.POST['textfield']
    password=request.POST['textfield2']
    lg=Login.objects.filter(username=username,password=password)
    if lg.exists():
        lg2=Login.objects.get(username=username,password=password)
        request.session['lid']=lg2.id
        if lg2.type=="admin":
            return HttpResponse('''<script>alert("success");window.location='/myapp/home/'</script>''')
        else:
            return HttpResponse('''<script>alert("success");window.location='/myapp/login/'</script>''')
    else:
        return HttpResponse('''<script>alert("login falied");window.location='/myapp/login/'</script>''')


def add_company(request):
    return render(request, "Admin/Company.html")

def addcompanypost(request):
    name=request.POST['name']
    email=request.POST['email']
    phoneno=request.POST['phoneno']
    street=request.POST['street']
    district=request.POST['district']
    pincode=request.POST['pincode']
    establisheddate=request.POST['establisheddate']
    logo=request.FILES['logo']

    # image
    date=datetime.now().strftime('%Y%m%d-%H%M%S')
    fs=FileSystemStorage()
    fs.save(date,logo)
    logopath=fs.url(date)

    cc=Company()
    cc.company_name=name
    cc.email=email
    cc.phoneno=phoneno
    cc.street=street
    cc.district=district
    cc.pincode=pincode
    cc.established_date=establisheddate
    cc.logo=logopath
    cc.save()
    return HttpResponse("""<script>alert("success");window.location='/myapp/home/'</script>""")



def edit_company(request):
    return render(request,"Admin/Company edit.html")

def editcompanypost(request):
    name=request.POST['name']
    email=request.POST['email']
    phoneno=request.POST['phoneno']
    street=request.POST['street']
    district=request.POST['district']
    establisheddate=request.POST['establisheddate']
    logo=request.POST['logo']
    return

def view_company(request):
    cc=Company.objects.all()
    return render(request,"Admin/company view.html",{"data":cc})



def add_vehicle(request):
    return render(request,"Admin/vehicle manage.html")

def vehicleaddpost(request):
    vehicle=request.POST['vehicle']
    photo=request.POST['photo']
    feature=request.POST['feature']
    driver=request.POST['driver']
    brand=request.POST['brand']
    regno=request.POST['regno']
    typeofvehicle=request.POST['typeofvehicle']
    amountperhour=request.POST['amountperhour']
    return

def edit_vehicle(request):
    return render(request,"Admin/vehicle dit.html")

def view_vehicle(request):
    return render(request,"Admin/view vehicle.html")

def add_report(request):
    return render(request,"Admin/monthly report.html")

def edit_report(request):
    return render(request,"Admin/report edit.html")

def view_report(request):
    return render(request,"Admin/report view.html")

def view_complaint(request):
    return render(request,"Admin/complaint view.html")

def send_reply(request):
    return render(request,"Admin/Reply.html")

def change_password(request):
    return render(request,"Admin/Admin chane password.html")

def view_booking(request):
    return render(request,"Admin/view  booking and accept admin.html")

def view_acceptbooking(request):
    return render(request,"Admin/view approved booking.html")

def view_request(request):
    return render(request,"Admin/view Request admin.html")

def update_booking(request):
    return render(request,"Admin/update extended.html")

def view_payment(request):
    return render(request,"Admin/view payment admin.html")

def update_payment(request):
    return render(request,"Admin/upate payment.html")

def view_review(request):
    return render(request,"Admin/view review admin.html")





#user


def register(request):
    return render(request,"user/Register.html")

def view_profile(request):
    return render(request,"user/view profile.html")

def edit_profile(request):
    return render(request,"user/profile edit.html")

def change_password_user(request):
    return render(request, "user/user change password.html")

def view_company_user(request):
    return render(request, "user/company view user.html")

def view_vehicle_user(request):
    return render(request, "user/view vehicle user.html")

def add_booking(request):
    return render(request, "user/booking user.html")

def view_status(request):
    return render(request, "user/view booking status user.html")

def send_request(request):
    return render(request, "user/Send request user.html")

def view_paymentstatus_user(request):
    return render(request, "user/view payment status user.html")

def send_complaint(request):
    return render(request, "user/send complaint user.html")

def view_reply(request):
    return render(request,"user/view reply.html")

def send_review(request):
    return render(request, "user/send review user.html")







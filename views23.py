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
    if request.session['lid'] == '':
        return HttpResponse('''<script> alert ('error occured');window.location='/myapp/home/'</script>''')
    else:
        return render(request, "Admin/Company.html")

def addcompanypost(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script> window.location='/myapp/home/'</script>''')
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



def edit_company(request,id):
    s=Company.objects.get(id=id)
    return render(request,"Admin/Company edit.html",{'data':s})

def editcompanypost(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script> window.location='/myapp/home/'</script>''')
    name=request.POST['name']
    email=request.POST['email']
    phoneno=request.POST['phoneno']
    street=request.POST['street']
    district=request.POST['district']
    pincode=request.POST['pincode']
    establisheddate=request.POST['establisheddate']
    id=request.POST['id']

    cc=Company.objects.get(id=id)

    if 'logo' in request.FILES:
        logo = request.FILES['logo']

        date=datetime.now().strftime('%Y%m%d-%H%M%S')
        fs=FileSystemStorage()
        fs.save(date,logo)
        logopath=fs.url(date)
        cc.logo=logopath
        cc.save()

    cc.company_name=name
    cc.email=email
    cc.phoneno=phoneno
    cc.street=street
    cc.district=district
    cc.pincode=pincode
    cc.established_date=establisheddate
    cc.save()
    return HttpResponse("""<script>alert("success");window.location='/myapp/viewcompany/'</script>""")


def view_company(request):
    cc=Company.objects.get(id=request.session['lid'])
    return render(request,"Admin/company view.html",{"data":cc})

def add_driver(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script> alert ('error occured');window.location='/myapp/home/'</script>''')
    else:
        return render(request,"Admin/driver add.html")

def adddriverpost(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script> window.location='/myapp/home/'</script>''')
    name=request.POST['name']
    dob=request.POST['dob']
    house=request.POST['house']
    street=request.POST['street']
    district=request.POST['district']
    pincode=request.POST['pincode']
    state=request.POST['state']
    gender=request.POST['gender']
    phoneno1=request.POST['phoneno1']
    phoneno2=request.POST['phoneno2']
    email=request.POST['email']


    dr=Driver()

    dr.name=name
    dr.DOB=dob
    dr.house=house
    dr.street=street
    dr.district=district
    dr.pincode=pincode
    dr.state=state
    dr.gender=gender
    dr.phoneno1=phoneno1
    dr.phoneno2=phoneno2
    dr.email=email
    dr.save()


    return HttpResponse("""<script>alert("success");window.location='/myapp/home/'</script>""")


def edit_driver(request,id):
    if request.session['lid'] == '':
        return HttpResponse('''<script> window.location='/myapp/home/'</script>''')
    else:
        d=Driver.objects.get(id=id)
        return render(request,"Admin/driver edit.html",{'data':d})

def editdriverpost(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script> window.location='/myapp/home/'</script>''')

    name=request.POST['name']
    dob=request.POST['dob']
    house=request.POST['house']
    street=request.POST['street']
    district=request.POST['district']
    pincode=request.POST['pincode']
    state=request.POST['state']
    gender=request.POST['gender']
    phoneno1=request.POST['phoneno1']
    phoneno2=request.POST['phoneno2']
    email=request.POST['email']
    id=request.POST['id']

    dr = Driver.objects.get(id=id)
    dr.name=name
    dr.DOB=dob
    dr.house=house
    dr.street=street
    dr.district=district
    dr.pincode=pincode
    dr.state=state
    dr.gender=gender
    dr.phoneno1=phoneno1
    dr.phoneno2=phoneno2
    dr.email=email
    dr.save()


    return HttpResponse("""<script>alert("success");window.location='/myapp/viewdriver/'</script>""")


def view_driver(request):
    dr=Driver.objects.all()
    return render(request,"Admin/driver view.html",{"data":dr})

def search_driver(request):
    # if request.session['lid'] == '':
    #     return HttpResponse('''<script> window.location='/myapp/home/'</script>''')
    search=request.POST['searchs']
    obj=Driver.objects.filter(name=search)
    return render(request,'admin/driver view.html', {'data':obj})

def deletedriver(request, id):
    Driver.objects.get(id=id).delete()
    return HttpResponse("""<script>alert("success");window.location='/myapp/viewdriver/'</script>""")


def add_vehicle(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script> window.location='/myapp/home/'</script>''')
    else:
        va=Driver.objects.all()
        return render(request,"Admin/vehicle manage.html",{'data':va})

def addvehiclepost(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script> window.location='/myapp/home/'</script>''')
    vehicle=request.POST['vehicle']
    photo=request.FILES['photo']
    feature=request.POST['feature']
    driver=request.POST['driver']
    brand=request.POST['brand']
    regno=request.POST['regno']
    typeofvehicle=request.POST['typeofvehicle']
    amountperhour=request.POST['amountperhour']

     #image
    date = datetime.now().strftime('%Y%m%d-%H%M%S')
    fs = FileSystemStorage()
    fs.save(date, photo)
    photopath = fs.url(date)


    ve=Vehicle()
    ve.vehicle=vehicle
    ve.photo=photopath
    ve.category=feature
    ve.DRIVER_id=driver
    ve.brand=brand
    ve.regno=regno
    ve.typeofvehicle=typeofvehicle
    ve.amountperhour=amountperhour
    ve.save()


    return HttpResponse("""<script>alert("success");window.location='/myapp/home/'</script>""")


def edit_vehicle(request,id):
    ve = Vehicle.objects.get(id=id)

    return render(request, "Admin/vehicle dit.html", {'data': ve})


def editvehiclepost(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script> window.location='/myapp/home/'</script>''')
    vehicle=request.POST['vehicle']
    photo=request.FILES['photo']
    feature=request.POST['feature']
    driver=request.POST['driver']
    brand=request.POST['brand']
    regno=request.POST['regno']
    typeofvehicle=request.POST['typeofvehicle']
    amountperhour=request.POST['amountperhour']

    id=request.POST['id']

    ve=Vehicle.objects.get(id=id)

    if 'photo' in request.FILES:
        photo = request.FILES['photo']
    # image
    date = datetime.now().strftime('%Y%m%d-%H%M%S')
    fs = FileSystemStorage()
    fs.save(date, photo)
    photopath = fs.url(date)
    ve.photo=photopath
    ve.save()


    ve.vehicle = vehicle
    ve.photo = photopath
    ve.category = feature
    ve.DRIVER_id = driver
    ve.brand = brand
    ve.regno = regno
    ve.typeofvehicle = typeofvehicle
    ve.amountperhour = amountperhour
    ve.save()

    return HttpResponse("""<script>alert("success");window.location='/myapp/viewvehicle/'</script>""")


def view_vehicle(request):
    vv=Vehicle.objects.all()
    return render(request,"Admin/view vehicle.html",{"data":vv})





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







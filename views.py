from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
# def login(request):
#     return render(request,'Login.html')
from myapp.models import *

def admin_home(request):
    return render(request,"aindex.html")


def admin_login(request):
    return render(request,"loginindex.html")


def login_post(request):
    username=request.POST['textfield']
    password=request.POST['textfield2']
    if login.objects.filter(username=username,password=password).exists():
        res=login.objects.get(username=username,password=password)
        request.session['lid']=res.id
        if res.type=="admin":
            return redirect("/myapp/adminhome/")
        else:
            return HttpResponse("<script> alert('Not Found');window.location='/myapp/login/'</script>")
    else:
        return HttpResponse("<script>alert('Not Foound');window.location='/myapp/login/'</script>")

def view_user(request):
    obj = user.objects.all()
    return render(request,'View user.html',{'data':obj})

def view_user_post(request):
    search = request.POST['textfield']
    obj = user.objects.filter(name__icontains=search)
    return render(request,'View user.html',{'data':obj})


def admin_view_rating(request):
    res=review.objects.all()
    return render(request,"view rating.html",{'data':res})


def admin_view_rating_post(request):
    fromdate=request.POST['texfield']
    todate=request.POST['textfield2']
    print(fromdate)
    res=review.objects.filter(date__range=[fromdate,todate])
    return render(request, "view rating.html",{'data':res})

def add_notification(request):
    return render(request,'notification.html')

def add_notification_post(request):
    notification = request.POST['textarea']

    res = Notification()
    res.notification=notification
    from datetime import datetime
    res.date=datetime.now().today()
    res.save()
    return HttpResponse("<script>alert('Added');window.location='/myapp/add_notification/'</script>")


def notification(request):
    res = Notification.objects.all()
    return render(request,'Notification management.html',{'data':res})

def notification_post(request):
    fromdate=request.POST['frm']
    todate=request.POST['to']
    print(fromdate)
    res=Notification.objects.filter(date__range=[fromdate,todate])
    return render(request, "Notification management.html",{'data':res})

def delete_notification(request,id):
    data = Notification.objects.get(id=id)
    data.delete()
    return HttpResponse("<script>alert('Deleted');window.location='/myapp/notification/'</script>")

def view_blk_users(request):

    return render(request,'view blk req _users.html')

def view_blk_drivers(request):
    return render(request,'view blk req_drivers.html')

def view_detection(request):
    res = Record.objects.all()
    return render(request,'view detection records.html',{'data':res})

def report(request):
    res = Report.objects.all()
    return render(request,'reports.html',{'data':res})

def report_post(request):
    fromdate = request.POST['textfield']
    todate = request.POST['textfield2']
    res = Report.objects.filter(Date__range=[fromdate,todate])
    return render(request,'reports.html',{'data':res})

def driver(request):
    res = Driver.objects.filter(status='pending')
    return render(request,'view driver and verify.html',{'data':res})

def driver_post(request):
    search = request.POST['textfield']
    res = Driver.objects.filter(status='pending',givennamed__icontains=search)
    return render(request,'view driver and verify.html',{'data':res})

def admin_approve_driver(request,id):
    res=Driver.objects.filter(LOGIN=id).update(status='approved')
    ress=login.objects.filter(id=id).update(type='driver')
    return HttpResponse("<script> alert('Approved');window.location='/myapp/driver/'</script>")



def admin_reject_driver(request,id):
    res=Driver.objects.filter(LOGIN=id).update(status='reject')
    ress=login.objects.filter(id=id).update(type='reject')
    return HttpResponse("<script> alert('reject');window.location='/myapp/driver/'</script>")

def approved_driver(request):
    res = Driver.objects.filter(status='approved')
    return render(request,'approved driver.html',{'data':res})

def approved_driver_post(request):
    search = request.POST['textfield']
    res = Driver.objects.filter(status='approved',givennamed__icontains=search)
    return render(request,'approved driver.html',{'data':res})

def reject_driver(request):
    res = Driver.objects.filter(status='reject')
    return render(request,'rejected driver.html',{'data':res})

def reject_driver_post(request):
    search = request.POST['textfield']
    res = Driver.objects.filter(status='reject',givennamed__icontains=search)
    return render(request,'rejected driver.html',{'data':res})

def admin_view_user_complaints(request):
    res=complaints.objects.all()
    return render(request,"view_user_complaints.html",{'data':res})


def admin_view_user_complaints_search(request):
    fromdate=request.POST['textfield']
    todate=request.POST['textfield2']
    res=complaints.objects.filter(date__range=[fromdate,todate])
    print(res)
    return render(request,"view_user_complaints.html",{'data':res})


def adminsentreplyuser(request):
    id=request.POST['cid']
    reply=request.POST['textarea']
    res=complaints.objects.filter(id=id).update(replay=reply,status="replied")
    return HttpResponse('''<script>alert('Sending Successfull');window.location="/myapp/admin_view_user_complaints/"</script>''')


def admin_view_user_request(request):
    res=UserRequest.objects.all()
    return render(request,"view blk req _users.html",{'data':res})


def admin_view_user_request_search(request):
    fromdate=request.POST['textfield']
    todate=request.POST['textfield2']
    res=UserRequest.objects.filter(date__range=[fromdate,todate])
    print(res)
    return render(request,"view blk req _users.html",{'data':res})


def adminsentactionuser(request):
    id=request.POST['cid']
    reply=request.POST['textarea']
    res=UserRequest.objects.filter(id=id).update(action=reply,status="replied")
    return HttpResponse('''<script>alert('Sending Successfull');window.location="/myapp/admin_view_user_request/"</script>''')



def admin_view_driver_request(request):
    res=DriverRequest.objects.all()
    return render(request,"view blk req_drivers.html",{'data':res})


def admin_view_driver_request_search(request):
    fromdate=request.POST['textfield']
    todate=request.POST['textfield2']
    res=DriverRequest.objects.filter(date__range=[fromdate,todate])
    print(res)
    return render(request,"view blk req_drivers.html",{'data':res})


def adminsentreplydriver(request):
    id=request.POST['cid']
    reply=request.POST['textarea']
    res=DriverRequest.objects.filter(id=id).update(action=reply,status="replied")
    return HttpResponse('''<script>alert('Sending Successfull');window.location="/myapp/admin_view_driver_request/"</script>''')







##############################


def and_login(request):
    uname = request.POST['name']
    password = request.POST['password']

    lobj = login.objects.filter(username=uname, password=password)

    if lobj.exists():
        lobj1 = login.objects.get(username=uname, password=password)
        if lobj1.type == 'driver':
            lid = lobj1.id
            return JsonResponse({'status': 'ok', 'lid': str(lid), 'type': lobj1.type})

        elif lobj1.type == 'user':
            lid = lobj1.id
            return JsonResponse({'status': 'ok', 'lid': str(lid), 'type': lobj1.type})

        else:
            return JsonResponse({'status': 'no'})

    else:
        return JsonResponse({'status': 'no'})


def signup(request):
    givennamed = request.POST['name']
    taximodel = request.POST['taximodel']
    number = request.POST['number']
    seat = request.POST['seat']
    place = request.POST['place']
    email = request.POST['email']
    contact = request.POST['contact']
    photo = request.POST['photo']
    idproof = request.POST['idproof']
    password = request.POST['password']
    confirmpassword = request.POST['confirm']

    from datetime import datetime
    date = datetime.now().strftime("%Y-%m-%d%H-%M-%S") + ".jpg"
    import base64
    fs = base64.b64decode(photo)
    # open(r'C:\\Users\\anusr\\PycharmProjects\\ShareMyRide\\media\\user\\' + date, 'wb').write(fs)
    open(r'C:\\Users\\SHAIMA\\Downloads\\SHARE_MY_RIDE\\SHARE_MY_RIDE\\ShareMyRide\\ShareMyRide\\media\\user\\' + date, 'wb').write(fs)
    path = '/media/user/' + date

    from datetime import datetime
    date1 = datetime.now().strftime("%Y-%m-%d%H-%M-%S") + ".jpg"
    import base64
    fs1 = base64.b64decode(idproof)
    # open(r'C:\\Users\\anusr\\PycharmProjects\\GetMeHelper\\media\\user\\lic\\' + date1, 'wb').write(fs1)
    # open(r'C:\\Users\\anusr\\PycharmProjects\\ShareMyRide\\media\\id\\' + date1, 'wb').write(fs1)
    open(r'C:\\Users\\SHAIMA\\Downloads\\SHARE_MY_RIDE\\SHARE_MY_RIDE\\ShareMyRide\\ShareMyRide\\media\\id\\' + date1, 'wb').write(fs1)
    path1 = '/media/id/' + date1

    lobj = login()
    lobj.username = email
    lobj.password = confirmpassword
    lobj.type = 'pending'
    lobj.save()

    if password == confirmpassword:
        tobj = Driver()
        tobj.photo = path
        tobj.idproof = path1
        tobj.givennamed = givennamed
        tobj.taximodel = taximodel
        tobj.number = number
        tobj.seat = seat
        tobj.place = place
        tobj.email = email
        tobj.contact = contact
        tobj.status = 'pending'
        tobj.LOGIN = lobj
        tobj.save()

    return JsonResponse({'status': 'ok'})

def driver_view_profile(request):
    lid=request.POST['lid']
    res=Driver.objects.get(LOGIN=lid)
    return JsonResponse({'status':'ok','id':'id',
                         'name':res.givennamed,
                         'taximodel':res.taximodel,
                         'number':res.number,
                         'seat':res.seat,
                         'place':res.place,
                         'email':res.email,
                         'contact':res.contact,
                         'photo':res.photo,
                         'idproof':res.idproof})


def driver_view_notification(request):
    res = Notification.objects.all()
    l=[]
    for i in res:
        l.append({'id':i.id,'date':i.date,'notification':i.notification})
        return JsonResponse({'status':'ok','data':l})


def add_ride(request):
    Date = request.POST['Date']
    Time = request.POST['Time']
    Destination = request.POST['Destination']
    source = request.POST['source']
    Typeofvehicle = request.POST['Typeofvehicle']
    seats = request.POST['seats']
    lid = request.POST['lid']

    fobj = Journey()
    fobj.Date = Date
    fobj.Time = Time
    fobj.Destination = Destination
    fobj.source = source
    fobj.Typeofvehicle = Typeofvehicle
    fobj.seats = seats
    fobj.DRIVER= Driver.objects.get(LOGIN_id=lid)
    fobj.save()
    return JsonResponse({'status': "ok"})

def view_journey(request):
    lid = request.POST['lid']
    res = Journey.objects.filter(DRIVER__LOGIN_id=lid)
    l = []
    for i in res:
        l.append({'id': i.id, 'Date': i.Date,
                  'Time': i.Time,
                  'Destination': i.Destination,
                  'source': i.source,
                  'Typeofvehicle': i.Typeofvehicle,
                  'seats': i.seats})
    return JsonResponse({'status': "ok","data":l})

def edit_journey(request):
    sid = request.POST['sid']
    i = Journey.objects.get(id=sid)
    return JsonResponse({'status':'ok','id': i.id,
                         'Date': i.Date,
                         'Time': i.Time,
                         'Destination': i.Destination,
                         'source': i.source,
                         'Typeofvehicle': i.Typeofvehicle,
                         'seats': i.seats})

def update_journey(request):
    lid=request.POST['lid']
    sid = request.POST['sid']
    Date = request.POST['Date']
    Time = request.POST['Time']
    Destination = request.POST['Destination']
    source = request.POST['source']
    Typeofvehicle = request.POST['Typeofvehicle']
    seats = request.POST['seats']

    fobj = Journey.objects.get(id=sid)
    fobj.Date = Date
    fobj.Time = Time
    fobj.Destination = Destination
    fobj.source = source
    fobj.Typeofvehicle = Typeofvehicle
    fobj.seats = seats
    fobj.save()
    return JsonResponse({'status': 'ok'})

def delete_journey(request):
    sid=request.POST["sid"]
    res=Journey.objects.get(id=sid).delete()
    return JsonResponse({'status':'ok'})



def driver_add_seat(request):
    sid = request.POST['sid']
    available = request.POST['available']
    booked = request.POST['booked']

    obj = Availableseats()
    obj.available=available
    obj.booked=booked
    obj.JOURNEY_id=sid
    obj.save()
    return JsonResponse({'status': 'ok'})

def driver_view_seats(request):
    lid = request.POST['lid']
    res = Availableseats.objects.filter(JOURNEY__DRIVER__LOGIN_id=lid)
    l=[]
    for i in res:
        l.append({'id':i.id,'journey':i.JOURNEY.Destination,
                  'available':i.available,
                  'booked':i.booked})
    return JsonResponse({'status':'ok','data':l})

def driver_edit_seat(request):
    sid = request.POST['sid']
    i = Availableseats.objects.filter(JOURNEY__DRIVER__LOGIN_id=sid)
    return JsonResponse({'status':'ok','journey':i.JOURNEY.Destination,
                         'available':i.available,'booked':i.booked})

def driver_update_seat(request):
    # id = request.POST['id']
    sid = request.POST['sid']
    available = request.POST['available']
    booked = request.POST['booked']

    obj = Availableseats.objects.get(id=sid)
    obj.available=available
    obj.booked=booked
    # obj.JOURNEY_id=rid
    obj.save()
    return JsonResponse({'status': 'ok'})

def delete_seat(request):
    sid=request.POST["sid"]
    res=Availableseats.objects.get(id=sid).delete()
    return JsonResponse({'status':'ok'})

def view_booking_user(request):
    res = Book.objects.filter(Booking='booked')
    l = []
    for i in res:
        l.append({'id': i.id, 'name': i.USER.name,
                  'idproof': i.USER.idproof,
                  'date': i.Date})
    return JsonResponse({'status': "ok", "data": l})

def Verify_user(request):
    lid = request.POST['lid']
    var = Book.objects.filter(id=lid).update(Status='confirmed')
    return JsonResponse({'status':'ok'})


def driver_send_block(request):
    lid = request.POST["lid"]
    uid = request.POST["sid"]
    from datetime import datetime
    date = datetime.now().date().today()
    request = request.POST["request"]
    status = "pending"
    action = 'pending'

    cobj = DriverRequest()
    cobj.date = date
    cobj.request = request
    cobj.status = status
    cobj.action = action
    cobj.DRIVER =Driver.objects.get(LOGIN_id=lid)
    cobj.USER_id=uid
    cobj.save()
    return JsonResponse({'status': 'ok'})

def driver_view_action(request):
    lid = request.POST['lid']
    sf = DriverRequest.objects.filter(DRIVER__LOGIN_id=lid)
    l = []
    for i in sf:
         l.append({'id':i.id,'date': i.date,
                   'complaint':i.request,
                   'status': i.status,
                   'reply': i.action})
    return JsonResponse({'status': 'ok', 'data': l})

# def driver_view_user(request):
#     res = user.objects.all()
#     l=[]
#     for i in res:
#         l.append({'id':i.id,'name':i.name,
#                   'Houseno':i.Houseno,
#                 'number':i.contact,
#                   'seat':i.seat,
#                   'place':i.place,
#                   'email':i.email,
#                 'contact':i.contact,
#                   'photo':i.photo,
#                   'idproof':i.idproof})
#         return JsonResponse({'status':'ok','data':l})

def driver_send_notif(request):
    lid = request.POST["lid"]
    uid = request.POST["uid"]
    from datetime import datetime
    date = datetime.now().date().today()
    complaint = request.POST["complaint"]
    status = "pending"
    reply = 'pending'

    cobj = Delay()
    cobj.date = date
    cobj.notification = complaint
    cobj.status = status
    cobj.reply = reply
    cobj.DRIVER = Driver.objects.get(LOGIN_id=lid)
    cobj.USER_id = uid
    cobj.save()
    return JsonResponse({'status': 'ok'})
def driver_send_notif(request):
    lid = request.POST["lid"]
    uid = request.POST["uid"]
    from datetime import datetime
    date = datetime.now().date().today()
    complaint = request.POST["complaint"]
    status = "pending"
    reply = 'pending'

    cobj = Delay()
    cobj.date = date
    cobj.notification = complaint
    cobj.status = status
    cobj.reply = reply
    cobj.DRIVER = Driver.objects.get(LOGIN_id=lid)
    cobj.USER_id = uid
    cobj.save()
    return JsonResponse({'status': 'ok'})
def user_rep_notif(request):
    uid = request.POST["did"]
    complaint = request.POST["complaint"]

    cobj = Delay.objects.get(id=uid)
    cobj.status = "Replied"
    cobj.replay = complaint
    cobj.save()
    return JsonResponse({'status': 'ok'})

def driver_view_n_reply(request):
    lid = request.POST['lid']
    sf = Delay.objects.filter(DRIVER__LOGIN_id=lid)
    l = []
    for i in sf:
         l.append({'id':i.id,'date': i.date, 'complaint':i.notification,'status': i.status, 'reply': i.replay})
    return JsonResponse({'status': 'ok', 'data': l})

def user_view_n_reply(request):
    lid = request.POST['lid']
    sf = Delay.objects.filter(USER__LOGIN_id=lid)
    l = []
    for i in sf:
         l.append({'id':i.id,'date': i.date, 'complaint':i.notification,'status': i.status, 'reply': i.replay})
    return JsonResponse({'status': 'ok', 'data': l})




######################  USER  #############




def user_signup(request):
    name = request.POST['name']
    Houseno = request.POST['Houseno']
    idproof = request.POST['idproof']
    photo = request.POST['photo']
    email = request.POST['email']
    contact = request.POST['contact']
    pincode = request.POST['pincode']
    gender = request.POST['gender']
    place = request.POST['place']
    post = request.POST['post']
    district = request.POST['district']
    area = request.POST['area']
    landmark = request.POST['landmark']
    password = request.POST['password']
    confirmpassword = request.POST['confirm']

    if password == confirmpassword:
        lobj = login()
        lobj.username = email
        lobj.password = confirmpassword
        lobj.type = 'user'
        lobj.save()

        tobj = user()

        from datetime import datetime
        date = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
        import base64
        fs = base64.b64decode(photo)
        open(r'C:\\Users\\SHAIMA\\Downloads\\SHARE_MY_RIDE\\SHARE_MY_RIDE\\ShareMyRide\\ShareMyRide\\media\\user\\' + date, 'wb').write(fs)
        # open(r'C:\\Users\\anusr\\PycharmProjects\\ShareMyRide\\media\\user\\' + date, 'wb').write(fs)
        path = '/media/user/' + date

        from datetime import datetime
        date1 = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
        import base64
        fs1 = base64.b64decode(idproof)
        # open(r'C:\\Users\\anusr\\PycharmProjects\\ShareMyRide\\media\\id\\' + date1, 'wb').write(fs1)
        open(r'C:\\Users\\SHAIMA\\Downloads\\SHARE_MY_RIDE\\SHARE_MY_RIDE\\ShareMyRide\\ShareMyRide\\media\\id\\' + date1, 'wb').write(fs1)
        path1 = '/media/id/' + date1

        tobj.photo = path
        tobj.idproof = path1
        tobj.name = name
        tobj.Houseno = Houseno
        tobj.idproof = idproof
        tobj.email = email
        tobj.contact = contact
        tobj.pincode = pincode
        tobj.gender = gender
        tobj.place = place
        tobj.post = post
        tobj.district = district
        tobj.area = area
        tobj.landmark = landmark
        tobj.LOGIN = lobj
        tobj.save()

    return JsonResponse({'status': 'ok'})

def user_view_profile(request):
    lid=request.POST['lid']
    res=user.objects.get(LOGIN=lid)
    return JsonResponse({'status':'ok','name':res.name,'Houseno':res.Houseno,
                         'idproof':res.idproof,'photo':res.photo,'email':res.email,
                         'contact':res.contact,'pincode':res.pincode,'gender':res.gender,
                         'place':res.place,'post':res.post,'district':res.district,
                         'area': res.area,'landmark':res.landmark,})

def user_editprofile(request):
    name = request.POST['name']
    Houseno = request.POST['Houseno']
    email = request.POST['email']
    contact = request.POST['contact']
    pincode = request.POST['pincode']
    gender = request.POST['gender']
    place = request.POST['place']
    post = request.POST['post']
    district = request.POST['district']
    area = request.POST['area']
    landmark = request.POST['landmark']
    idproof = request.POST['idproof']
    photo = request.POST['photo']
    lid=request.POST['lid']

    mobj = user.objects.get(LOGIN_id=lid)

    if len(photo) > 1:
        import base64
        from datetime import datetime
        date = datetime.now().strftime("%Y%m%d_%H%M%S") + ".jpg"
        import base64
        fs = base64.b64decode(photo)
        # open(r'C:\\Users\\anusr\\PycharmProjects\\GetMeHelper\\media\\user\\' + date, 'wb').write(fs)
        open(r'C:\\Users\\SHAIMA\\Downloads\\SHARE_MY_RIDE\\SHARE_MY_RIDE\\ShareMyRide\\ShareMyRide\\media\\user\\' + date, 'wb').write(fs)
        path = '/media/user/' + date
        mobj.photo = path
        mobj.save()

    if len(idproof) > 1:
        import base64
        from datetime import datetime
        date1 = datetime.now().strftime("%Y%m%d_%H%M%S") + ".jpg"
        import base64
        fs1 = base64.b64decode(idproof)
        open(r'C:\\Users\\SHAIMA\\Downloads\\SHARE_MY_RIDE\\SHARE_MY_RIDE\\ShareMyRide\\ShareMyRide\\media\\id\\' + date1, 'wb').write(fs1)
        # open(r'C:\\Users\\anusr\\PycharmProjects\\GetMeHelper\\media\\user\\lic\\' + date1, 'wb').write(fs1)
        path1 = '/media/id/' + date1
        mobj.idproof = path1
        mobj.save()


    mobj.name = name
    mobj.Houseno = Houseno
    mobj.email = email
    mobj.contact = contact
    mobj.pincode = pincode
    mobj.gender = gender
    mobj.place = place
    mobj.post = post
    mobj.district = district
    mobj.area = area
    mobj.landmark = landmark
    mobj.save()

    return JsonResponse({'status':"ok"})

def user_Changepassword(request):
    lid=request.POST["lid"]
    cpassword=request.POST["currentpassword"]
    npassword=request.POST["newpassword"]
    conpassword=request.POST["confirmpassword"]
    log=login.objects.filter(password=cpassword)
    if log.exists():
        log1 = login.objects.get(id=lid, password=cpassword)
        if npassword == conpassword:
            log1 = login.objects.filter(id=lid, password=cpassword).update(password = npassword)
            return JsonResponse({'status':'ok'})
        else:
            return JsonResponse({'status':'no'})
    else:
        return JsonResponse({'status': 'no'})

def view_driver(request):
    res = Driver.objects.all()
    l=[]
    for i in res:
        l.append({'id':i.id,'name':i.givennamed,'taximodel':i.taximodel,
                         'number':i.number,'seat':i.seat,'place':i.place,'email':i.email,
                         'contact':i.contact,'photo':i.photo,'idproof':i.idproof})
        return JsonResponse({'status':'ok','data':l})

def view_rating(request):
    lid = request.POST['lid']
    res = review.objects.all().exclude(LOGIN_id=lid)
    l=[]
    for i in res:
        l.append({'id':i.id,'date':i.date,'review':i.review,'rating':i.rating,'user':i.USER.name})
        return JsonResponse({'status':'ok','data':l})

def user_send_complaint(request):
    lid = request.POST["lid"]
    from datetime import datetime
    date = datetime.now().date().today()
    complaint = request.POST["complaint"]
    status = "pending"
    reply = 'pending'

    cobj = complaints()
    cobj.date = date
    cobj.complaint = complaint
    cobj.status = status
    cobj.reply = reply
    cobj.USER =user.objects.get(LOGIN_id=lid)
    cobj.save()
    return JsonResponse({'status': 'ok'})

def user_view_reply(request):
    lid = request.POST['lid']
    sf = complaints.objects.filter(USER__LOGIN_id=lid)
    l = []
    for i in sf:
         l.append({'id':i.id,'date': i.date, 'complaint':i.complaint,'status': i.status, 'reply': i.replay})
    return JsonResponse({'status': 'ok', 'data': l})


def view_new_journey(request):
    res = Availableseats.objects.all()
    l=[]
    for i in res:
        l.append({'id':i.id,'Destination':i.JOURNEY.Destination,
                  'Date':i.JOURNEY.Date,
                  'Time':i.JOURNEY.Time,
                  'available':i.available})
        return JsonResponse({'status':'ok','data':l})


def book_jorney(request):
    lid = request.POST['lid']
    sid = request.POST['sid']

    fobj = Book()
    from datetime import datetime
    fobj.Date = datetime.now().today()
    fobj.Booking = 'booked'
    fobj.Status = 'pending'
    fobj.USER = user.objects.get(LOGIN_id=lid)
    fobj.AVAILABLESEATS_id = sid
    fobj.save()
    return JsonResponse({'status':'ok'})


def view_book_status(request):
    lid = request.POST['lid']
    res = Book.objects.filter(USER__LOGIN_id=lid)
    l=[]
    for i in res:
        loc = Location.objects.filter(LOGIN=i.AVAILABLESEATS.JOURNEY.DRIVER.LOGIN)
        lat = ''
        lon = ''
        if loc.exists():
            lat = loc[0].lat
            lon = loc[0].lon
        l.append({'id':i.id,'jorney':i.AVAILABLESEATS.JOURNEY.Destination,
                  'Date':i.Date,
                  'lat':lat,
                  'lon':lon,
                  'Status':i.Status})
        return JsonResponse({'status':'ok','data':l})


def user_sendfeedback(request):
    lid=request.POST['lid']
    feedback=request.POST['feedback']


    fobj=Feedback()
    fobj.Feedback=feedback
    from datetime import datetime
    fobj.Date=datetime.now().today()
    fobj.USER=user.objects.get(LOGIN_id=lid)
    fobj.save()
    return JsonResponse({'status': "ok"})


def user_send_block(request):
    lid = request.POST["lid"]
    did = request.POST["did"]
    from datetime import datetime
    date = datetime.now().date().today()
    request = request.POST["request"]
    status = "pending"
    action = 'pending'

    cobj = UserRequest()
    cobj.date = date
    cobj.request = request
    cobj.status = status
    cobj.action = action
    cobj.USER =user.objects.get(LOGIN_id=lid)
    cobj.DRIVER_id=did
    cobj.save()
    return JsonResponse({'status': 'ok'})

def user_view_action(request):
    lid = request.POST['lid']
    sf = UserRequest.objects.filter(USER__LOGIN_id=lid)
    l = []
    for i in sf:
         l.append({'id':i.id,'date': i.date,
                   'complaint':i.request,
                   'status': i.status,
                   'reply': i.action})
    return JsonResponse({'status': 'ok', 'data': l})

def add_lost(request):
    lid = request.POST['lid']
    Object = request.POST['Object']
    Description = request.POST['Description']

    obj = Lost()
    from datetime import datetime
    obj.Date = datetime.now().today()
    obj.Object = Object
    obj.Description = Description
    obj.USER = user.objects.get(LOGIN_id = lid)
    obj.save()
    return JsonResponse({'status': 'ok'})

def view_lost(request):
    lid = request.POST['lid']
    lst = Lost.objects.filter(USER__LOGIN_id=lid)
    l = []
    for i in lst:
         l.append({'id':i.id,'Date': i.Date,
                   'Object':i.Object,
                   'Description': i.Description})
    return JsonResponse({'status': 'ok', 'data': l})

def view_others_lost(request):
    lid = request.POST['lid']
    lst = Lost.objects.exclude(USER__LOGIN_id=lid)
    l = []
    for i in lst:
         l.append({'id':i.id,'Date': i.Date,
                   'Object':i.Object,
                   'Description': i.Description,
                   'name':i.USER.name,
                   'contact': i.USER.contact,})
    return JsonResponse({'status': 'ok', 'data': l})

def delete_lost(request):
    sid=request.POST["sid"]
    res=Lost.objects.get(id=sid).delete()
    return JsonResponse({'status':'ok'})

def driver_view_user(request):
    res = user.objects.all()
    l=[]
    for i in res:
        print(i.id)
        l.append({'status':'ok','id':i.id,'name':i.name,
                         'contact':i.contact,
                  'email': i.email,
                  'place':i.place,
                  'post':i.post,
                    'district':i.district,
                    'pincode':i.pincode,
                  'photo':i.photo,
                  'idproof':i.idproof})
        return JsonResponse({'status':'ok','data':l})

def update_location(request):
    lid = request.POST['lid']
    lat = request.POST['lat']
    lon = request.POST['lon']
    obj = Location()
    if Location.objects.filter(LOGIN_id=lid).exists():
        obj = Location.objects.filter(LOGIN_id=lid)[0]
    obj.lat=lat
    obj.lon=lon
    obj.LOGIN_id=lid
    obj.save()
    return JsonResponse({'status': 'ok'})

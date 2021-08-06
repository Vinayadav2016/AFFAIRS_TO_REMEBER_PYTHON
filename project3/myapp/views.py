from django.shortcuts import render
from .models import*
from datetime import date
# Create your views here.

def homepage(request):
    success=False
    if request.method=='GET':
     return render(request,'homepage.html')
    if request.method=='POST':
        phone=request.POST.get('phone')
        user=book.objects.all().filter(phone=phone)
        user1=partyreg.objects.all().filter(phone=phone)
        success=True
        return render(request, 'homepage.html',{'user':user,'user1':user1,'success':success})


def details(request,name):
    success=False
    if request.method=='GET':
        hcom=usercom.objects.all().filter(hname=name)
        my_data=dinner.objects.all()
        for d in my_data:
            if d.hname==name:
                user=dinner.objects.get(hname=d.hname)
        return render(request,'details.html',{'user':user,'hcom':hcom})

    if request.method=='POST':
       if 'BOOK' in request.POST:
        hcom = usercom.objects.all().filter(hname=name)
        hname=request.POST.get('hname')
        user = dinner.objects.get(hname=hname)
        obj=book()
        obj.hname=request.POST.get('hname')
        obj.phone=request.POST.get('phone')
        obj.date=request.POST.get('date')
        obj.person=request.POST.get('person')
        obj.save()
        success=True
        return render(request, 'details.html', {'success': success,'user':user,'hcom':hcom})
       if 'ADD' in request.POST:

           hname = request.POST.get('hname')
           user = dinner.objects.get(hname=hname)
           obj = usercom()
           obj.hname = request.POST.get('hname')
           obj.pname= request.POST.get('pname')
           obj.comments=request.POST.get('comments')

           obj.save()
           success = True
           hcom = usercom.objects.all().filter(hname=name)
           return render(request, 'details.html', {'success1': success, 'user': user,'hcom':hcom})


def detailsd(request, name):
        success = False
        if request.method == 'GET':
            my_data = dinner.objects.all()
            for d in my_data:
                if d.hname == name:
                    user = dinner.objects.get(hname=d.hname)
            return render(request, 'detailsd.html', {'user': user})
        if request.method == 'POST':
            hname = request.POST.get('hname')
            user = dinner.objects.get(hname=hname)
            obj = book()
            obj.hname = request.POST.get('hname')
            obj.phone = request.POST.get('phone')
            obj.date = request.POST.get('date')
            obj.person = request.POST.get('person')
            obj.save()
            success = True
            return render(request, 'detailsd.html', {'success': success, 'user': user})
def dates(request):

    if request.method == 'GET':

        my_data = dinner.objects.all()
        ni="northindian"
        return render(request, "dates.html", {'my_data': my_data,'ni':ni})
    if request.method == 'POST':
        veg = request.POST.get('example1')
        nonveg = request.POST.get('example2')
        drinks = request.POST.get('example3')
        if veg == 'on' and nonveg == 'on' and drinks == 'on':
            name = "NON VEG & DRINKS & DRINKS"
            user = dinner.objects.all().filter(typef='both').filter(drinks='yes')
            return render(request, 'datesc.html', {'my_data': user, 'name': name})
        elif veg == 'on' and nonveg == 'on':
            name = "NON VEG & VEG"
            user = dinner.objects.all().filter(typef='both')
            return render(request, 'datesc.html', {'my_data': user, 'name': name})
        elif veg == 'on' and drinks == 'on':
            name = "VEG & DRINKS"
            user = dinner.objects.all().filter(typef='veg').filter(drinks='yes')
            user1 = dinner.objects.all().filter(typef='both').filter(drinks='yes')
            return render(request, 'datesc.html', {'my_data': user, 'my_data2': user1, 'name': name})
        elif nonveg == 'on' and drinks == 'on':
            name = "NON VEG & DRINKS"
            user = dinner.objects.all().filter(typef='non-veg').filter(drinks='yes')
            user1 = dinner.objects.all().filter(typef='both').filter(drinks='yes')
            return render(request, 'datesc.html', {'my_data': user, 'my_data2': user1, 'name': name})
        elif veg == 'on':
            name = "VEG"
            user = dinner.objects.all().filter(typef='veg')
            user1 = dinner.objects.all().filter(typef='both')
            return render(request, 'datesc.html', {'my_data': user, 'my_data2': user1, 'name': name})
        elif nonveg == 'on':
            name = "NON VEG"
            user = dinner.objects.all().filter(typef='non-veg')
            user1 = dinner.objects.all().filter(typef='both')
            return render(request, 'datesc.html', {'my_data': user, 'my_data2': user1, 'name': name})
        elif drinks == 'on':
            name = "Drinks"
            user = dinner.objects.all().filter(drinks='yes')
            return render(request, 'datesc.html', {'my_data': user, 'name': name})


def datesc(request, name):
        success = False
        if request.method == 'GET':


            user = dinner.objects.all().filter(cusine1=name)
            user2 = dinner.objects.all().filter(cusine2=name)
            user3 = dinner.objects.all().filter(cusine3=name)
            user4 = dinner.objects.all().filter(cusine4=name)
            return render(request, 'datesc.html', {'name1':name,'my_data': user,'my_data2':user2,'my_data3':user3,'my_data4':user4})
        if request.method == 'POST':
            veg = request.POST.get('example1')
            nonveg = request.POST.get('example2')
            drinks = request.POST.get('example3')
            if veg == 'on' and nonveg == 'on' and drinks == 'on':
                name = "NON VEG & DRINKS & DRINKS"
                user = dinner.objects.all().filter(typef='both').filter(drinks='yes')
                return render(request, 'datesc.html', {'my_data': user, 'name': name})
            elif veg == 'on' and nonveg == 'on':
                name = "NON VEG & VEG"
                user = dinner.objects.all().filter(typef='both')
                return render(request, 'datesc.html', {'my_data': user, 'name': name})
            elif veg == 'on' and drinks == 'on':
                name = "VEG & DRINKS"
                user = dinner.objects.all().filter(typef='veg').filter(drinks='yes')
                user1 = dinner.objects.all().filter(typef='both').filter(drinks='yes')
                return render(request, 'datesc.html', {'my_data': user, 'my_data2': user1, 'name': name})
            elif nonveg == 'on' and drinks == 'on':
                name = "NON VEG & DRINKS"
                user = dinner.objects.all().filter(typef='non-veg').filter(drinks='yes')
                user1 = dinner.objects.all().filter(typef='both').filter(drinks='yes')
                return render(request, 'datesc.html', {'my_data': user, 'my_data2': user1, 'name': name})
            elif veg == 'on':
                name = "VEG"
                user = dinner.objects.all().filter(typef='veg')
                user1 = dinner.objects.all().filter(typef='both')
                return render(request, 'datesc.html', {'my_data': user, 'my_data2': user1, 'name': name})
            elif nonveg == 'on':
                name = "NON VEG"
                user = dinner.objects.all().filter(typef='non-veg')
                user1 = dinner.objects.all().filter(typef='both')
                return render(request, 'datesc.html', {'my_data': user, 'my_data2': user1, 'name': name})
            elif drinks == 'on':
                name = "Drinks"
                user = dinner.objects.all().filter(drinks='yes')
                return render(request, 'datesc.html', {'my_data': user, 'name': name})


def familydinnerc(request, name):
    success = False
    if request.method == 'GET':
        user = dinner.objects.all().filter(cusine1=name)
        user2 = dinner.objects.all().filter(cusine2=name)
        user3 = dinner.objects.all().filter(cusine3=name)
        user4 = dinner.objects.all().filter(cusine4=name)
        return render(request, 'familydinnerc.html',
                      {'name1': name, 'my_data': user, 'my_data2': user2, 'my_data3': user3, 'my_data4': user4})
    if request.method == 'POST':
        veg = request.POST.get('example1')
        nonveg = request.POST.get('example2')
        drinks = request.POST.get('example3')
        if veg == 'on' and nonveg == 'on' and drinks == 'on':
            name = "NON VEG & DRINKS & DRINKS"
            user = dinner.objects.all().filter(typef='both').filter(drinks='yes')
            return render(request, 'datesc.html', {'my_data': user, 'name': name})
        elif veg == 'on' and nonveg == 'on':
            name = "NON VEG & VEG"
            user = dinner.objects.all().filter(typef='both')
            return render(request, 'datesc.html', {'my_data': user, 'name': name})
        elif veg == 'on' and drinks == 'on':
            name = "VEG & DRINKS"
            user = dinner.objects.all().filter(typef='veg').filter(drinks='yes')
            user1 = dinner.objects.all().filter(typef='both').filter(drinks='yes')
            return render(request, 'datesc.html', {'my_data': user, 'my_data2': user1, 'name': name})
        elif nonveg == 'on' and drinks == 'on':
            name = "NON VEG & DRINKS"
            user = dinner.objects.all().filter(typef='non-veg').filter(drinks='yes')
            user1 = dinner.objects.all().filter(typef='both').filter(drinks='yes')
            return render(request, 'datesc.html', {'my_data': user, 'my_data2': user1, 'name': name})
        elif veg == 'on':
            name = "VEG"
            user = dinner.objects.all().filter(typef='veg')
            user1 = dinner.objects.all().filter(typef='both')
            return render(request, 'datesc.html', {'my_data': user, 'my_data2': user1, 'name': name})
        elif nonveg == 'on':
            name = "NON VEG"
            user = dinner.objects.all().filter(typef='non-veg')
            user1 = dinner.objects.all().filter(typef='both')
            return render(request, 'datesc.html', {'my_data': user, 'my_data2': user1, 'name': name})
        elif drinks == 'on':
            name = "Drinks"
            user = dinner.objects.all().filter(drinks='yes')
            return render(request, 'datesc.html', {'my_data': user, 'name': name})


def familydinner(request):
    if request.method == 'GET':
        my_data = dinner.objects.all()
        return render(request, "familydinner.html", {'my_data': my_data})
    if request.method == 'POST':
        veg = request.POST.get('example1')
        nonveg = request.POST.get('example2')
        drinks = request.POST.get('example3')
        if veg == 'on' and nonveg == 'on' and drinks == 'on':
            name = "NON VEG & DRINKS & DRINKS"
            user = dinner.objects.all().filter(typef='both').filter(drinks='yes')
            return render(request, 'datesc.html', {'my_data': user, 'name': name})
        elif veg == 'on' and nonveg == 'on':
            name = "NON VEG & VEG"
            user = dinner.objects.all().filter(typef='both')
            return render(request, 'datesc.html', {'my_data': user, 'name': name})
        elif veg == 'on' and drinks == 'on':
            name = "VEG & DRINKS"
            user = dinner.objects.all().filter(typef='veg').filter(drinks='yes')
            user1 = dinner.objects.all().filter(typef='both').filter(drinks='yes')
            return render(request, 'datesc.html', {'my_data': user, 'my_data2': user1, 'name': name})
        elif nonveg == 'on' and drinks == 'on':
            name = "NON VEG & DRINKS"
            user = dinner.objects.all().filter(typef='non-veg').filter(drinks='yes')
            user1 = dinner.objects.all().filter(typef='both').filter(drinks='yes')
            return render(request, 'datesc.html', {'my_data': user, 'my_data2': user1, 'name': name})
        elif veg == 'on':
            name = "VEG"
            user = dinner.objects.all().filter(typef='veg')
            user1 = dinner.objects.all().filter(typef='both')
            return render(request, 'datesc.html', {'my_data': user, 'my_data2': user1, 'name': name})
        elif nonveg == 'on':
            name = "NON VEG"
            user = dinner.objects.all().filter(typef='non-veg')
            user1 = dinner.objects.all().filter(typef='both')
            return render(request, 'datesc.html', {'my_data': user, 'my_data2': user1, 'name': name})
        elif drinks == 'on':
            name = "Drinks"
            user = dinner.objects.all().filter(drinks='yes')
            return render(request, 'datesc.html', {'my_data': user, 'name': name})


def wedding(request):
    return render(request,'wedding.html')
def contactus(request):
    today=date.today()

    return render(request,'contactus.html',{'today':today})
saved1=False
def dinnerreg(request):
    global saved1
    obj=dinner()
    if request.method == 'GET':
        return render(request, 'dinnerreg.html')
    else:
        obj.hname = request.POST.get('hname')

        if 'h_pic_1' in request.FILES:
            h_pic_1 = request.FILES['h_pic_1']
        else:
            h_pic_1 = None
        obj.himage1=h_pic_1
        if 'h_pic_2' in request.FILES:
            h_pic_2 = request.FILES['h_pic_2']
        else:
            h_pic_2 = None
        obj.himage2=h_pic_2
        obj.hadd = request.POST.get('hadd')
        obj.hpp=request.POST.get('hpp')
        obj.cusine1=request.POST.get('cusine1')
        obj.cusine2 = request.POST.get('cusine2')
        obj.cusine3 = request.POST.get('cusine3')
        obj.cusine4 = request.POST.get('cusine4')
        obj.typef=request.POST.get('typef')
        obj.drinks=request.POST.get('drinks')
        obj.save()
        saved1 = True
        return render(request, 'dinnerreg.html', {'success': saved1})





def aboutus(request):
    return render(request,'aboutus.html')

def decor(request):
    global saved
    DecorModel=decorModel()

    if request.method=='GET':
        return render(request,"decor.html")
    else:
        decorname=request.POST.get('decorname')

        if 'profile_pic_1' in request.FILES:
            profile_pic_1 = request.FILES['profile_pic_1']
        else:
            profile_pic_1=None

        print(decorname,profile_pic_1)

        DecorModel.decorname=decorname
        DecorModel.image1=profile_pic_1
        DecorModel.save()

        saved=True

        return render(request,'decor.html',{'success':saved})












def venue(request):
    global saved
    VenueModel=venueModel()

    if request.method=='GET':
        return render(request,"venue.html")
    else:
        venuename=request.POST.get('venuename')

        if 'profile_pic_1' in request.FILES:
            profile_pic_1 = request.FILES['profile_pic_1']
        else:
            profile_pic_1=None
        if 'profile_pic_2' in request.FILES:
            profile_pic_2 = request.FILES['profile_pic_2']
        else:
            profile_pic_2=None
        if 'profile_pic_3' in request.FILES:
            profile_pic_3 = request.FILES['profile_pic_3']
        else:
            profile_pic_3=None
        if 'profile_pic_4' in request.FILES:
            profile_pic_4 = request.FILES['profile_pic_4']
        else:
            profile_pic_4=None
        if 'profile_pic_5' in request.FILES:
            profile_pic_5 = request.FILES['profile_pic_5']
        else:
            profile_pic_5=None
        if 'profile_pic_6' in request.FILES:
            profile_pic_6 = request.FILES['profile_pic_6']
        else:
            profile_pic_6=None

        print(venuename,profile_pic_1)

        VenueModel.venuename=venuename
        VenueModel.image1=profile_pic_1
        VenueModel.image2 = profile_pic_2
        VenueModel.image3 = profile_pic_3
        VenueModel.image4 = profile_pic_4
        VenueModel.image5 = profile_pic_5
        VenueModel.image6 = profile_pic_6
        VenueModel.city=request.POST.get('city')
        VenueModel.save()

        saved=True

        return render(request,'venue.html',{'success':saved})
def portfolio(request,name):
    v_data=venueModel.objects.all().filter(venuename=name)
    return render(request,'portfolio.html',{'my_data':v_data})
def portfoliow(request,name):
    v_data=venueModel.objects.all().filter(venuename=name)
    return render(request,'portfoliow.html',{'my_data':v_data})

def partys(request, name):
    success = False
    if request.method == 'GET':
        user = venueModel.objects.all().filter(city=name)
        return render(request, 'partys.html',
                      {'name1': name, 'my_data': user})

def party(request):
    if request.method=='GET':

        v_data=venueModel.objects.all()
        return render(request,"party.html",{'my_data':v_data})

def partyd(request,name):
    if request.method=='GET':
        d_data=decorModel.objects.all()
        return render(request, "partyd.html", {'my_data': d_data,'vname':name})
def partyreg1(request,dname,vname):
    if request.method=='GET':
        today=date.today()
        return render(request, "partyreg1.html", {'dname':dname , 'vname':vname,'today':today})
    success=False
    if request.method=='POST':
        obj = partyreg()
        pdate=request.POST.get('date')
        hname=request.POST.get('vname')
        test=partyreg.objects.all().filter(pdate=pdate).filter(venuename=hname)
        var="no"
        for d in test:
            var="yes"
        if var=="yes":
            v_data = venueModel.objects.all()
            success=True
            return render(request, 'party.html', {'success1': success, 'my_data': v_data})
        else:
            v_data = venueModel.objects.all()

            obj.ptype = "party"
            obj.pname = request.POST.get('name')
            obj.pemail = request.POST.get('email')
            obj.pdate=request.POST.get('date')
            obj.phone = request.POST.get('mobile')
            obj.pguest=request.POST.get('guest')
            obj.venuename=request.POST.get('vname')
            obj.decorname=request.POST.get('dname')
            obj.ptype="party"
            phh=request.POST.get('photo')
            dss=request.POST.get('dj')

            if phh == 'on':
                obj.photo = request.POST.get('photo')
            else:
               obj.photo = "none"
            if dss == 'on':
                obj.ds = request.POST.get('dj')
            else:
                obj.ds = "none"
            obj.save()
            success=True

            return render(request,'party.html',{'success':success,'my_data':v_data})

def weddings(request, name):
    success = False
    if request.method == 'GET':
        user = venueModel.objects.all().filter(city=name)
        return render(request, 'weddings.html',
                      {'name1': name, 'my_data': user})



def wedding(request):
    if request.method=='GET':

        v_data=venueModel.objects.all()
        return render(request,"wedding.html",{'my_data':v_data})

def weddingd(request,name):
    if request.method=='GET':
        d_data=decorModel.objects.all()
        return render(request, "weddingd.html", {'my_data': d_data,'vname':name})
def weddingreg(request,dname,vname):
    if request.method=='GET':

        return render(request, "weddingreg.html", {'dname':dname , 'vname':vname})
    success=False
    if request.method=='POST':
        obj=partyreg()
        pdate = request.POST.get('date')
        test = partyreg.objects.all().filter(pdate=pdate)
        var = "no"
        for d in test:
            var = "yes"
        if var == "yes":
            v_data = venueModel.objects.all()
            success = True
            return render(request, 'party.html', {'success1': success, 'my_data': v_data})
        else:
         obj.ptype="wedding"
         obj.pname=request.POST.get('name')
         obj.pemail=request.POST.get('email')
         dss=request.POST.get('dj')
         obj.phone=request.POST.get('mobile')
         obj.pdate=request.POST.get('date')
         obj.pguest=request.POST.get('guest')
         obj.venuename=request.POST.get('vname')
         obj.ptype = "wedding"
         obj.decorname=request.POST.get('dname')
         phh=request.POST.get('photo')
         if phh=='on':
          obj.photo=request.POST.get('photo')
         else:
            obj.photo="none"
         if dss=='on':
          obj.ds=request.POST.get('dj')
         else:
          obj.ds="none"
         obj.save()
         success=True
         v_data = venueModel.objects.all()
         return render(request,'wedding.html',{'success':success,'my_data':v_data})






def gallery(request):
    user=gallerym.objects.all()
    return render(request,'gallery.html',{'user':user})
def galleryreg(request):
    if request.method=='GET':
      return render(request,'galleryreg.html')
    success=False
    if request.method=='POST':
        obj=gallerym()
        obj.group=request.POST.get('group')
        obj.work=request.POST.get('work')
        if 'profile_pic_1' in request.FILES:
            profile_pic_1 = request.FILES['profile_pic_1']
        else:
            profile_pic_1 = None
        obj.image=profile_pic_1
        obj.save()
        success=True
        return render(request,'galleryreg.html',{'success':success})

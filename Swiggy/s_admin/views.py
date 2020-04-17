from django.shortcuts import render,redirect
from django.contrib import messages
from AdminApplication.models import *
from AdminApplication.form import *

# Create your views here.
def adminloginpage(request):
    return render(request, 'sadmin/login.html')


def admin_login_check(request):
    ausername = request.POST.get("admin_username")
    apassword = request.POST.get("admin_password")
    try:
        AdminLoginModel.objects.get(username=ausername, password=apassword)
        request.session['status'] = True
        return redirect('admin_home')

    except AdminLoginModel.DoesNotExist:
        messages.error(request, "Sorry Invalid Details")
        return redirect('adminloginpage')


def admin_home(request):
    return render(request, 'sadmin/admin_home.html')




def admin_logout(request):
    request.session['status'] = False
    return redirect('adminloginpage')


def open_state(request):
    return render(request,'sadmin/open_state.html',{"sf":StateForm(),"sdata":StateModel.objects.all()})


def save_state(request):
    sf = StateForm(request.POST)
    if sf.is_valid():
        sf.save()
        return redirect('open_state')
    else:
        return render(request,"sadmin/open_state.html",{"sf":sf})


def update_state(request):
    sno = request.GET.get("sno")
    sname = request.GET.get("sname")
    d1 = {"sno":sno,"sname":sname}
    return render(request,"sadmin/open_state.html",{"update_data":d1,"sdata":StateModel.objects.all()})


def update_state_data(request):
    sno = request.POST.get("s1")
    sname = request.POST.get("s2")
    StateModel.objects.filter(state_no = sno).update(state_name=sname)
    return redirect('open_state')


def delete_state(request):
    sno = request.GET.get("sno")
    StateModel.objects.filter(state_no=sno).delete()
    return redirect('open_state')


def open_city(request):
    return render(request,'sadmin/open_city.html',{"sf":CityForm(),"sdata":CityModel.objects.all()})


def save_city(request):
    sf = CityForm(request.POST)
    if sf.is_valid():
        sf.save()
        return redirect('open_city')
    else:
        return render(request, "sadmin/open_city.html", {"sf": sf})


def update_city(request):
    cno = request.GET.get("cno")
    cname = request.GET.get("cname")
    d1 = {"cno":cno,"cname":cname}
    return render(request,"sadmin/open_state.html",{"update_data":d1,"sdata":StateModel.objects.all()})


def update_city_data(request):
    cno = request.POST.get("s1")
    cname = request.POST.get("s2")
    CityModel.objects.filter(city_no = cno).update(city_name=cname)
    return redirect('open_city')


def delete_city(request):
    cno = request.GET.get("sno")
    CityModel.objects.filter(city_no=cno).delete()
    return redirect('open_city')


def open_area(request):
    return render(request, 'sadmin/open_area.html', {"sf": AreaForm(), "sdata": AreaModel.objects.all()})


def save_area(request):
    sf = AreaForm(request.POST)
    if sf.is_valid():
        sf.save()
        return redirect('open_area')
    else:
        return render(request, "sadmin/open_area.html", {"sf": sf})

def update_area(request):
    ano = request.GET.get("ano")
    aname = request.GET.get("aname")
    d1 = {"ano":ano,"aname":aname}
    return render(request,"sadmin/open_area.html",{"update_data":d1,"sdata":AreaModel.objects.all()})


def update_area_data(request):
    ano = request.POST.get("s1")
    aname = request.POST.get("s2")
    AreaModel.objects.filter(area_no = ano).update(area_name=aname)
    return redirect('open_area')


def delete_area(request):
    ano = request.GET.get("ano")
    AreaModel.objects.filter(area_no=ano).delete()
    return redirect('open_area')

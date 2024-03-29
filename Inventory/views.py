from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import SA_Serial_Numbers, Alienware, new_alienware_table, sparkfun_table, SparkFunKit, teacherpack_table, teacherpack, raspberry_pi_table, Raspberry_Pi
from django.shortcuts import get_object_or_404
from datetime import datetime
from .forms import AddAlienware, AddSparkfun, AddTeacherpack, AddRaspberryPiForm

# Create your views here.

def home(request):
    if request.method == "POST":
        Username = request.POST['username']
        Password = request.POST['password']

        user = authenticate(request, username=Username, password=Password)
    
        if user is not None: 
            login(request, user)
            messages.success(request, "Login successful")
            return render(request, 'home.html')
        else:
            messages.success(request, "Login unsuccessful")
            return render(request, 'home.html')
    else:
        return render(request,'home.html')
    
def logout_user(request):

    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')



def scanner(request):
    if request.method == "POST":
        sa_serial_number = request.POST.get('decodedText')
        print(sa_serial_number)
        sa_serial_object = get_object_or_404(SA_Serial_Numbers, serial_number=sa_serial_number)
        if sa_serial_object.serial_number == sa_serial_number:


            sa_serial_object.last_checked = datetime.now().date()
            sa_serial_object.save()
            print(datetime.now().date())
            print("Serial number matched")

    return render(request, 'scanner.html')


def robotics_lab(request):
    return render(request, 'robotics_lab.html')

def sparkfun(request):
    kits = sparkfun_table.objects.all()
    return render(request, 'sparkfun.html',{ 'kits' : kits})

def teacherpack(request):
    ipads = teacherpack_table.objects.all()
    return render(request, 'teacherpack.html', { 'ipads' : ipads})

def alienware(request):
    aliens = new_alienware_table.objects.all()
    return render(request, 'alienware.html', {"aliens" : aliens})

def spheros(request):
    return render(request, 'spheros.html')

def raspberry_pi(request):
    kits = raspberry_pi_table.objects.all()
    return render(request, 'raspberry_pi.html', { 'kits' : kits})


def add_sparkfun(request):
    form = AddSparkfun(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":   
            if form.is_valid():

                tracking_data = {
                'serial_number' : form.cleaned_data['serial_number'],
                'last_checked' : form.cleaned_data['last_checked'],
                }
                sparkfun_data = {
                    'location' : form.cleaned_data['location'],
                    'sa_serial_number' : form.cleaned_data['sa_serial_number'],
                    'serial_number' : form.cleaned_data['serial_number'],
                    'batch_number' : form.cleaned_data['batch_number'],
                    }

                new_item_SA_Serial_Number = SA_Serial_Numbers.objects.create(**tracking_data)
                new_item_sparkfun = SparkFunKit.objects.create(**sparkfun_data)
                messages.success(request, "Item Created")

                return redirect('sparkfun')
        return render(request,'add_sparkfun.html', {'form' : form})



def add_alienware(request):
    form = AddAlienware(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":   
            if form.is_valid():

                tracking_data = {
                'serial_number' : form.cleaned_data['serial_number'],
                'last_checked' : form.cleaned_data['last_checked'],
                }
                alienware_data = {
                    'location' : form.cleaned_data['location'],
                    'sa_serial_number' : form.cleaned_data['sa_serial_number'],
                    'serial_number' : form.cleaned_data['serial_number'],
                    }

                new_item_SA_Serial_Number = SA_Serial_Numbers.objects.create(**tracking_data)
                new_item_alienware = Alienware.objects.create(**alienware_data)
                messages.success(request, "Item Created")

                return redirect('alienware')
        return render(request,'add_alienware.html', {'form' : form})


def add_teacherpack(request):
    form = AddTeacherpack(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":   
            if form.is_valid():

                tracking_data = {
                'serial_number' : form.cleaned_data['serial_number'],
                'last_checked' : form.cleaned_data['last_checked'],
                }
                teacherpack_data = {
                    'location' : form.cleaned_data['location'],
                    'sa_serial_number' : form.cleaned_data['sa_serial_number'],
                    'serial_number' : form.cleaned_data['serial_number'],
                    }

                new_item_SA_Serial_Number = SA_Serial_Numbers.objects.create(**tracking_data)
                new_item_teacherpack = teacherpack.objects.create(**teacherpack_data)
                messages.success(request, "Item Created")

                return redirect('teacherpack')
        return render(request,'add_teacherpack.html', {'form' : form})

def add_raspberry_pi(request):
    form = AddRaspberryPiForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":   
            if form.is_valid():

                tracking_data = {
                'serial_number' : form.cleaned_data['sa_serial_number'],
                'last_checked' : form.cleaned_data['last_checked'],
                }
                raspberry_pi_data = {
                    'location' : form.cleaned_data['location'],
                    'sa_serial_number' : form.cleaned_data['sa_serial_number'],

                    }

                new_item_SA_Serial_Number = SA_Serial_Numbers.objects.create(**tracking_data)
                new_item_teacherpack = Raspberry_Pi.objects.create(**raspberry_pi_data)
                messages.success(request, "Item Created")

                return redirect('raspberry_pi')
        return render(request,'add_raspberry_pi.html', {'form' : form})



def vr_lab(request):
    return render(request, 'vr_lab.html')
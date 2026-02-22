from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import date, timedelta
from datetime import timedelta
import random

from .models import Job, OTP


# 🔹 Job List (Homepage)
@login_required(login_url='/accounts/login/')
def job_list(request):
    jobs = Job.objects.all()

    # 🔍 Search filter
    query = request.GET.get('q')
    if query:
        jobs = jobs.filter(title__icontains=query)

    # 📂 Category filter
    category = request.GET.get('category')
    if category:
        jobs = jobs.filter(category=category)

    # 🔃 Sorting
    sort = request.GET.get('sort')
    if sort == "deadline":
        jobs = jobs.order_by('last_date')

    # Deadline Soon logic
    soon_date = date.today() + timedelta(days=7)

    context = {
        'jobs': jobs,
        'soon_date': soon_date
    }

    return render(request, 'jobs/job_list.html', {'jobs': jobs})


# 🔹 Register
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password = request.POST['password']

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.is_active = False
        user.save()

        otp_code = str(random.randint(100000, 999999))
        OTP.objects.create(user=user, otp=otp_code)

        print("OTP:", otp_code)

        return redirect('verify_otp')

    return render(request, 'registration/register.html')


# 🔹 Verify OTP
def verify_otp(request):
    if request.method == "POST":
        otp_entered = request.POST['otp']
        otp_obj = OTP.objects.filter(otp=otp_entered).first()

        if otp_obj:
            user = otp_obj.user
            user.is_active = True
            user.save()
            otp_obj.delete()
            return redirect('login')

    return render(request, 'verify_otp.html')


# 🔹 Job Detail
def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'jobs/job_detail.html', {'job': job})


# 🔹 Add Job
def add_job(request):
    if request.method == 'POST':
        Job.objects.create(
            title=request.POST.get('title'),
            organization=request.POST.get('organization'),
            category="Central Govt",
            last_date=request.POST.get('last_date'),
            description=request.POST.get('description'),
            url=request.POST.get('url'),
            status=request.POST.get('status')
        )
        return redirect('job_list')

    return render(request, 'jobs/add_job.html')
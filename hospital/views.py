from django.shortcuts import render, redirect, get_object_or_404

from hospital.models import Patient, Doctor, Registration
from datetime import datetime
from django import forms
from django.core.validators import ValidationError


def home(request):
    return render(request, 'home.html')

class LoginForm(forms.Form):
    username = forms.fields.CharField(
        required=True,  #必填字段
        # min_length=3,
        # max_length=16,
        widget=forms.widgets.TextInput({"placeholder":"username","class":"form-control"})
    )
    password = forms.fields.CharField(
        required=True,
        min_length=3,
        max_length=16,
        widget=forms.widgets.PasswordInput({"placeholder":"password","class":"form-control"}),
    )
    # user_type = forms.fields.CharField(  # 新增用户类型字段，用于区分病人和医生登录
    #     required=True,
    #     widget=forms.widgets.HiddenInput()
    # )

    # def clean_username(self):
    #     user = self.cleaned_data["username"]
    #     is_exits = Patient.objects.filter(username=user).count()
    #     if not is_exits:
    #         raise ValidationError("用户名和密码错误")
    #     return user

def login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "login.html", {"form": form})
    else:
        form = LoginForm(data=request.POST)
        if form.is_valid():
            print(form.cleaned_data)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            login_type = request.POST.get('login_type')
            print(login_type)
            user_model = Patient if login_type == 'patient_login' else Doctor

            user = user_model.objects.filter(username=username, password=password).first()
            # user = False
            if user:
                print(user.username)
                request.session['info'] = {'id':user.id}
                return redirect("/home")
            else:
                # 验证密码失败，就增加错误，并重新渲染
                form.add_error("password","用户名或密码不正确")
                return render(request, "login.html", {"form": form})
        else:
            return render(request, "login.html", {"form": form})

    # form = LoginForm(data=request.POST)
    # login_type = request.POST.get('login_type')
    # print(login_type)
    # return render(request, "login.html", {"form": form})
        
# def login(request):
#     if request.method == 'GET':
#         return render(request, 'home.html')
    
#     username = request.POST.get('username')
#     pwd = request.POST.get('password')

#     ture_pwd = Patient.objects.filter(username=username)

#     if(pwd == ture_pwd):
#         redirect('home.html')

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'username', 'password', 'gender']
        widgets = {
            'password': forms.PasswordInput(),  # Display password field as a password input
        }

    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        # Customize form fields
        self.fields['name'].required = True
        self.fields['username'].required = True
        self.fields['password'].required = True

def enroll(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            # patient = form.save()
            return redirect('/login')  # Redirect to a success page
    else:
        form = PatientForm()

    return render(request, 'enroll.html', {'form': form})

def register(request):
    doctors_data = Doctor.objects.all()

    # 处理搜索
    name_query = request.GET.get('name', '')
    dept_query = request.GET.get('department', '')
    
    if name_query:
        doctors_data = doctors_data.filter(name=name_query)
    
    if dept_query:
        doctors_data = doctors_data.filter(dept=dept_query)

    #doctors_data = []

    return render(request, 'register.html', {'doctors_data': doctors_data, 'name_query': name_query, 'dept_query': dept_query})
    

def register_appoint(request, doctor_id):
    print('--register_appoint')
    doctor = get_object_or_404(Doctor, pk=doctor_id)

    if request.method == 'POST':
        appointment_time = request.POST.get('appointment_time')
        period = request.POST.get('period')
        print(appointment_time)
        print(period)

        # 将字符串时间转换为datetime对象
        appointment_datetime = datetime.strptime(appointment_time, '%Y-%m-%d')
        # 创建挂号记录
        registration = Registration.objects.create(
            doctor=doctor,
            patient=Patient.objects.filter(id=request.session['info']['id']).first(),  # 假设你有用户系统，并且患者信息保存在 user 模型中
            registration_time=appointment_datetime,
            peirod=period,
            status='registered',
        )
        

        return render(request, 'register/appoint_success.html')
    options = Registration.PERIOD_CHOICES
    return render(request, 'register_appoint.html', {'doctor': doctor, 'options':options})

def register_appoint_test(request):
    return render(request, 'register_appoint.html')

# def test(request):
    # objects = Patients.objects.all()
    # for object in objects:
    #     print(object.name)

#     Patients.objects.create(
#         name='**',
#         pub_time='2001-11-25',
#         author='***',
#     )
#     Patients.objects.filter(id=1).delete()
#     Patients.objects.all().delete()
#     Patients.objects.filter(id=1).update(pname='Bob')



def patient_personal(request):
    userid = request.session['info']['id']
    registrations = Registration.objects.filter(patient=userid)
    return render(request, 'patient_personal.html', {'registrations':registrations})

def cancel_registration(request, registration_id):
    registration = get_object_or_404(Registration, pk=registration_id)
    if request['info']['id'] == registration.patient and registration.status == 'registered':
        registration.status = 'cancelled'
        registration.save()
    
    return redirect('patient_personal')
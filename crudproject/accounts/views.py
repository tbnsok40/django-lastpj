# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User # Django가 제공해주는 User 모델을 사용하기 위해서 import 해줬습니다. 
from django.contrib import auth # 그리고 인증 절차를 위해서도 가져왔습니다. 
# Create your views here.


def signup(request):
    if request.method == 'POST': # 앞서 form에서 post 방식으로 요청을 보냈을 경우, 즉 회원가입 버튼을 눌렀을 경우 이 다음 과정이 실행됩니다. 
        if request.POST['password1'] == request.POST['password2']: # 비밀번호가 일치하는지 확인합니다. 
            user = User.objects.create_user(
                request.POST['username'], password=request.POST['password1']) # 홈에서 받은 아이디와 패스워드를 가진 유저를 생성합니다. 
            auth.login(request, user) # 회원가입 후 바로 로그인이 되게 하기 위해 작성해주었습니다. 
            return redirect('index') # 회원가입이 완료되면 index 페이지로 보냅니다. 
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)        
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            return render(request, 'login.html',{'error':'username or password is wrong'})
    else:
        return render(request, 'login.html')



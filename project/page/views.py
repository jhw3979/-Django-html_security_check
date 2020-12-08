from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from .models import Html_file
from .models import User
from .forms import UploadFileForm

# Create your views here.

def reg(request):
    if request.method == "POST":    #값을 받을경우 실행
        if request.POST['name'] != "" and request.POST['id'] != "" and request.POST['pw'] != "" and request.POST['re_pw'] != "":
            if request.POST['pw'] == request.POST['re_pw']: #비밀번호가 같을경우
                if len(User.objects.filter(User_id=request.POST['id'])) == 0:   #존재하는 아이디일경우
                    User_qs = User(User_id=request.POST['id'],
                                   User_pw=request.POST['pw'],
                                   User_name=request.POST['name'])
                    User_qs.save()
                    return HttpResponseRedirect(reverse('project:login'))
                else:
                    context = {"mes": "존재하는 아이디입니다."}
                    return render(request, "page/reg.html", context)
            else:
                context = {"mes": "아이디 혹은 비밀번호가 일치하지 않습니다."}
                return render(request, "page/reg.html", context)
        else:
            context = {"mes": "빈칸이 있습니다."}
            return render(request, "page/reg.html", context)
    else:
        return render(request, 'page/reg.html')


def login(request):
    if request.method == "POST":
        post_id = request.POST['id']
        post_pw = request.POST['pw']

        if post_id != "" and post_pw != "":
            if len(User.objects.filter(User_id=post_id)) != 0:
                if post_id == get_object_or_404(User, User_id=post_id).User_id and \
                        post_pw == get_object_or_404(User, User_id=post_id).User_pw:
                    #세션 전달
                    User_qs = get_object_or_404(User, User_id=post_id)
                    request.session['User_id'] = User_qs.id
                    return HttpResponseRedirect(reverse('project:home'))
                else:
                    return render(request, 'page/login.html', {'mes': '아이디 혹은 비밀번호가 일치하지 않습니다.'})
            else:
                return render(request, "page/login.html", {"mes": "계정이 존재하지 않습니다."})
        else:
            return render(request, "page/login.html", {"mes": "빈칸이 있습니다."})

    elif request.method == "GET":
        return render(request, 'page/login.html')


def home(request):
    print("홈페이지")
    if request.method == "POST":
        print("post받음")
        if request.POST['file'][request.POST['file'].find("html"):] != "html":
            context = {"mes": "html파일이 아닙니다."}
            return render(request, "page/home.html", context)
        return render(request, "page/home.html")
    elif request.method == "GET":
        print("get받음")
        return render(request, "page/home.html")
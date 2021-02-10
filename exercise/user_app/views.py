from django.shortcuts import render
# from django.http import HttpResponse
# from user_app.models import user_info
from user_app.forms import Newuser

# Create your views here.

def index (request):
    return render (request , 'user_app/index.html')

def user_view (request):
    form = Newuser()
    if request.method == 'POST':
        form = Newuser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else :
            Print ("form Invalid")

    return render (request,"user_app/user.html",{'form':form})

    # user = user_info.objects.order_by('first_name')
    # user_dict={'user_data':user}
    # return render (request,'user_app/user.html',user_dict)

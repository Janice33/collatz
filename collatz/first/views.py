from django.shortcuts import render
from django.http import request, HttpResponse
from .forms import MyForm
from .models import User

def input(request):
    if request.method=='POST':
        formvar= MyForm(request.POST)
        if formvar.is_valid():
            modelvar=User()
            modelvar.name= formvar.cleaned_data.get('fname')
            modelvar.no= formvar.cleaned_data.get('fno')
            modelvar.save()
            object_var= User.objects.all()
            list_num = []
            count = int(0)
            num = int(modelvar.no)
            while num!=1:
                if num%2==0:
                    num=num/2
                    list_num.append(int(num))
                else:
                    num=num*3+1
                    list_num.append(int(num))
                count=count+1
            modelvar.steps= count
            modelvar.save()
            context = {'object_var': object_var,
                   'modelvar': modelvar,
                   'count': count,
                   'num': modelvar.no,
                   'list_num':list_num
                   }
        return render(request, 'display.html', context)
    else:
        formvar=MyForm()
        context={'formvar':formvar}
        return render(request,'finput.html',context)



def details(request):
    object_var = User.objects.all()
    return render(request,'details.html',{'object_var':object_var})


def options(request):
    return render(request,'options.html',{})
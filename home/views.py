from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from home.models import Task
# Create your views here.


def home(request):
    context = {'success': False}
    if request.method == "POST":
        title = request.POST['title'] #handle form
        desc = request.POST['desc']
        print(title,desc)
        ins = Task(tasktitle=title, taskdesc=desc)
        ins.save()
        context = {'success': True}

    return render(request,'index.html', context)


def tasks(request):
    alltasks = Task.objects.all()
    context = {'tasks': alltasks}
    return render(request,'tasks.html',context)


def delete(request,id):
    delitem = Task.objects.get(pk=id)
    delitem.delete()
    return redirect('/tasks')


"""def edit(request,id):
    updateitem = Task.objects.get(pk=id)
    context = {'title' : updateitem.title,
               'desc': updateitem.desc,
               'id':updateitem.id}
    return render(request,'edit.html',context)
    
def update(request,id):
    obj = Task(id=id)
    obj.title = request.GET['title']  # handle form
    obj.desc = request.GET['desc']
    obj.save()
    context = {"alltodos" : Task.objects.all()}
    return render(request, 'index.html', context)"""


def search(request):
    if request.method=='GET':
        q = request.GET['q'].upper()
        task = Task.objects.all().filter(tasktitle__icontains=q)
        return render(request,'tasks.html',{'tasks':task})

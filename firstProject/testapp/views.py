from django.shortcuts import render
from django.http import HttpResponse
from testapp.models import Employee
def employee_info_view(request):
    employees=Employee.objects.all()
    data={'employees':employees}
    res=render(request,'testapp/employees.html',data)
    return(res)
def about(request):
    text="This an about page"
    return render(request,'testapp/about.html',{'text':text})
def showContact(request):
    s="<h1>Websit:Mysirg<h1/>"
    s+="<p>Emailid:shrikants1takale@gamail.com<p/>"
    s+="<p1>Moble:9970349497<p/>"
    return HttpResponse(s)
def greeting(request):
  s="<h1>Hello and welcom to first page of testapp <h1/>"
  return HttpResponse(s)

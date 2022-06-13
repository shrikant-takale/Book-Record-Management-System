from testapp import views
from django.conf.urls import url
urlpatterns = [
url('contact/',views.showContact),
url('about/',views.about),
url('^$',views.greeting),
url('employee',views.employee_info_view),
]

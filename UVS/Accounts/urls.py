from django.conf.urls import url
from .views import index,student_login, Login


app_name = 'Accounts'

urlpatterns = [
	url(r'^$', index, name='account_index'),
	url(r'^student_login/$', student_login, name='student_login'),
	url(r'^teachers_login/$', Login, name='teacher_login')
]
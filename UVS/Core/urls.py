from django.conf.urls import url
from . import views

app_name = 'Core'

urlpatterns = [
	url(r'^$', views.index, name='index_page'),
	url(r'^add_student/$', views.add_student, name='add_student'),
	url(r'^add_contest/$', views.add_contest, name='add_contest'),
	url(r'^add_contestant/$', views.add_contestant, name='add_contestant'),
	url(r'^add_position/$', views.add_position, name='add_position'),
	url(r'^delete_position/(?P<slug>[\w-]+)/$', views.delete_position, name='delete_position'),
	url(r'^contest_page/$', views.contest_page, name='contest_page'),
	url(r'^contestants_page/$', views.contestants_page, name='contestants_page'),
	url(r'^students_page/$', views.students_page, name='students_page'),

]

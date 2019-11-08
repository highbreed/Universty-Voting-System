from django.conf.urls import url
from .views import index, results


app_name = 'Voter'


urlpatterns = [
	url(r'^$', index, name='index_page'),
	url(r'^results/$', results, name='results_page'),
]

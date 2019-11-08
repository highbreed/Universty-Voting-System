from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from Core.models import Contestant, Contest

# Create your views here.

def index(request):
	"""
	this a function for the landing page
	:param request:
	:return:
	"""
	contest_queryset = Contest.objects.all()
	contestant_queryset = Contestant.objects.all()
	if request.method == 'POST':
		selected_candidates = request.POST.getlist('votes', None)
		for candidate in selected_candidates:
			candidate_qs = get_object_or_404(Contestant, id=candidate)
			candidate_qs.votes = candidate_qs.votes + 1
			candidate_qs.save(update_fields=['votes'])
		redirect('/student/')
	template = 'student_index.html'
	context = {
		'contests': contest_queryset,
		'contestants': contestant_queryset,
	}
	return render(request, template, context)


def results(request):
	contest_queryset = Contest.objects.all()
	contestant_queryset = Contestant.objects.all()
	# get top performer in each position
	template = 'results.html'
	context = {
		'contests': contest_queryset,
		'contestants': contestant_queryset,
	}

	return render(request, template, context)





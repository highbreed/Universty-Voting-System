from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import AddStudentForm, AddContestForm, AddContestantForm, AddPositionForm
from .models import Contest, Student, Contestant, Position
from datetime import date
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='/account/')
def index(request):
	"""
	this is the index dashboard page for admins
	:param request:
	:return:
	"""
	contest_qs = Contest.objects.all()
	student_qs = Student.objects.all().count()
	contestant_qs = Contestant.objects.all().count()
	position_qs = Position.objects.all()
	open_contests = []
	present_date = date.today()
	for contest in contest_qs:
		if contest.voting_end >= present_date:
			open_contests.append(contest)
	position_form = AddPositionForm()
	template = 'index.html'
	context = {
		'students': student_qs,
		'contestants': contestant_qs,
		'contests': len(open_contests),
		'positions': position_qs,
		'position_form': position_form,

	}
	return render(request, template, context)


def add_student(request):
	"""
	a function that handles admission of Students
	:param request:
	:return:
	"""
	if request.method == 'POST':
		student_form = AddStudentForm(request.POST)
		if student_form.is_valid():
			student_form.save()
			return redirect('/add_student/')
		else:
			return student_form.errors
	else:
		student_form = AddStudentForm()
		template = 'add_student.html'
		context = {
			'student_form': student_form,
		}
		return render(request, template, context)


def add_contest(request):
	"""
	function to handle creation and updating of contests
	:param request:
	:return:
	"""
	if request.method == 'POST':
		contest_form = AddContestForm(request.POST)
		if contest_form.is_valid():
			contest_form.save()
			messages.info(request, 'New contest has been added successfully')
			return redirect('/add_contest/')
		else:
			messages.info(request,
						  'New contest  was not added successfully due to {} errors'.format(contest_form.errors))
			return redirect('/add_contest/')

	else:
		contest_form = AddContestForm()
		template = 'add_contest.html'
		context = {
			'contest_form': contest_form,
		}
		return render(request, template, context)


def add_contestant(request):
	"""
	this function handles adding and deleting of contestants
	:param request:
	:return:
	"""
	if request.method == 'POST':
		contestant_form = AddContestantForm(request.POST)
		if contestant_form.is_valid():
			contestant_form.save()
			return redirect('/add_contestant/')
		else:
			return contestant_form.errors
	else:
		contestant_form = AddContestantForm()
		template = 'add_contestant.html'
		context = {
			'contestant_form': contestant_form,
		}

		return render(request, template, context)


def add_position(request):
	if request.method == 'POST':
		position_form = AddPositionForm(request.POST)
		if position_form.is_valid():
			position_form.save()
			return redirect('/')
		else:
			return position_form.errors
	else:
		position_form = AddPositionForm()
		template = 'add_position.html'
		context = {
			'position_form': position_form,
		}
		return render(request, template, context)


def delete_position(request, slug):
	position_qs = Position.objects.get(pk=slug)
	position_qs.delete()
	messages.info(request, '{} deleted Successful'.format(position_qs))
	return redirect("/")


def contest_page(request):
	contest_qs = Contest.objects.all()
	contestant_qs = Contestant.objects.all()
	present_date = date.today()
	valid_contest = []
	my_dic = {}

	# lets find valid contests and append to variable above
	for contest_value in contest_qs:
		if contest_value.voting_end >= present_date:
			valid_contest.append(contest_value)
			my_dic[contest_value] = []

	for x in my_dic.keys():
		for contestant in contestant_qs:
			if contestant.contest == x:
				my_dic[x].append(contestant)

	print(my_dic)
	template = 'contest_page.html'
	context = {
		'contests': valid_contest,
		'contestants': contestant_qs,
		'contestant_dic': my_dic,
	}
	return render(request, template, context)


def contestants_page(request):
	contest_qs = Contest.objects.all()
	contestant_qs = Contestant.objects.all()

	template = 'contestants_page.html'

	context = {
		'contests': contest_qs,
		'contestants': contestant_qs,
	}

	return render(request, template, context)


def students_page(request):
	student_qs = Student.objects.all()
	template = 'students_page.html'
	context = {
		'students': student_qs
	}
	return render(request, template, context)

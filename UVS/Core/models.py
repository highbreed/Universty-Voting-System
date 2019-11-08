import datetime

from django.db import models


GENDER_CHOICE = (
	('Male', 'Male'),
	('Female', 'Female'),

)


class Student(models.Model):
	"""
	this is a database model that captures the students details
	:returns FirstName and LastName
	"""
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	gender = models.CharField(choices=GENDER_CHOICE, max_length=10)
	adm_number = models.CharField(max_length=100)

	def __str__(self):
		return "{} {}".format(self.first_name, self.last_name)


class Position(models.Model):
	"""
	A database model that captures the available seats for contest
	"""

	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class Contest(models.Model):
	"""
	model to set registration of voting
	"""
	STATUS_CHOICE = (
		('active', 'active'),
		('voting ongoing', 'voting ongoing'),
		('registration ongoing', 'registration ongoing'),
		('registration ended', 'registration ended'),
		('results relesed', 'results relesed'),
		('ended', 'ended'),
	)
	name = models.CharField(max_length=100)
	open_positions = models.ManyToManyField(Position)
	registration_start = models.DateField()
	registration_end = models.DateField()
	voting_start = models.DateField()
	voting_end = models.DateField()
	status = models.CharField(choices=STATUS_CHOICE, max_length=50, default='active')

	def __str__(self):
		return self.name


class Contestant(models.Model):
	"""
	model to register contestants
	"""
	name = models.ForeignKey(Student, on_delete=models.CASCADE)
	contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
	position = models.ForeignKey(Position, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='contestant_images', blank=True, null=True)
	votes = models.IntegerField(default=0, null=True, blank=True)

	def __str__(self):
		return str(self.name)


class Winner(models.Model):
	"""
	This model stores the final winners
	"""
	contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
	contestant = models.ForeignKey(Contestant, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.contestant)


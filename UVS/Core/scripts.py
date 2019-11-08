from .models import Contest
from datetime import datetime
import pytz


def available_contest():
	contest_qs = Contest.objects.all()
	present = datetime.now()
	for contest in contest_qs:
		if contest.registration_start < present:
			print(contest)



from django.forms import ModelForm, DateInput, CheckboxSelectMultiple
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Student, Contest, Contestant, Position


class DateWidget(DateInput):
	input_type = 'date'


class AddStudentForm(ModelForm):
	class Meta:
		model = Student
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Submit'))


class AddContestForm(ModelForm):
	class Meta:
		model = Contest
		fields = '__all__'
		widgets = {
			'registration_start': DateWidget(),
			'registration_end': DateWidget(),
			'voting_start': DateWidget(),
			'voting_end': DateWidget(),
			'open_positions': CheckboxSelectMultiple(),
		}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Submit'))


class AddContestantForm(ModelForm):
	class Meta:
		model = Contestant
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Submit'))


class AddPositionForm(ModelForm):
	class Meta:
		model = Position
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Submit'))

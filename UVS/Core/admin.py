from django.contrib import admin
from .models import Student, Position, Contestant, Contest, Winner


admin.site.register(Student)
admin.site.register(Position)
admin.site.register(Contestant)
admin.site.register(Contest)
admin.site.register(Winner)

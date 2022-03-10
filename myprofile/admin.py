from django.contrib import admin

# from myprofile.models import Person, Project
# from.models import Person,Project
from myprofile.models import Education, Person, Project, Skill

# Register your models here.

admin.site.register(Person)
admin.site.register(Project)
admin.site.register(Education)
admin.site.register(Skill)
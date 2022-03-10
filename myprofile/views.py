from sre_constants import CATEGORY
from django.shortcuts import render

from myprofile.models import Education, Person, Project, Skill

# Create your views here.

def index(request):
    # projects=Project.objects.order_by().values_list('category').distinct()
    
    #
    #person = Person.objects.filter(name='Sadaqat Ahmadzai')
    # person= Person.objects.get(pk=person_id)
    persons=Person.objects.all()
    skills=Skill.objects.all()
    education=Education.objects.all()
    total_projects = Project.objects.all().count()
    # total_projectss = Project.objects.all()
    projects=Project.objects.values().distinct()
    projects.distinct()
    uniques=[]
   
    

        
        
        
    
    
    
    # proj=models.Shop.objects.order_by().values_list('city').distinct()
    # profiles=SocialProfile.objects.all()

    context = {
            'persons': persons,
            'skills': skills,
            'education': education,
            'projects': projects,
            # 'output': output,
            'uniques': uniques,
            # 'total_projectss':total_projectss,
            # 'project': project,
            'total_projects': total_projects,
            # 'educ':educ,
            
            
            }
    
    
    return render(request, 'myprofile/index.html', context)
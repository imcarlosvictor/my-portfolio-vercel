from django.shortcuts import render
from django.core.mail import send_mail
from .models import Project
from .forms import ContactForm
from json import dumps

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            company= form.cleaned_data['company']
            message = form.cleaned_data['message']

            # Send to business email
            subject = f'{name.capitalize()} from {company.capitalize()}'
            guest_msg = email + '\n\n' + message

            send_mail(subject, guest_msg, email, ['imcvlucas@gmail.com'])
    else:
        form = ContactForm()


    projects = Project.objects.all()
    # Create a project data dictionary and pass the project id to get all data
    project_data_dict = {}
    for project  in projects:
        project_data_dict[project.id] = {
            'title': project.title,
            'image': str(project.image),
            'year': project.year,
            'status': project.completed,
            'tech_stack': project.tech_stack,
            'libraries': project.libraries,
            'description': project.description,
            'live_url': project.live_url,
            'code_url': project.github_url,
        }
    project_data_JSON = dumps(project_data_dict)

    context = {'projects': projects,  'project_data_JSON': project_data_JSON, 'form': form }
    return render(request, 'index.html', context)

def projectDetail(request):
    return render(request, 'projects/projects.html')

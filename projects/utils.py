from .models import Project,Tag
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.db.models import Q


def searchProjects(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    tags = Tag.objects.filter(name__icontains=search_query)

    projects = Project.objects.distinct().filter(
        Q(title__icontains=search_query)|
        Q(description__icontains=search_query)|
        Q(owner__name__icontains=search_query)|
        Q(tags__in=tags)
    )

    return projects,search_query



def paginateProjects(request,projects,results):
    page = request.GET.get('page')
    paginator = Paginator(projects,results)

    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        projects = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        projects = paginator.page(page)
    

    leftIndex = max(int(page) - 1,1)
    rightIndex = min(int(page) + 1, paginator.num_pages)


    custom_range = range(leftIndex,rightIndex+1)
    return custom_range, projects






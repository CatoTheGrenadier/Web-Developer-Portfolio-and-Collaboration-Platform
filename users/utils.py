from .models import Profile, skill
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.db.models import Q




def searchProfiles(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    skills = skill.objects.filter(name__iexact=search_query)

    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search_query)|
        Q(short_intro__icontains=search_query)|
        Q(skill__in=skills)
        )
    
    return profiles, search_query



def paginateProfles(request,profiles,results):
    page = request.GET.get('page')
    paginator = Paginator(profiles,results)

    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)
    

    leftIndex = max(int(page) - 1,1)
    rightIndex = min(int(page) + 1, paginator.num_pages)


    custom_range = range(leftIndex,rightIndex+1)
    return custom_range, profiles
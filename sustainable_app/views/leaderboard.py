from django.http import HttpResponse
from django.template import loader

from sustainable_app.models.user import User



def leaderboard(request):

    template = loader.get_template("sustainable_app/leaderboard.html")

    if request.method == 'GET':
        param = request.GET.get("param",None)
        
        if param == "username" :
            context = sorted_by_username()
        elif param == "level":
            context =  sorted_by_xp()
        elif param == "points":
            context = sorted_by_points()
        else:
            return HttpResponse(template.render(sorted_by_username()))

        return HttpResponse(template.render(context))

    else:
        return HttpResponse(template.render(sorted_by_username()))
   
    

# Returns dictionary sorted by username
def sorted_by_username():
    
    users = User.objects.order_by("username")
    context = {"users": users}
    return context

# Returns dictionary sorted by xp
def sorted_by_xp():
    
    users = User.objects.order_by("-xp")
    context = {"users": users}
    return context

# Returns dictionary sorted by level
def sorted_by_points():
    
    users = User.objects.order_by("-points")
    context = {"users": users}
    return context


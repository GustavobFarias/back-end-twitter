# deploy/views.py
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import git

@csrf_exempt
def update(request):
    if request.method == "POST":
        repo = git.Repo('/home/gfarias/back-end-twitter')
        origin = repo.remotes.origin
        origin.pull()
        return HttpResponse("Updated code on PythonAnywhere")
    return HttpResponse("Couldn't update the code on PythonAnywhere")
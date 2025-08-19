from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

import git

@csrf_exempt
def update(request):
    secret_key = "MINHA_CHAVE_SECRETA"
    if request.method == "POST" and request.headers.get("Authorization") == f"Token {secret_key}":
        repo = git.Repo('/home/gfarias/twitter-login')
        origin = repo.remotes.origin
        origin.pull()
        return HttpResponse("Updated code on PythonAnywhere")
    return HttpResponse("Unauthorized", status=401)
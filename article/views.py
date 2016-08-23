from django.http.response import Http404
from django.shortcuts import render_to_response, redirect
from article.models import *
from django.core.exceptions import ObjectDoesNotExist
# from article.forms import CommentForm
from django.template.context_processors import csrf
# from django.contrib import auth
# from django.core.paginator import Paginator
# from django.contrib.auth.models import User
# from tvoy_style.users.models import User
# from django.template import loader, Context, RequestContext


# Create your views here.



# def return_path_f(request):
#     request.session.modified = True
#     if 'return_path' in request.session:
#         del request.session['return_path']
#         request.session['return_path'] = request.META.get('HTTP_REFERER', '/')
#     else:
#         request.session['return_path'] = request.META.get('HTTP_REFERER', '/')





def advice(request):

    # return_path_f(request)

    args = {}
    args['articles'] = Article.objects.all()   

    return render_to_response("advice.html", args)


def article(request, article_id=1):

    article = Article.objects.get(id=article_id)
    args = {}

    args.update(csrf(request))

    # return_path_f(request)

    args["article"] = article
      
    return render_to_response("article.html", args)



#encoding=utf-8

from django.shortcuts import render
from blog.models import Category, Banner, Article
from common.helpers import paged_items, ok_json
from blog.helper import judge_pc_or_mobile


def index(request):
    cat_id = int(request.GET.get('cat_id', 0))
    page = int(request.GET.get('page', 0))
    page_size = int(request.GET.get('page_size', 20))
    title = request.GET.get('title', None)
    user_agt = judge_pc_or_mobile(request.META.get("HTTP_USER_AGENT"))
    cat_list = Category.objects.filter(is_active=True).order_by('-id')
    banner_list = Banner.objects.filter(is_active=True).order_by('-id')[:3]
    article_list = Article.objects.filter(is_active=True).order_by('-id')
    if user_agt is False:
        if cat_id not in ["0", 0, None]:
            cat = Category.objects.get(id=cat_id)
            article_list = article_list.filter(category=cat, is_active=True).order_by('-id')
        if title not in [None, ""]:
            article_list = article_list.filter(title__icontains=title)
        article_lst = paged_items(request, article_list)
        return render(request, 'web/blog/index.html', locals())
    else:
        if cat_id not in ["0", 0, None]:
            cat = Category.objects.get(id=cat_id)
            article_lst = article_list.filter(category=cat).order_by('-id')
        if title not in [None, ""]:
            article_lst = article_list.filter(title__icontains=title)
        if request.is_ajax():
            start = page * page_size
            end = start + page_size
            artcle_list_ret = []
            article_list = article_list[start:end]
            for article in article_list:
                artcle_list_ret.append(article.return_dict())
            return ok_json(artcle_list_ret)
        else:
            article_lst = article_list[0:20]
            return render(request, 'mobile/blog/index.html', locals())


def artcle(request):
    aid = int(request.GET.get('aid', 0))
    article = Article.objects.get(id=aid)
    user_agt = judge_pc_or_mobile(request.META.get("HTTP_USER_AGENT"))
    if user_agt is False:
        return render(request, 'web/blog/arctcle.html', locals())
    else:
        return render(request, 'mobile/blog/arctcle.html', locals())
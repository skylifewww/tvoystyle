from django.contrib import admin
from article.models import *
# from embed_video.admin import AdminVideoMixin
# from mptt.admin import MPTTModelAdmin
from article.fields import AdminImageWidget
from easy_thumbnails.fields import ThumbnailerImageField


# Register your models here.




class ArticleAdmin(admin.ModelAdmin):
    fields = ["article_title", "article_title_small", 'short_text',
              'full_text', 'slug']

   
    list_filter = ["article_title"]
    search_fields = ["article_title"]
    list_display = ["article_title", "article_title_small", 'pic_slug']
    formfield_overrides = {
        ThumbnailerImageField: {'widget': AdminImageWidget},
    }

    #  fields = ["article_author", "article_title", "article_video", 'video_published', "article_date", 'short_text',
    #           'full_text', 'slug',
    #           "article_tag", "article_category", "article_works"]

   
    # list_filter = ["article_date", "article_tag", "article_category", "article_author", 'video_published']
    # search_fields = ["article_title", "article_author", "article_category", "article_tag", 'video_published']
    # list_display = ["article_title", "article_author", "article_category", 'video_published', 'pic_slug']
    # formfield_overrides = {
    #     ThumbnailerImageField: {'widget': AdminImageWidget},
    # }


# class  CategoryAdmin(admin.ModelAdmin):
#       # fields = ['name', 'parent']
#       list_display = ['name']


# class  AuthorAdmin(admin.ModelAdmin):
#       list_display = ['name', 'pic_slug']      



# class  WorksAdmin(admin.ModelAdmin):
#     # fields = ['work_author', 'work_title', 'slug', 'short_text', 'work_price']    
#     list_filter = ['work_category', 'work_author', 'work_title', 'work_price']  
#     search_fields = ['work_category','work_author', 'work_title', 'work_price']  
#     list_display = ['work_title', 'work_category', 'work_author', 'pic_slug', 'short_text', 'work_price']    
#     formfield_overrides = {
#         ThumbnailerImageField: {'widget': AdminImageWidget},
#     }


# class SlideAdmin(admin.ModelAdmin):
#     list_display = ['name', 'pic_slug', 'category', 'published', 'published_main', 'ordering']
#     list_editable = ['published','ordering', 'published_main']
#     formfield_overrides = {
#         models.ImageField: {'widget': AdminImageWidget},
#     }

   

# admin.site.register(Slide, SlideAdmin)        
admin.site.register(Article, ArticleAdmin)
# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Author, AuthorAdmin)
# admin.site.register(Tag)
# admin.site.register(Works, WorksAdmin)

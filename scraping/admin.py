from django.contrib import admin
from .models import Category,Language,Post,Error,Post_video
# ,Url
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class VideoRes(resources.ModelResource):

    class Meta:
        model = Post_video
        fields = ('id','posts','title','videos')

class VideoLinks(ImportExportModelAdmin):
        resource_class = VideoRes

class CategoryRes(resources.ModelResource):

    class Meta:
        model = Category
        fields = ('name')

class Categorys(ImportExportModelAdmin):
        resource_class = CategoryRes


class PostRes(resources.ModelResource):

    class Meta:
        model = Post
        fields = ('id','title','descr_post','time_videos','quantity_videos','time_add','language_videos','picture_post')

class Posts(ImportExportModelAdmin):
        resource_class = PostRes


admin.site.register(Category,Categorys)
admin.site.register(Language)
admin.site.register(Post,Posts)
admin.site.register(Error)
admin.site.register(Post_video, VideoLinks)
# admin.site.register(Url)
from django.contrib import admin
from .models import Category,Language,Post,Error,Post_video
# ,Url
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class VideoRes(resources.ModelResource):

    class Meta:
        model = Post_video
        fields = ('id','videos')

class VideoLinks(ImportExportModelAdmin):
        resource_class = VideoRes


admin.site.register(Category)
admin.site.register(Language)
admin.site.register(Post)
admin.site.register(Error)
admin.site.register(Post_video, VideoLinks)
# admin.site.register(Url)
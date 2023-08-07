
from django.contrib import admin
from django.utils.html import format_html
from . models import News,Notice,Holiday,Career,About,Contact


admin.site.register(News)
admin.site.register(Notice)
admin.site.register(Holiday)
admin.site.register(Career)
admin.site.register(About)

class ContactAdmin(admin.ModelAdmin):
    list_filter=["Situation"]
    search_fields=['name','email','subject','Situation']
    list_display=['name','email','subject','status','_']
   
    list_per_page =5

    def _(self,obj):
        if obj.Situation =="Read":
            return True
        else:
            return False
    _.boolean=True

    #function for color

    def status(self,obj):
        if obj.Situation=="Read":
            color='#99c904'
        else:
            color='red'
        return format_html('<strong><p style="color:{}">{}</p></strong>'.format(color,obj.Situation))

    status.allow_tags=True


admin.site.register(Contact,ContactAdmin)

# Register your models here.

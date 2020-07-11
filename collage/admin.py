from django.contrib import admin

# Register your models here.

from .models import collage , dep , Post ,comment


admin.site.register(collage)
admin.site.register(dep)
admin.site.register(Post)
admin.site.register(comment)
from django.contrib import admin
from tasklists.models import TaskList, Task

admin.site.register(TaskList)
admin.site.register(Task)

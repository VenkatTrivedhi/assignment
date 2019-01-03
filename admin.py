from django.contrib import admin
from contest.models import Contest,Colleges,Challenges,View_Stats,Submission_Stats

admin.site.register(Contest)
admin.site.register(Colleges)
admin.site.register(Challenges)
admin.site.register(View_Stats)
admin.site.register(Submission_Stats)
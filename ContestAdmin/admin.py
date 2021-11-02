from django.contrib import admin

# Register your models here.
from .models import creator, Contest, adm, submission, candidate, language, RegisterContest, ChooseLanguage

class creatorAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class ContestAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class admAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class submissionAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

# class problemAdmin(admin.ModelAdmin):
#     readonly_fields = ('id',)

class candidateAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class languageAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class RegisterContestAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class ChooseLanguageAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(creator, creatorAdmin)
admin.site.register(Contest, ContestAdmin)
admin.site.register(adm, admAdmin)
admin.site.register(submission, submissionAdmin)
# admin.site.register(problem, problemAdmin)
admin.site.register(candidate,candidateAdmin)
admin.site.register(language, languageAdmin)
admin.site.register(RegisterContest, RegisterContestAdmin)
admin.site.register(ChooseLanguage, ChooseLanguageAdmin)
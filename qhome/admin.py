from django.contrib import admin
from .models import Quiz, Question, Answer

class AnswerInLine(admin.TabularInline):
    model = Answer
    readonly_fields = ('id',)

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInLine]
    readonly_fields = ('id',)

class QuizAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Quiz, QuizAdmin)

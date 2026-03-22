from django.contrib import admin
from .models import Lesson, Question, Choice, Submission


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'lesson')
    inlines = [ChoiceInline]


class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    inlines = [QuestionInline]


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'question', 'is_correct')


class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'question', 'selected_choice', 'submitted_at')


admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Submission, SubmissionAdmin)

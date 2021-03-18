from django.contrib import admin
from .models import Choice, Question

# Register your models here.
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 4

admin.site.register(Choice)

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')

admin.site.register(Question)

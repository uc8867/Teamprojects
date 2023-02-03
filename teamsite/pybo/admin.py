from django.contrib import admin
from .models import Question
from .models import Answer

#질문 데이터를 제목(subject)으로 검색
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

# Register your models here.
admin.site.register(Question)
admin.site.register(Answer)
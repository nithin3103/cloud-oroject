from django import forms
from .models import Quiz, Question, Answer

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ('name', 'desc', 'no_of_questions')

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question', 'quiz')
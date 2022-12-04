from django.db import models

class Quiz(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)
    no_of_questions = models.IntegerField(default=1)

    def __str__(self):
        return self.name
    def get_questions(self):
        return self.question_set.all()

class Question(models.Model):
    question = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return self.question

    def get_answers(self):
        return self.answer_set.all()


class Answer(models.Model):
    answer = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
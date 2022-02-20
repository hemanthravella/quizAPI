from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Quizzes(models.Model):

    class Meta:
        verbose_name = _("Quiz")


    category = models.ForeignKey(Category, default=1, on_delete=models.DO_NOTHING)


class Question(UpdatedQuestion):
    quiz = models.ForeignKey(Quizzes, related_name='question',on_delete=models.DO_NOTHING)


class Answer(UpdatedQuestion):
    question = models.ForeignKey(Question, related_name='answer', on_delete=models.DO_NOTHING)

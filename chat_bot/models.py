from django.db import models

# Create your models here.


class ChatBotQuestion(models.Model):
    question = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.question



class ChatBotAnswer(models.Model):
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    question = models.ManyToManyField(ChatBotQuestion)
    
    def __str__(self):
        return self.answer

from django.db import models
from django.utils import timezone
import datetime
from django.utils.timezone import now

# Create your models here.
class Question(models.Model):

    def __str__(self):
        return self.question_text
    
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=now )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    def choice_count(self):
        return self.choices.all().count()
    def total_votes(self):
        total = 0
        for choice in self.choices.all():
            total = total + choice.votes;
        return total
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    def __str__(self):
        return self.choice_text
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
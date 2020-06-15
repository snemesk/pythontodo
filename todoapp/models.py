from django.db import models

# Create your'' models here.
Priority = (('danger','high'),('info','nomal'),('success','low'))
class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    note = models.TextField()
    priority = models.CharField(
        max_length = 50,
        choices = Priority
    )
    duedate = models.DateField()
    def __str__(self):
        return self.title
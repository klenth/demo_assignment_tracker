from django.db import models

# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=64, null=False, blank=False)

    def __str__(self):
        return self.title


class Assignment(models.Model):
    course = models.ForeignKey(to=Course, null=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=64, null=False, blank=False)
    due_date = models.DateField()
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=66)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

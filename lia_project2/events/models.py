from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
    
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    max_attendees = models.PositiveIntegerField()
    location = models.CharField(max_length=250)
    province = models.CharField(max_length=100, blank=True, null=True) 
    latitude = models.FloatField(null=True, blank=True)  
    longitude = models.FloatField(null=True, blank=True) 
    image = models.ImageField(upload_to='events/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="liked_events", blank=True)
    Favorited_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="favorite_events", blank=True)
    flagged_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="flagged_events", blank=True)


    def __str__(self):
        return self.title
    
  
class Comment(models.Model):
    event = models.ForeignKey(Event, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.event.title}"
    

class FavoriteEvent(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
            unique_together = ("user", "event")

    def __str__(self):
        return f"{self.user.username} favorite {self.event.title}"
    

class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    class Meta:
            unique_together = ("user", "event")

    def __str__(self):
        return f"{self.user.username} liked {self.event.title}"
    

class Flag(models.Model):
    REASON_CHOICES = [
        ('spam', 'Spam or Misleading'),
        ('abuse', 'Harassment or Abuse'),
        ('inappropriate', 'Inappropriate Content'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    reason = models.CharField(max_length=50, choices=REASON_CHOICES, default='other')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "event")

    def __str__(self):
        return f"{self.user.username} flagged {self.event.title} for {self.get_reason_display()}"

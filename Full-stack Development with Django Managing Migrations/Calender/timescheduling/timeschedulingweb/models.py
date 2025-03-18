from django.db import models

# Create your models here.
class TimeSlot(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return str(self.start_time).format('Y-m-d')

class TimeSlotRequest(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    created_at = models.DateField(auto_now_add=True)
    time_slot = models.ForeignKey('TimeSlot', on_delete=models.CASCADE, default=None, null=True)
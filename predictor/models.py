from django.db import models
import json
from django.utils import timezone

class Prediction(models.Model):
    input_data = models.TextField()  # Store serialized input data
    result = models.CharField(max_length=50)
    timestamp = models.DateTimeField(default=timezone.now)  # Ensure this field is included

    def save(self, *args, **kwargs):
        self.input_data = json.dumps(self.input_data)  # Serialize
        super().save(*args, **kwargs)

    def get_input_data(self):
        return json.loads(self.input_data)  # Deserialize

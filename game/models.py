from django.db import models
import json

class GameSave(models.Model):
    player_name = models.CharField(max_length=100)
    algorithm = models.CharField(max_length=20)
    difficulty = models.CharField(max_length=10)
    current_array = models.TextField()  
    original_array = models.TextField() 
    score = models.IntegerField(default=0)
    moves = models.IntegerField(default=0)
    step = models.IntegerField(default=0)
    hints_used = models.IntegerField(default=0)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def set_current_array(self, array):
        self.current_array = json.dumps(array)
    
    def get_current_array(self):
        return json.loads(self.current_array)
    
    def set_original_array(self, array):
        self.original_array = json.dumps(array)
    
    def get_original_array(self):
        return json.loads(self.original_array)
    
    def __str__(self):
        return f"{self.player_name} - {self.algorithm} ({self.difficulty})"
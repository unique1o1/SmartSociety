from django.db import models

class item(models.Model):
	STATUS_CHOICES = (
('draft', 'Draft'),
('published', 'Published')
)
	title= models.CharField(max_length=200)
	description= models.TextField()
	amount=models.IntegerField()
	gender=models.CharField(max_length=50, choices=STATUS_CHOICES, default='draft')
from django.db import models

class item(models.Model):
# 	STATUS_CHOICES = (
# ('male', 'Male'),
# ('female', 'Female')
# )
# 	title= models.CharField(max_length=200)
# 	description= models.TextField()
# 	amount=models.IntegerField()
# 	gender=models.CharField(max_length=50, choices=STATUS_CHOICES, default='male')
	name=models.CharField(max_length=50)
	message=models.TextField()
	number=models.IntegerField()
	email=models.EmailField()
	def __str__(self):
		return self.name
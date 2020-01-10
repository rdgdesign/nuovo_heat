from django.db import models

# Create your models here.
class Contact(models.Model):
	UNIT_CHOICE = (
		('gradi centigradi' ,'gradi centigradi'),
		('gradi fahrenheit','gradi fahrenheit')
	)
	unita = models.CharField(max_length= 200, choices= UNIT_CHOICE)
	# name = models.CharField(max_length = 100)
	# email = models.EmailField()
	temperatura  = models.DecimalField(decimal_places=2, max_digits=1000)
	umidita = models.DecimalField(decimal_places=2, max_digits=1000)
	# message = models.TextField()
	timestamp = models.DateTimeField(auto_now_add = True)

	# def __str__(self):
	# 	return self.name
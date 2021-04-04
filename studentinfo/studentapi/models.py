from django.db import models
#from django.contrib.auth.models import User

# Create your models here.

class studentmd(models.Model):
	stdname = models.CharField(max_length =100)
	stdclass = models.IntegerField(blank=True, null=True)
	stdrollno = models.IntegerField(blank=True, null=True)
	#usr = models.ForeignKey(User, on_delete=models.CASCADE)


	def __str__(self):
		return self.stdname
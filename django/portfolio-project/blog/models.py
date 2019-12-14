from django.db import models

# Create your models here.

class Blog(models.Model):
	title = models.CharField(max_length=255)
	body = models.TextField(null=True,default='')
	body2 = models.TextField(null=True,default='')
	body3 = models.TextField(null=True,default='')
	image = models.ImageField(upload_to = 'images/')
	def __str__(self):
		return self.title
		class Meta:
			verbose_name_plural = "Blogs"

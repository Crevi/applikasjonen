from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model): 
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=100)
	username = models.CharField(max_length=50)
	email = models.EmailField()

def __unicode__(self): 
	return u'%s %s' (self.first_name, self.last_name)

class CommentField(models.Model):
	user = models.ForeignKey(User, related_name='comments')
	comment = models.TextField()
	comment_by = models.ForeignKey(User, related_name="written_comments")
	comment_datetime = models.DateTimeField()

	def __unicode__(self):
		return u'%s' & self.comment

	#class Meta: 
		#ordering = ['-pub_date']
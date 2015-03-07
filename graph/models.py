from django.db import models

# Create your models here.
class Person(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)

	def __unicode__(self):
		return u'%s %s' % (self.first_name, self.last_name)

class PersonToTag(models.Model):
	person = models.ForeignKey(Person, related_name='people')
	tag = models.CharField(max_length=200)
	count =  models.IntegerField()

	def __unicode__(self):
		return u'%s %s - %s, %d' % (self.person.first_name, self.person.last_name, self.tag.title)

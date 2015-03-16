from django.db import models

# Create your models here.


class Section(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField('Photo', upload_to='dataomaha/', max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.name 
    class Meta:
        db_table = u'dataomaha_section'

class App(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    link = models.CharField(max_length=200)
    section = models.ForeignKey(Section)
    source = models.CharField(max_length=200, null=True, blank=True)
    featured = models.BooleanField('Featured Project?', help_text="Checking this box makes app appear in 'Featured Projects' section on left side of page", blank=True)
    section_feature = models.BooleanField('Highlight app within specific section?', blank=True)
    last_change = models.DateTimeField(auto_now=True)
    image = models.ImageField('Photo', upload_to='dataomaha/', max_length=200, null=True, blank=True)


    def __unicode__(self):
        return self.title
    class Meta:
        db_table = u'dataomaha_app'
	

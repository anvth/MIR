from django.db import models

from django.forms import ModelForm
# Create your models here.

class feature_extractor(models.Model):
	filename	= models.CharField(max_length=500)
	feature1	= models.IntegerField()
	label		= models.IntegerField() 

class Upload(models.Model):
    pic = models.FileField("Music File", upload_to="uploads/")    
    upload_date=models.DateTimeField(auto_now_add =True)

# FileUpload form class.
class UploadForm(ModelForm):
    class Meta:
        model = Upload
	

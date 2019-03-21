
# Create your models here.
from django.db import models
SAVED_FILES_DIR = r'files/'


class FileSto(models.Model):
    CATAGORY_CHOICE = {
        ('kejian','课件'),
        ('sheji','设计报告参考'),
        ('lunwen','论文'),
        ('qita','其他'),
    }
    cata = models.CharField(max_length=20,choices=CATAGORY_CHOICE,default='kejian',verbose_name='文件类别')
    file = models.FileField(upload_to=SAVED_FILES_DIR,verbose_name="文件选择" )
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.get_name()
    def get_name(self):
        return self.file.name.split('/')[-1]

# Receive the pre_delete signal and delete the file associated with the model instance.
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

@receiver(pre_delete, sender=FileSto)
def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.file.delete(False)
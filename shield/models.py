from django.db import models




class PostData(models.Model):

        data = models.TextField(("اعلان ها") , blank=True , null=True)
        time = models.DateTimeField(("زمان"), auto_now=False, auto_now_add=True )
        file = models.FileField(("فایل"), upload_to="upload/",blank=True , null=True)
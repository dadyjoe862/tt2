from django.db import models

class Files(models.Model):
    name = models.CharField(max_length=255, default='')
    path = models.CharField(max_length=255, default='')  # Assuming file paths are within 255 characters
    extension = models.CharField(max_length=10, default='')
    language = models.CharField(max_length=50)



    def __str__(self):
        return self.name

# class Files(models.Model):
#     name = models.CharField(max_length=255)
#     path = models.CharField(max_length=255)
#     extension = models.CharField(max_length=10)
#     language = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name
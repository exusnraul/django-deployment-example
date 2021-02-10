from django.db import models

# Create your models here.


class user_info(models.Model) :
    first_name =models.CharField(max_length=150)
    last_name =models.CharField(max_length=150)
    email_id=models.EmailField(max_length=254)

    def __str__(self):
        return self.first_name
    
    
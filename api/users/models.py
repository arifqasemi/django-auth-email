from django.db import models

# Create your models here.
from authemail.models import EmailUserManager, EmailAbstractUser,AbstractBaseCode,SignupCodeManager

class Customer(EmailAbstractUser):
	is_admin = models.BooleanField(default=False)
	date_of_birth = models.CharField('date of birth', max_length=50, null=True, blank=True)
	is_customer = models.BooleanField(default=False)

	objects = EmailUserManager()
 
 
 
 
class Profile(models.Model):
    user = models.ForeignKey(Customer,related_name='profile',on_delete=models.CASCADE,default=0)
    image = models.ImageField(upload_to='media',default='default.png',blank=True)
    
    def __str__(self):
        return str(self.image)
    
    
    
    
    
    







from django.db import models
from django.urls import reverse
#Clothes классының моделин курамыз
class Clothes(models.Model):

    clothes = models.CharField(max_length=200)
    firma= models.ForeignKey('Firma', on_delete=models.SET_NULL, null=True)
   
    description = models.TextField(max_length=1000, help_text=" clothes")
 #  isbn = models.CharField('ISBN',max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
  # clothes_name= models.ManyToManyField(Clothes_name, help_text="Select  for this clothes")
      
    def __str__(self):
         return self.clothes

    
    def get_absolute_url(self):

        return reverse('odezhda-detail', args=[str(self.id)])

import uuid 
#Clothes_name классын курамын
class Clothes_name(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="id")
    clothes = models.ForeignKey('Clothes', on_delete=models.SET_NULL, null=True) 
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'FIRMADAGY'),
        ('o', 'Satylymda'),
        ('a', 'Satylgan'),
    
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='d', help_text='Clothes_satylymda')

    class Meta:
        ordering = ["due_back"]
        

    def __str__(self):

        return '%s (%s)' % (self.id,self.clothes.clothes)

class Firma(models.Model):

    firma_name = models.CharField(max_length=100)
    date_of_creation = models.DateField(null=True, blank=True)

    
    def get_absolute_url(self):
      
        return reverse('firma-detail', args=[str(self.id)])
    

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.firma_name, self.date_of_creation)
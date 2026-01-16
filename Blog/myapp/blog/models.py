from django.db import models
from django.utils.text import slugify

#Category
class Category(models.Model):
     name = models.CharField(max_length= 100)#column 1  

     def __str__(self) :
         return self.name
       

# Create your models here.
class Post(models.Model):#post model to create columns for the table in database
    title = models.CharField(max_length=100)#column 1
    content = models.TextField()#column 2
    img_url= models.URLField(max_length=200,null=True)#column 3
    create_at = models.DateTimeField(auto_now_add=True)#column 4 for date and time field
    slug = models.SlugField(unique=True, null=True, blank=True)# column 5
    category = models.ForeignKey(Category, on_delete = models.CASCADE)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def __str__(self):  #Function for displaying title as default 
        return self.title


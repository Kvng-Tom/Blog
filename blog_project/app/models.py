from django.db import models
from django.forms import model_to_dict
# Create your models here.

class Author(models.Model):
    
    name = models.CharField(max_length=250)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




class Blog(models.Model):

    title = models.CharField(max_length=650)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    body = models.TextField()
    image = models.ImageField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


@property
def author_data(self):

    if self.author:
                                                    # return {
                                                    #     'id': self.author.id,
                                                    #     'name': self.author.name,
                                                    #     'email': self.author.email,
                                                    # }

        return model_to_dict(self.author, exclude=['id', 'age'])
            
    return {}

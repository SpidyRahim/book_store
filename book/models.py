from django.db import models

# Create your models here.


class BookStoreModel(models.Model):
    CATEGORY = (
        ('Mystery', 'Mystery'),
        ('Thriller', 'Thriller'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Humor', 'Humor'),
        ('Horror', 'Horror'),
    )
    id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=40)
    author = models.CharField(max_length=20)
    category = models.CharField(max_length=30, choices=CATEGORY)
    # django ekdom first date dekhabe
    first_pub = models.DateTimeField(auto_now_add=True)
    # erpor joto update korbo sei date dekhabe
    last_pub = models.DateTimeField(auto_now=True)
    # Allow blank and null for the image field
    cover_image = models.ImageField(
        upload_to='book_covers/', null=True, blank=True)

    def __str__(self):
        return self.book_name

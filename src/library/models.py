from django.db import models
from django.urls import reverse

# Create your models here.

class BookCategory(models.Model):
    name = models.CharField(
        max_length = 200,
        help_text="Enter book category (eg. Science, Maths, English..etc.)"
    )

    def __str__(self):
        return self.name
    
class Language(models.Model):
    name = models.CharField(
        max_length = 200,
        help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)"
    )

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(
        max_length = 120,
        help_text = "Enter the book title"
    )
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    summary = models.TextField(
        max_length=500,
        help_text="Enter a brief description of the book"
        )
    isbn    = models.CharField('ISBN', max_length=13,
                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn'
                                      '">ISBN number</a>')
    bookcategory = models.ManyToManyField(BookCategory, help_text="Select a book category for this book")
    # ManyToManyField used because a genre can contain many books and a Book can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)

    def display_bookcategory(self):
        return ', '.join([bookcategory.name for bookcategory in self.bookcategory.all()[:3]])

    display_bookcategory.short_description = 'BookCategory'

    def get_absolute_url(self):
        return reverse("library:book-detail", kwargs={"id": self.id})

    def __str__(self):
        return self.title
    
import uuid
from datetime import date
from django.contrib.auth.models import User

class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
        help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200, help_text="Give any random integer number")
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False
    
    LOAN_STATUS = (
        ('d', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='d',
        help_text='Book availability'
    )
    class Meta:
        ordering = ['due_back']
        permissions = (("can_mark_returned", "Set book as returned"),)
    
    def __str__(self):
        return '{0} ({1})'.format(self.id, self.book)

class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    # date_of_death = models.DateField('died', null=True, blank=True)

    class Meta:
        ordering = ['first_name', 'last_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse("library:author-detail", kwargs={"id": self.id})
        # return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return '{0} {1}'.format(self.first_name, self.last_name)
    

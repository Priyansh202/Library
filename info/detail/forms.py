from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    

    class Meta:
        model = Book
        fields = ('title', 'author', 'publisher', 'publication_date', 'isbn', 'category')
        widgets = {
            'publication_date': forms.DateInput(attrs={'type': 'date'})
        }
        
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 3:
            raise forms.ValidationError('Title must be at least 3 characters long.')
        return title
        
    def clean_author(self):
        author = self.cleaned_data.get('author')
        if not author.isalpha():
            raise forms.ValidationError('Author name must only contain letters.')
        return author
        
    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn')
        if not isbn.isdigit() :
            raise forms.ValidationError('ISBN must be a 10-digit number.')
        return isbn

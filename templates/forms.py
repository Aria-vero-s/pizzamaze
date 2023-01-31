from .models import Book
from bootstrap_modal_forms.forms import BSModalModelForm

class BookModelForm(BSModalModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price']
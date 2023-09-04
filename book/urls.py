# from django.urls import path
# from book.views import home, store_book, show_books
# from django.conf.urls.static import static


# urlpatterns = [
#     path('', home),
#     path('store_new_book/', store_book, name='storebook'),
#     path('show_books/', show_books, name='showbook'),
# ]


from django.urls import path
from book.views import home, store_book, show_books, edit_book, delete_book
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home),
    path('store_new_book/', store_book, name='storebook'),
    path('show_books/', show_books, name='showbook'),
    # <int:id> deyar fole edit_book ta "id" ke capture korbe
    path('edit_book/<int:id>', edit_book, name='editbook'),
    # <int:id> deyar fole edit_book ta "id" ke capture korbe
    path('delete_book/<int:id>', delete_book, name='deletebook'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

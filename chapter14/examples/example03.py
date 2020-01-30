>>> from book import Book
>>> python_book_1 = Book(
...     'Practical Programming',
...     ['Campbell', 'Gries', 'Montojo'],
...     'Pragmatic Bookshelf',
...     '978-1-6805026-8-8',
...     25.0)
>>> python_book_2 = Book(
...     'Practical Programming'
... ,
... ['Campbell', 'Gries', 'Montojo'],
... 'Pragmatic Bookshelf',
... '978-1-6805026-8-8',
... 25.0)
>>> python_book_1 == python_book_2
False
>>> python_book_1 == python_book_1
True
>>> python_book_2 == python_book_2
True

>>> from book import Book
>>> python_book = Book( 
...             'Practical Programming', 
...             ['Campbell', 'Gries', 'Montojo'], 
...             'Pragmatic Bookshelf', 
...             '978-1-6805026-8-8', 
...             25.0)
>>> python_book = Book( 
...             'Practical Programming', 
...             ['Campbell', 'Gries', 'Montojo'], 
...             'Pragmatic Bookshelf', 
...             '978-1-6805026-8-8', 
...             25.0)
>>> python_book_1 = Book(
... 'Practical Programming', 
...             ['Campbell', 'Gries', 'Montojo'], 
...             'Pragmatic Bookshelf', 
...             '978-1-6805026-8-8', 
...             25.0)

>>> python_book == python_book_1
True
>>> survival_book = Book(
...     "New Programmer's Survival Manual",
...     ['Carter'],
...     'Pragmatic Bookshelf',
...     '978-1-93435-681-4',
...     19.0)

>>> python_book_1 == survival_book
False
>>> python_book_1
python_book_1
>>> python_book_1
python_book_1
>>> python_book_1 == ['Not', 'a', 'book']
False
>>> 
# devclub-library
Django project made for IITD [DevClub](https://devclub.in/) [Inductions](https://drive.google.com/file/d/1HsUoeqMsSgESCTzvhPw9BpPWtIHfpGv6/view)

## Features
* Email notifications for user registered, book added, book requested/issued/returned and forgot password.
* Search books from the library by title, author, publisher, genre, summary or ISBN
* Autofill book details using ISBN with [Google Books API](https://developers.google.com/books/docs/v1/using#RetrievingVolume)
* Can also store PDF links for books

## Installation
* [python](https://www.python.org/downloads/)
* [virtual environment](https://code.visualstudio.com/docs/python/tutorial-django#_create-a-project-environment-for-the-django-tutorial)
```python3 -m venv env```
* django
```python3 -m pip install django```
* run ```python3 manage.py runserver```
## Environment Variables
```
export EMAIL_USER="<email>";
export EMAIL_PASS="<pass>";
```
## accounts
USERNAME | PASSWORD | PRIVILEDGE
---------|----------|-----------
admin | admin | admin
aditya | librarian1234 | librarian
user1 | pass@1234 | student
user2 | pass@1234 | student

## Design
There are models defined for each book, request, issue, return in `books/models.py`. First, the librarian creates a new book, then the student can browse them, and request a book. The librarian can see lists of requests and then chose to approve them and issue the book with a due date, the student gets notified. The librarian updates the records for each issue when it is returned.

The permissions are maintained using django's inbuilt groups, and I have used the appropriate `@permission_required` decorator for each view, to prevent unauthorised access. While initialising the database, the admin should add a Group 'Librarian' first and give the permissions to view book, add book, view request, add issue, view issue, add return, view return, and more if they wish to. Then they have to add a Group 'Student' and give the permissions to view book and add request.

The admin can use the django admin panel to give the Librarian group to the librarian, and also give staff access to the librarian so they can use the powerful django admin portal too for editing stuff.

This model allows a secure system where the data is changed only by backend and a history is maintained for all operations. The form fields are chosen in a way to not allow any unauthorized access, only the backend can change the booleans for available, approved and returned.

The database used is django's default `db.sqlite3`, it is secure and has many built in attack preventions. I have used django's inbuilt `django.contrib.auth` to securely authorise logins, it also hashes the passwords so they cannot be compromised.
The app hosted on heroku uses PostgreSQL which is more powerful.

Front end uses bootstrap for a nice and informative interface.

### Tutorials I watched to learn django
* [Programming with Mosh](https://www.youtube.com/watch?v=_uQrJ0TkZlc)
* [freecodecamp](https://www.youtube.com/watch?v=F5mRW0jo-U4)
* [Corey Schafer](https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)

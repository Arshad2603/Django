# Django
The Blog Application:(in-process)
This is a django based application where users can read and view others posts in this blog 
Files and purpose:

APP STRUCTURE FILES:
models.py :
->creates models called Post and Category and built schemas for it so post and category act as tables in mysql.
->Post model has a foreign key called category to link each post to a category and used slugify method to protect data from hackers whereas slugify is used to not reveal the post id instead shows the title in the URL For Example : future-of-AI

views.py:
->This is viewport of the app where it fetches all data from the Databse using Post Models and handles function detail and classes to return the fetched data.

urls.py:
->This direct the user requested URL path to respective function. For example: "post/<slug:slug>" directs to detail function in views that handles the data.

migrations.py:
-> This file handles or updates changes in models schemas. For example: When a new column called source or citation is added in the Post Model then after writing "python ./manage.py makemigrations" and "python ./manage.py migrate" This updates the respective field in the database.

HTML FILES:
header.html,footer.html:
-> acts as common header and footer for all html files to reduce repetition.

base.html:
-> contains bootstrap links,high-level HTML structure and includes the header.html and footer.html partials so one do not have to rewrite them for every page

index.html:
-> this file uses for loop to loop through the page_obj.

detail.html:
-> Displays full content of specific post including the date it was created

SCRIPT OR DATA FILES:
populate_posts.py:
-> Seeds the database with quality blog posts instantly.Utilises random.choice() to assign each post to random category not only that using zip() method it combines the title,content,images in one Post Object .
->Finally Loops through the List and uses ORM command Post.objects.create() to generate the database records and confirms with the success message

populate_category.py:
-> Ensures Database has required categories before the blog posts are created.Category.objects.all().delete() ensure no categories are present to prevent duplication.
->This script must be run before the post-population script because the Post model requires a valid Category ID for its ForeignKey relationship.
->Finally Loops through the List and uses ORM command Category.objects.create() to generate the database records and confirms with the success message


DEMO SCREENSHOTS:
<img width="1920" height="1080" alt="Screenshot (2201)" src="https://github.com/user-attachments/assets/df91911b-d9b5-41be-949e-61e65cb794bb" />
<img width="1920" height="1080" alt="Screenshot (2199)" src="https://github.com/user-attachments/assets/6960984f-b10d-462e-af76-3ca188a52c14" />
<img width="1920" height="1080" alt="Screenshot (2200)" src="https://github.com/user-attachments/assets/2fb5ae88-603d-4b32-be58-1e38d8f90404" />


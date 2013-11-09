BarterSpot
==============================================================
How to launch the project locally
----------------------------------------------------------------
Assuming that $PROJECT is the project's main directory:

* The file *$PROJECT/BarterSpot/settings.py* should contain paths to templates and static files in the project. 
They should be filled automatically. If there are any problems, add an **absolute** path to *$PROJECT/static* 
and *$PROJECT/templates* directories respectively into *STATICFILES\_DIRS* and *TEMPLATE\_DIRS* lists included in the *settings.py* .     

* Create a database with the parameters described in the *DATABASES['default']* included in the *settings.py* . 
One can change the parameters at their discretion. By default it is postgreSQL database with the name 'barterdb' 
and the user 'barterman' with the password 'barterman'.

Afterwards, in the $PROJECT run: *python manage.py syncdb*
which should create all the necessary tables in the datebase.

* Finally, again in the $PROJECT directory run:*python manage.py runserver [port]*.
The port is optional and by default is set to 8000. The website should be then available at *http://localhost:port* .

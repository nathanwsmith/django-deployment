# Openshift temlate for Django, Gunicorn, PostgreSQL and NGINX

Git:
* Django: https://github.com/nedialkom/my-openshift.git
* NGINX: https://github.com/nedialkom/nginx-openshift.git

Deployment:
1. Create new project in Openshift
2. Add new application "From Git" for Django application and for NGINX
3. Deploy PostgreSQL DB from Databases

Database settings:
PostgreSQL Database Name: 	    db
PostgreSQL Connection Password: my_password
PostgreSQL Connection Username: my_user
Database Service Name: 		    postgresql
Namespace:			            openshift
Namespace:			            myproject-mnv

4. Edit routes for 2 applications (django and NGINX) as in attached files
5. Do not forget to change user and password in /admin; 
Default user is admin
Default password is password
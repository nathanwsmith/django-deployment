# Openshift temlate for Django

Deployment:
1. Create new project in Openshift
2. Add new application "From Git" 
3. Deploy PostgreSQL DB from Databases

Database settings:
PostgreSQL Database Name: 	    
PostgreSQL Connection Password: 
PostgreSQL Connection Username: 
Database Service Name: 		    

Environment Variables:

Name: OPENSHIFT_PYTHON_DIR Value: /opt/app-root/lib/python
Name: OPENSHIFT_REPO_DIR   Value: /opt/app-root/src
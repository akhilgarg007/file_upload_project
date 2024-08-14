File upload project which summaries PDF, DOCX and PPTX files using predibase, django and mongodb.

Installation Instructions
- Install Python 3.8
- Install Mongodb https://www.mongodb.com/docs/manual/installation/
- Install pipenv https://pypi.org/project/pipenv/
- Run `pipenv shell`
- Run `pipenv install`
- Run `python manage.py migrate`
- Create superuser using `python manage.py createsuperuser` with username(`akhil`) and password(`akhil`). You can create your own username and password but you will have to edit the postman collection authentication
- Add your own predibase settings and add to .env file or use mine which are already populated
- Start server using `gunicorn file_upload_project.wsgi`
- Use the shared postman collection to test

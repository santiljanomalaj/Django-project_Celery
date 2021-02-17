# ABA Nerd Django
- [Production Deployment](https://abanerd-api.herokuapp.com/)
- [Development Deployment](https://abanerd-api-dev.herokuapp.com/)

## Swagger
     `http://<site-url>/swagger/`

## TODO
- Do a `Provider` + `Title` check vs just a title
- I need to ensure that `media type` and `credit type` objects are searched and not created.
- Ensure that URL are added to Provider records
- clean up the loggging
- create s3 buckets using terrafor,

## Resources
- ***Django General***
  - https://simpleisbetterthancomplex.com/tips/2017/07/03/django-tip-20-working-with-multiple-settings-modules.html
  - https://github.com/goinnn/django-multiselectfield
- ***Django Rest Framework (DRF)***
  - https://medium.com/swlh/build-your-first-rest-api-with-django-rest-framework-e394e39a482c
  - https://www.django-rest-framework.org/api-guide/filtering/#searchfilter
- ***Django S3 Storages***
  - https://simpleisbetterthancomplex.com/tutorial/2017/08/01/how-to-setup-amazon-s3-in-a-django-project.html
  - https://testdriven.io/blog/storing-django-static-and-media-files-on-amazon-s3/
- ***Zappa***
  - https://www.youtube.com/watch?v=Kjee33g1z84
  - https://cloudacademy.com/blog/zappa-or-how-to-go-serverless-with-django/
  - https://github.com/flipperpa/django-s3-sqlite
- ***Selective Fields***
  - https://sunscrapers.com/blog/the-ultimate-tutorial-for-django-rest-framework-selective-fields-and-related-objects-part-7/
- https://docs.djangoproject.com/en/3.1/howto/initial-data/
- https://www.django-rest-framework.org/api-guide/fields/#serializermethodfield
- https://www.django-rest-framework.org/api-guide/pagination/
- https://django-simple-history.readthedocs.io/en/latest/
- https://timmyomahony.com/blog/upload-and-validate-image-from-url-in-django

####Celery Implementation
    https://devcenter.heroku.com/articles/celery-heroku#using-remap_sigterm
    
    Running Celery worker
    celery --app abanerd  worker -l info
    
    Setting up celery in heroku
    https://devcenter.heroku.com/articles/celery-heroku
    
    CELERY ENV:
    
    BROKER_URL = 'redis://localhost:6379'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379'
    
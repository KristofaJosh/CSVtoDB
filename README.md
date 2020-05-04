
## How do I set up ?

#### you can use 
- Docker Compose
    - make sure you have docker desktop installed and shared drive checked.
    - run **docker-compose up --build** from the root directory
    ###### Setup DB
    you will need an account to view DB
    - you can create super user with docker by running
        - docker-compose run django python manage.py migrate
        - docker-compose run django python manage.py createsuperuser
        - docker-compose run django python manage.py makemigrations
        - docker-compose run django python manage.py migrate
        **docker-compose up**
    route is _localhost:8000/admin_
                                    
    
- Locally
    ###### Setup DB
        - create super user with python manage.py migrate
        - create super user with python manage.py makemigrations
        - create super user with python manage.py createsuperuser
    follow the instructions
    #
        - navigate into the backend folder and run **python manage.py runserver**
        - navigate into the frontend folder and run **yarn start**
        - you should have two web servers running and your web browser should open if not;
        - in your browser front end: enter http://localhost:3000
        - in your browser back end: enter http://localhost:8000
        
     
        
- Docker Image
    - Docker Frontend 
        - get the [image](https://hub.docker.com/repository/docker/chrisjosh/zeno_client)
        - docker pull chrisjosh/zeno_client
        
    - Docker Backend 
        - get the [image](https://hub.docker.com/repository/docker/chrisjosh/zeno_django_server)
        - or docker pull chrisjosh/zeno_django_server

    use docker run <image name> command to run the containers seperately

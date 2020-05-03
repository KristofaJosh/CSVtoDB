
## How do I set up ?

#### you can use 
- Docker Compose
    - make sure you have docker desktop installed and shared drive checked.
    - run **docker-compose up --build** from the root directory
        - consistently you can use **docker-compose up** after first build
    ###### View DB
        - run docker ps -a
            you should see two images
                1. zeno_django, copy the CONTAINER ID
                2. create super user with docker by running
                    
    
- Locally
    - navigate into the backend and run **python manage.py runserver**
    - navigate into the frontend and run **yarn start**
    you should have two web servers running and your web browser should open if not;
        - in your browser; enter http://localhost:3000
    ###### View DB
        - create super user with python manage.py createsuperuser
    follow the instructions
     
        
- Docker Image
    - Docker Frontend 
        - get the [image]()
        
    - Docker Backend 
        - get the [image]()
    
    use docker commands to run the containers seperately

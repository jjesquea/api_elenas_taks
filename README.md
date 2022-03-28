Hello Welcome to Elenas Tasks API

## Installation steps

1. Ensure you have docker installed.
2. Clone the repository.
3. Open a terminal inside the folder to build the docker images using the following command `docker-compose build`.
4. You can launch the application using `docker-compose up` to install dependencies, run migrations and start the django server.
- Note: If the above command did not apply the migrations please kill the docker execution and run the `docker-compose up` command again.
5. In other terminal also inside the folder you can create data fake using the following command `docker-compose run web python factory.py`(Optional).
- Note: If I run step five you can use the following credentials email:`test1@test.com` and password:`Admin123$` to get the access token.
6. You can test the data loaded in the previous step directly from POSTMAN by importing the collections and creating an environment with the `access_token -> user token` and `host -> localhost:8000` variables that are in `Elenas.postman_collection.json` file, that is in the project folder (Optional).
7. To run the tests opening other terminal inside the folder run the following command `docker-compose run web python manage.py test`

Thank you very much for the opportunity.
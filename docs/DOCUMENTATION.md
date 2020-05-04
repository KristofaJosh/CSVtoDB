This is a **Minimal Viable Product** that illustrates extracting data from the provided CSV file and sending it to a database, 
after which, this data is presented to the user in a web app.

##### For this project assumptions are:
- Single data will not be deleted but all
- Data will and can only be modified if it exists else new record will be created
- CSV has a defined format [id, temperature, duration, timestamp] any other format will not work.

##### Choice of Database
- for this project, I chose to use **sqlite3** for it's portability and serverless operations.

##### Application
- I speculated between using _pandas_ module or the inbuilt _csv_ module python provides. Both will achieve the same task 
for this exercise, although I decided to use the pandas module because I find it more comfortable.
- Logging the GET request, I didn't understand the question entirely ( On each GET request, log that the data was requested)
    - my assumption is each time the web app was visited, the GET request should be logged.
    
##### Methods Used for API
- GET 
- PATCH 

_PATCH method is used to make changes to part of the data_
_PUT method was not used because it only allows a complete replacement of a document._

###### Middleware
- a custom middle ware was built in this project to filter the Get request and log it in the database, loggers cannot log request
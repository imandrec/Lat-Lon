# Getting Started with Latitude Longitude Program

This project was created with python

You need to have Docker install in your machine
### `git clone https://github.com/imandrec/Lat-Lon.git`
go to the directory where you have Lat-Lon
### `docker build -t task .`

### `docker run --rm task [IP ADDRESS]`

### Acknowledgments

*IPStack for providing the geolocation API.
*The Python community for their valuable packages.

### Rate Limiting

Lat-Lon includes rate limiting to prevent abuse of the IPStack API. The default rate limit is set to 5 requests per minute. If you exceed the rate limit, you will receive a "Rate limit exceeded" message. You can adjust the rate limit settings in the task.py file.

### Security

To improve security, I am using the 'dotenv' library to load sensitive environment variables from a hidden '.env' file. This helps in keeping sensitive information, such as API keys and credentials, out of the codebase and away from public repositories.

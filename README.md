# Getting Started with Latitude Longitude Program

This project was created using Docker

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

# Documentation

The "Url Shortener" project is a simple application that allows users to create and use short URLs. To set up the project, you need Docker installed on your system. Once you have Docker ready, build the containers using the given command and start the application using Docker Compose. For usage, users need to log in to the application to obtain a token, which they can then use to create a short URL. The generated short URLs can be used to redirect to the original URLs.

## Setup

### Prerequisites
- Docker

### Installation
To set up the project, follow these steps:
1. Build the Docker containers with the following command:
    * docker-compose build --no-cache

2. Start the application using Docker Compose:
    * docker-compose up 

## Usage

### Create a Short URL
To create a short URL, follow these steps:
* Login to the application and obtain the token from the response.
* Use the obtained token to create a short URL.
    * Add token to headers:
      * Authorization: Bearer token
* Use the generated short URL to redirect to the original URL.
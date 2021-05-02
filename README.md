# webfortune
Final project for my Development and Operations class.
## Description
webfortune provides a web frontend for the linux `fortune` and `cowsay` commands. These commands are accessible from the following routes:

`<web-address>/fortune/` - Displays a random fortune.

`<web-address>/cowsay/<message>/` - Displays a cow that's saying your entered message.

`<web-address>/cowfortune/` - Displays a cow that is telling you a random fortune.

`<web-address>/` - Redirects to `<web-address>/fortune/`.

## Operating webfortune from the command line
### Prerequisites
To run the server, you must have `python3`, `pip3`, and `virtualenv` installed.

### Setup
Clone this repository to the directory of your choice. Then enter that directory and create a virtual environment with the command `virtualenv -p python3 env`, then source that environment by running `source env/bin/activate`, and finally install dependencies by running `pip3 install -r requirements.txt`.

### Running the server
While still in your virtual environment, run `flask run --host=0.0.0.0 --port=<port_num>` to start the server on localhost.

### Testing the server
To make sure the server code is behaving properly, you can run `pytest` within your virtual environment, as long as you are the top-level webfortune directory.

### Shutting down
The server can be stopped with a keyboard interupt, and you can leave your virtaul environment by running `deactivate`.

## Operating webfortune from a Docker container
### Prerequisites
You must alread have `docker` installed.

### Setup
Clone this repository, enter the directory that's created and run `docker build -t webfortune .`.

### Running the server
To start the server, enter `docker run -dp <desired_port>:5000 webfortune`.

### Shutting down
To get the container ID of your running docker image, run `docker ps`. Then, to close the server, enter `docker stop <your_container_ID>`.

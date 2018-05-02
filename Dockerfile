FROM python:3.6.5-slim

LABEL maintainer="Callum Kift"

# Set the working directory to /app
WORKDIR /app

# Copying over source code and requirements file
COPY ["src", "requirements.txt", "/app/"]

# Installing the requirements for the app
RUN pip install -r /app/requirements.txt

# Make port available to the world outside this container
EXPOSE 5000

# ENTRYPOINT allows us to specify the default executible
ENTRYPOINT ["python"]

# CMD sets the default arguments to executible, which may be overwritten when using `docker run`
CMD ["api/app.py"]



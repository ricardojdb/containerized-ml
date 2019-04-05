# Select image to use as base for your specific model
FROM # TODO

# Docker commands to run the container
LABEL # TODO

# Create app folder
RUN mkdir /app

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt /app

# Local directory as a volume
VOLUME /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port available to the world outside this container
EXPOSE 7000 

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
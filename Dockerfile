# Use an official Python runtime as the parent image
FROM python:3.9-slim

# Set the working directory in the docker image
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./ /app/

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Define environment variable for Streamlit
ENV STREAMLIT_SERVER_PORT 8501

# Run entrypoint.py when the container launches
CMD ["streamlit", "run", "main.py"]

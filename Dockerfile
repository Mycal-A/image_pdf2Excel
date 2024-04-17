FROM --platform=linux/x86-64 python:slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app
WORKDIR /app

# Install necessary system packages
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    tesseract-ocr \
    tesseract-ocr-eng \
    && rm -rf /var/lib/apt/lists/*

# Install Flask and other required packages
RUN pip install --no-cache-dir flask img2table boto3 requests

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP app.py

ENTRYPOINT [ "python3" ]
CMD [ "./app.py" ]

# Use the base image specified in your compose file
FROM gingersociety/db-compose-runtime-prod:latest

# Expose the application port
EXPOSE 8000

# Copy the relevant files into the container
COPY models.py /app/src/models.py
COPY admin.py /app/src/admin.py
COPY migrations /app/src/migrations

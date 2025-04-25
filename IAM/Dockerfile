# Use the base image specified in your compose file
FROM containers.gingersociety.org/gingersociety/ginger-db-compose-runtime:prod

# Expose the application port
EXPOSE 8000

RUN rm -r /app/src/migrations

# Copy the relevant files into the container
COPY models.py /app/src/models.py
COPY admin.py /app/src/admin.py
COPY migrations /app/src/migrations

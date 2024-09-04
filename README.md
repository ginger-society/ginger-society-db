

```sh
docker run --env-file ./.env \
  -v ./models.py:/app/src/models.py \
  -v ./admin.py:/app/src/admin.py \
  -v ./migrations:/app/src/migrations \
  gingersociety/db-compose-migrator:latest


```

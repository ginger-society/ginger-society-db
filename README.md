
# This is the database repo for all the cloud hosted service of Ginger Society

This kind of repo is supposed to be one per workspace hence the name `ginger-society-db`

To run migrations , navigate to the repo and run the following command

```sh
docker run --env-file ./.env \
  -v ./models.py:/app/src/models.py \
  -v ./admin.py:/app/src/admin.py \
  -v ./migrations:/app/src/migrations \
  gingersociety/db-compose-migrator:latest


```

# simple-web-benchmarking

Simple project for benchmarking web response of different web stacks.

* node - express
* node - fastify
* python - flask
* python - fastapi
* go - bare server

more to come...

## Instructions

In order to setup the projects:

```bash
docker-compose up
```

To run the test:

```
siege -c 40 -t 10s http://localhost:9051/
```

| stack | url |
|-------|-----|
| node express   | http://localhost:9051/ |
| node fastify   | http://localhost:9052/ |
| python flask   | http://localhost:9053/ |
| python fastapi | http://localhost:9054/ |
| go base server | http://localhost:9055/ |


## notes

No optimization has been perfomed and the docker configurations are very simple but supports autoreload for all stacks.

Next tests:

* simple redis operation
* simple postgres read
* postgres write / update



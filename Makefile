DEV_DOCKER_COMPOSE_FILE = 'dev.dockerfile.yml'

start-dev:
	docker-compose -f ${DEV_DOCKER_COMPOSE_FILE} up -d

stop-dev:
	docker-compose -f ${DEV_DOCKER_COMPOSE_FILE} down

restart-dev:
	make start-dev
	make stop-dev
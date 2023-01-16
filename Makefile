ifneq (,$(wildcard ./.env))
include .env
export
ENV_FILE_PARAM = --env-file .env


endif

build:
	docker compose up --build -d --remove-orphans

up:
	docker compose up -d

down:
	docker compose down 

show-logs:
	docker compose logs

migrate:
	docker compose exec ece-blog python3 manage.py migrate

makemigrations:
	docker compose exec ece-blog python3 manage.py makemigrations

superuser:
	docker compose exec ece-blog python3 manage.py createsuperuser

collectstatic:
	docker compose exec ece-blog python3 manage.py collectstatic --no-input --clear

down-v:
	docker compose down -v

volume:
	docker volume inspect eceblog_postgres_data

# home-sales-db:
# 	docker compose exec postgres-db psql --username=admin --dbname=postgres

# pytest:
# 	docker compose exec ece-blog pytest -p no:warnings --cov=.

# pytest-html:
# 	docker compose exec ece-blog pytest -p no:warnings --cov=. --cov-report html

# flake8:
# 	docker compose exec ece-blog flake8 .

# black-check:
# 	docker compose exec ece-blog black --check --exclude=migrations .

# black-diff:
# 	docker compose exec ece-blog black --diff --exclude=migrations .
	
# black:
# 	docker compose exec ece-blog black --exclude=migrations .

# isort-check:
# 	docker compose exec ece-blog isort . --check-only --skip env --skip migrations

# isort-diff:
# 	docker compose exec ece-blog isort . --diff --skip env --skip migrations

# isort:
# 	docker compose exec ece-blog isort . --skip env --skip migrations

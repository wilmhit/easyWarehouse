PYMANAGE = poetry run python easywarehouse/manage.py

format:
	poetry run black easywarehouse --exclude migrations
	poetry run isort easywarehouse

makemigrate:
	$(PYMANAGE) makemigrations
	$(PYMANAGE) migrate

migrate:
	$(PYMANAGE) migrate

runserver:
	$(PYMANAGE) runserver

superuser:
	DJANGO_SUPERUSER_PASSWORD=admin \
	DJANGO_SUPERUSER_USERNAME=admin \
	DJANGO_SUPERUSER_EMAIL=admin@easywarehouse.local \
	$(PYMANAGE) createsuperuser  --noinput

dumpdata:
	$(PYMANAGE) dumpdata images.Image categories.Category products.Product  -o data/dump.json --format json

loaddata:
	$(PYMANAGE) loaddata data/dump.json

flush:
	$(PYMANAGE) flush --noinput

resetdb:
	$(PYMANAGE) reset_db

removecontainers:
	docker rm ew_logstash ew_pgadmin ew_postgres ew_kibana ew_elasticsearch

removevolumes:
	docker volume rm easywarehouse_es_data easywarehouse_psql_data easywarehouse_pgadmin_data

removealldocker: removecontainers removevolumes

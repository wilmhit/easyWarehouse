PYMANAGE = python easywarehouse/manage.py

format:
	poetry run black easywarehouse
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

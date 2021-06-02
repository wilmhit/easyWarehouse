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
	$(PYMANAGE) dumpdata products.Image products.Category products.Product  -o data/dump.json --format json

loaddata:
	$(PYMANAGE) loaddata data/dump.json

flush:
	$(PYMANAGE) flush --noinput

resetdb:
	$(PYMANAGE) reset_db

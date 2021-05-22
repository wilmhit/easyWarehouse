MANAGE = easywarehouse/manage.py
PYMANAGE = python $(MANAGE)

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

add-admin:
	$(PYMANAGE) createsuperuser --username admin --email admin@127.0.0.1


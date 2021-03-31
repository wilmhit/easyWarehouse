# easyWarehouse

## Development

0. Dependencies are managed with poetry. You can install poetry with command:
```python -m pip install poetry```
   
1. To initialize virtualenv and install packages, run: ```poetry install```
 
2. All databases and their admin panels are defined in *docker-compose.py*. To run all of them type:
```docker-compose up```. To run particular service, enter: ```docker-compose up <service-name>```
   
3. To start the server, run: ```python easywarehouse/manage.py runserver```
   
4. Before pushing your changes, format the code with black and isort: ```make format```

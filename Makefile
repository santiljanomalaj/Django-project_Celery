ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

su :
		python manage.py createsuperuser

mm :
		python manage.py makemigrations

migrate :
		python manage.py migrate

abanerd-mm :
		python manage.py makemigrations abanerd

abanerd-migrate :
		python manage.py migrate abanerd

migrateall :
		make mm && make migrate && make abanerd-mm && make abanerd-migrate

initdata :
		python manage.py loaddata data/static.json # this is the CEUType and CEUMedia items

reinit :
		rm -rf abanerd/migrations/ && rm db.sqlite3 && make migrateall && make initdata
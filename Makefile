SHELL := /bin/bash

.PHONY:
	clean
	init_env
	vue
	vue_dev
	assets
	migrations
	migrate
	shell
	jsreverse
	deploy
	build_base
	setup_node
	gunicorn_start
	gunicorn_stop
	gunicorn_restart
	beat_start
	beat_stop
	beat_restart
	workers_prod_start
	workers_prod_stop
	workers_prod_restart


clean:
	find . -iname "*.pyc" | xargs rm -Rf
	find . -iname "*.pyo" | xargs rm -Rf
	find . -iname "*.pyd" | xargs rm -Rf
	find . -iname "__pycache__" | xargs rm -Rf

init_env:
	make build_base
	source scripts/build/web/create_user.sh

vue_dev:
	rm -rf app/assets/webpack_bundles/*.js;
	cd frontend; npm run build_dev; cd -;
	mv app/assets/webpack_bundles/*.js app/assets/webpack_bundles_build/;
	mv app/assets/webpack_bundles_build/*.js app/assets/webpack_bundles/;
	make assets

vue:
	rm -rf app/assets/webpack_bundles/*.js;
	rm -rf app/assets/webpack_bundles/*.map;
	cd frontend; npm run build; cd -;
	mv app/assets/webpack_bundles_build/*.js app/assets/webpack_bundles/;
	mv app/assets/webpack_bundles_build/*.map app/assets/webpack_bundles/;
	make assets

build_base:
	source scripts/utils/set_env_var.sh
	make clean
	pip install -r requirements/base.pip

deploy:
	make build_base
	make assets
	make jsreverse
	make migrations
	make migrate
	make gunicorn_start
	make workers_prod_restart
	make beat_restart

gunicorn_start:
	source scripts/gunicorn/start.sh

gunicorn_stop:
	source scripts/gunicorn/stop.sh

gunicorn_restart:
	source scripts/gunicorn/restart.sh

beat_start:
	source scripts/celery/beat/start.sh

beat_stop:
	source scripts/celery/beat/stop.sh

beat_restart:
	source scripts/celery/beat/restart.sh

workers_prod_start:
	source scripts/celery/workers/prod/start.sh

workers_prod_stop:
	source scripts/celery/workers/prod/stop.sh

workers_prod_restart:
	source scripts/celery/workers/prod/restart.sh

setup_node:
	apt update -y
	apt install -y curl
	curl -sL https://deb.nodesource.com/setup_9.x | sudo -E bash -
	apt install -y nodejs
	npm install -g npm

assets:
	python3 manage.py collectstatic --no-input -v 0

shell:
	python3 manage.py shell

migrations:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

jsreverse:
	python3 manage.py collectstatic_js_reverse

superuser:
	python3 manage.py createsuperuser

startapp:
	mkdir ./app/$(APP)
	python3 manage.py startapp $(APP) ./app/$(APP)

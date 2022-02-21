# install all the python package from requirements.txt in editable mode
deps:
	pip install --upgrade pip
	pip install -r requirements.txt
	pip install --editable .
	( \
       . .env/bin/activate; \
    )

# create python3 virtual environment .env
dev-env:
	python3 -m venv .env

env:
	source .env/bin/activate

# start the docker container in background
infra-up:
	docker-compose up -d

# stops the conatiner and removes volumes, images created by UP command.
infra-down:
	docker-compose down

alembic:
	alembic init alembic

# upgrade to newest version
alembic-up:
	alembic upgrade head

# revise to previous version
alembic-down:
	alembic downgrade head

run:
	iam start-server
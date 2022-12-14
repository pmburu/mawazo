format:
	#format code
	black *.py posts/*/*.py
lint:
	#flake8 or #pylint
	pylint --disable=R,C *.py mylib/*.py
test:
	#test
	# python -m pytest -vv --cov=mylib --cov=main test_*.py
build:
	#build container
	docker compose build
run:
	#run docker
	docker compose up -d
deploy:
	#deploy
	# aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 561744971673.dkr.ecr.us-east-1.amazonaws.com
	# docker build -t fastapi-wiki .
	# docker tag fastapi-wiki:latest 561744971673.dkr.ecr.us-east-1.amazonaws.com/fastapi-wiki:latest
	# docker push 561744971673.dkr.ecr.us-east-1.amazonaws.com/fastapi-wiki:latest

all: format lint run

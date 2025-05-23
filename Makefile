.PHONY: build run-local run-docker-local package docker-package deploy

S3_BUCKET_NAME := gemtech-lfn-packages-prod
S3_BUCKET_KEY := DCW/mail-service/main.zip
LAMBDA_FUNCTION_NAME := dcw-mail-service

# Build the Docker image for the FastAPI application
build:
	docker build -t fastapi-lambda .

# Run the FastAPI application locally using Uvicorn
run-local:
	uvicorn app.main:app --reload

# Run the FastAPI application in Docker
run-docker-local:
	docker run -p 8080:8080 fastapi-lambda

# Package the application for deployment using local environment
package:
	rm -rf package
	mkdir -p package
	pip install -t package -r requirements.txt
	cp -r app package
	cd package && zip -r ./main.zip .

# Package the application for deployment using Docker (consistent with AWS Lambda environment)
docker-package:
	rm -rf package
	mkdir -p package
	docker run --rm \
		--entrypoint /bin/bash \
		-v $(PWD):/var/task \
		-w /var/task \
		public.ecr.aws/lambda/python:3.10 \
		-c "yum install -y zip && pip install -r requirements.txt -t package && cp -r app package/ && cd package && zip -r ./main.zip ."

# Push the packaged application to S3
push-to-s3:
	aws s3 cp package/main.zip s3://$(S3_BUCKET_NAME)/$(S3_BUCKET_KEY)

# Deploy the packaged application to AWS Lambda
deploy:
	aws lambda update-function-code --function-name $(LAMBDA_FUNCTION_NAME) --s3-bucket $(S3_BUCKET_NAME) --s3-key $(S3_BUCKET_KEY)

# Combined target to package, push to S3, and deploy using Docker package process
deploy-all: docker-package push-to-s3 deploy

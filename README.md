# Machine-Learning-Project-0
pip install -r requirements.txt
---
Set up CI/CD Pipeline in heroku needs 3 information:
1. HEROKU_EMAIL = ericdataguy77@gmail.com
2. HEROKU_API_KEY = e808c6da-cd04-4b2e-953d-44b5fc25d8cb
3. HEROKU_APP_NAME = ml-regression-eric-pipeline
--- 
Build Docker images
docker build -t <image_name>:<tag_name> .
docker build -t ml-project:lastest .

Notes: image_name must be lower case.

To list docker images:
docker images

To run docker images:
docker run -p 5000:5000 -e PORT=5000 <docker_images_ID>

To check running docker
docker ps

To stop docker
docker stop <container_id>


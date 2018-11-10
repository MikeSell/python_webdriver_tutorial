# Setup Selenium Grid with Docker containers 

## Requirements

- Docker installed and running 
- docker-compose yaml file ready 

#### Install Docker Compose 

`pip install docker-compose`

#### Pull Docker images

```bash
sudo docker pull selenium/hub
sudo docker pull selenium/node-chrome
sudo docker pull selenium/node-firefox
```

## Managing Selenium Grid 

### Start 
sudo docker-compose up -d --scale chrome=3 --scale firefox=2

### Stop 
sudo docker-compose down

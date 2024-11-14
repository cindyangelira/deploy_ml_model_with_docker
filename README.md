# Dockerize Your Machine Learning Model

This is simple demo for dockerizing the ML model.

### Build Docker Image
```
docker build -t logregml:1.0 .
```

### Run Docker Container
```
docker run --name logregmodel -p 8080:8080 logregml:1.0
```

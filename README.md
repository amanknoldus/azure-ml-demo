## End to End MAchine Learning Project



## Run from terminal:

docker build -t testdemoregistry.azurecr.io/mltest:latest .

docker login testdemoregistry.azurecr.io

docker push testdemoregistry.azurecr.io/mltest:latest

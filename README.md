# YELP
A collection of Problems based on Yelp data set

## Setup

Browse to the root folder/directory where the following code base has been cloned. For example,

```
cd ~/my/favourite/place/YELP
```

Assuming you have docker installed, all you need is to follow these steps.
Build the docker image

```
docker build -t yelp .
```

and running the image

```
docker run -v /<data-path>/yelp_dataset_challenge_academic_dataset:/src/data yelp
```
A quick note, we load systems local folder as the data source and tell the container where
to find the data. Look [here](https://docs.docker.com/engine/tutorials/dockervolumes/) for mounting Docker volumes.

## Potential Tasks


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

* **Predict checkins at a business**
    + Use the business and checkins data together to predict the number of checkins.
* **User Social network analysis**
    + Given the users and their followers we can analyse them as an undirected graph. Hence,
    it can enable to identify those influential users
* **Recommendation Engine**
    + We can recommend business to users. We can clearly see the user-business relationships via a
    set of reviews. A review is a star hence, we can predict how likely is an user to rate a business and also
    his list of top-k businesses he might like
* **Tour guide**
    + Suggest users good places for drinks/cafe based on the geo locations of the businesses. This is easier and  can be thought of as
    a extension of the recommendation engine but based on geo locations. Once, we know users preferences, its about filtering the
    final recommendations based on location proximity.
* **Automatically rate**
    + based on users reviews, we can automatically rate (in terms os star). This is more like sentiment analysis
    task.



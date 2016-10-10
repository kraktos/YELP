import pandas as pd

if __name__ == '__main__':
    df = pd.read_json("file://localhost/Users/arnabdutta/Downloads/yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_checkin.json")
    print("DF = {}".format(df.shape))
    print("Done..")
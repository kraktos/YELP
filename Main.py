"""
Inception Point
"""
import DataProcessor as data_proc
import Setup as setup
import Reviews_Rating_Predict as review_rater


if __name__ == '__main__':

    # prefix to say where the data is lying
    prefix = setup.data_path if True else "data/"

    df_review = data_proc.json_to_dataframe(prefix + 'yelp_academic_dataset_review_small.json')

    # call the review rating engine
    review_rater.rate(df_review)

    # once loaded all the dataframes, perform relevant joins to derive relevant dataframes
    print("Done..")
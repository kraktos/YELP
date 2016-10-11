import DataProcessor as data_proc
import Setup as setup

if __name__ == '__main__':

    # prefix to say where the data is lying
    prefix = setup.data_path if False else "data/"

    df_checkin = data_proc.json_to_dataframe(prefix + 'yelp_academic_dataset_checkin.json')
    print "Checking data loaded {}".format(df_checkin.shape)

    df_business = data_proc.json_to_dataframe(prefix + 'yelp_academic_dataset_business.json')
    print "Business data loaded {}".format(df_business.shape)

    df_tip = data_proc.json_to_dataframe(prefix + 'yelp_academic_dataset_tip.json')
    print "Tip data loaded {}".format(df_tip.shape)

    df_user = data_proc.json_to_dataframe(prefix + 'yelp_academic_dataset_user.json')
    print "User data loaded {}".format(df_user.shape)

    # df_review = data_proc.json_to_dataframe(prefix + 'yelp_academic_dataset_review.json')
    # print "Review data loaded {}".format(df_review.shape)
    
    print("Done..")
"""
This class takes the reviews given by user and tries to predict the star rating.
A variant of sentiment analysis task where we do not decide necessarily a 'Positive'
 or 'Negative' sentiment but a continuous rating.
"""


def feature_engineered(df):
    """
    take the votes and create normalised features from it
    """
    # pre populate with all 0 s
    df['funny'] = 0
    df['cool'] = 0
    df['useful'] = 0

    # parse the votes to create features
    for index, row in df.iterrows():
        val_dict = row['votes']
        for key in val_dict:
            # for any number of votes, we consider it as boolean
            if val_dict[key] > 0:
                df.loc[index, key] = 1

    # drop this column
    del df['votes']

    return df


def rate(df):
    print "Review data loaded {}".format(df.shape)

    # keep the columns needed
    imp_column_names = ['business_id', 'date', 'votes', 'text', 'stars']
    new_df = df.loc[:, imp_column_names]

    # feature engineering
    new_df = feature_engineered(new_df)

    # take the new dataframe to train/test models

    print new_df.shape
    # new_df['clean_text']

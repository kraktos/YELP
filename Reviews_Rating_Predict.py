"""
This class takes the reviews given by user and tries to predict the star rating.
A variant of sentiment analysis task where we do not decide necessarily a 'Positive'
 or 'Negative' sentiment but a continuous rating.
"""
import nltk as nltk
from nltk.corpus import stopwords
from string import punctuation
from nltk import PorterStemmer
from nltk import word_tokenize, WordNetLemmatizer
from collections import Counter
from nltk import NaiveBayesClassifier, classify

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
stop = set(stopwords.words('english'))
stemmer = PorterStemmer()
wnl = WordNetLemmatizer()


def perform_nlp(text):
    """
    remove English stopwords
    removes punctuations
    lemmatizes words
    stems words
    """

    text = ''.join(c for c in text if c not in punctuation)

    # tokenize the sentence
    text = word_tokenize(text)

    # lemmatize sentence
    text = [wnl.lemmatize(word) for word in text if not word in stop]

    # stem words to root form
    text = [stemmer.stem(word.strip()) for word in text]

    return text


def get_features(text, setting):
    if setting=='bow':
        return {word: count for word, count in Counter(text).items()}
    else:
        return {word: True for word in text if word not in stop}


def evaluate(train_set, test_set, classifier):
    """
    evaluate the classifier performance
    """
    # check how the classifier performs on the training and test sets
    print ('Accuracy on the training set = ' + str(classify.accuracy(classifier, train_set)))
    print ('Accuracy of the test set = ' + str(classify.accuracy(classifier, test_set)))

    # check which words are most informative for the classifier
    classifier.show_most_informative_features(20)


def model_classifier(df):
    """
    splits the data into train and test and fits a classifier on training
    """
    train_size = int(len(df) * 0.75)

    # initialise the training and test sets
    train_set, test_set = df[:train_size], df[train_size:]

    print ('Training set size = ' + str(len(train_set)) + ' reviews')
    print ('Test set size = ' + str(len(test_set)) + ' reviews')

    # train the classifier
    classifier = NaiveBayesClassifier.train(train_set)
    return train_set, test_set, classifier


def feature_engineered(df):
    """
    take the votes and create normalised features from it
    """
    # pre populate with all 0 s
    # df['funny'] = 0
    # df['cool'] = 0
    # df['useful'] = 0

    # parse the votes to create features
    # for index, row in df.iterrows():
    #     val_dict = row['votes']
    #     for key in val_dict:
    #         # for any number of votes, we consider it as boolean
    #         if val_dict[key] > 0:
    #             df.loc[index, key] = 1

    # stem, lemmatize, stop word removal of the texts
    df['text'] = df['text'].apply(lambda x: perform_nlp(x.lower()))

    # create a review length as an additional feature
    # df['review_length'] = df['text'].apply(lambda x: len(x))
    df['text_feature'] = df['text'].apply(lambda x: get_features(x, 'bow'))

    # re define the target variable as 1 or 0
    df['label'] = df['stars'].apply(lambda x: 0 if x <= 3 else 1)

    # drop these columns
    del df['votes']
    del df['text']
    del df['stars']

    return df


def rate(df):
    print "Review data loaded {}".format(df.shape)

    # keep the columns needed
    new_df = df.loc[:, ['votes', 'text', 'stars']]

    # feature engineering
    new_df = feature_engineered(new_df)

    # create a list of tuples from the dataframe
    feature_label_data = [tuple(x) for x in new_df.to_records(index=False)]

    # take the new dataframe to train/test models
    train_set, test_set, classifier = model_classifier(feature_label_data)

    # evaluate its performance
    evaluate(train_set, test_set, classifier)

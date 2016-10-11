import DataProcessor as data_proc
import Setup as setup

if __name__ == '__main__':
    # json_file = "/Users/arnabdutta/Downloads/yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_checkin.json"

    df_checkin = data_proc.json_to_dataframe('data/yelp_academic_dataset_checkin.json')

    # df_business = data_proc.json_to_dataframe()
    # df_tip = data_proc.json_to_dataframe()
    # df_user = data_proc.json_to_dataframe()
    # df_review = data_proc.json_to_dataframe()

    print df_checkin.shape

    # column_names = j2c.get_superset_of_column_names_from_file(json_file_path=json_file)
    # j2c.read_and_write_file("world_bank.json", "world_bank.csv", column_names)

    print("Done..")
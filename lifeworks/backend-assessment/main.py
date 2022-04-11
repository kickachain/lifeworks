import os
import json
import logging
from lib.modify_json_data import is_user, is_company, add_full_name, over_age_limit, add_related_company


def get_json_data_from_file(file_path):

    """
    uses the os module to get the file from the relative path provided
    andread the contents
    """
    rel_path = os.path.relpath(file_path)

    try:
        with open(rel_path, encoding='utf-8') as json_file:
            data = json.load(json_file)
    except IOError as _e:
        logging.error(f'failed to open file for {file_path}', _e)

    return data


def create_updated_json_file(updated_data_file_path, updated_users):

    """
    turns the updated data into a string and outputs a json file of the
    updated data
    """

    rel_path = os.path.relpath(updated_data_file_path)
    json_string = json.dumps(updated_users)

    try:
        with open(rel_path, 'w', encoding='utf-8') as out_file:
            out_file.write(json_string)
    except IOError as _e:
        logging.error(f'failed to create updated file for {updated_data_file_path}', _e)


def validate_and_clean_data_from_json(file_paths, user_age_limit):

    """
    makes sure the data is the expected shape and matches conditions before being modified
    uses list comprehension for conditionals.
    """

    companies = None

    for file_path in file_paths:
        json_data = get_json_data_from_file(file_path)
        valid_users = [item for item in json_data if is_user(
            item) is True and over_age_limit(item, user_age_limit) is True]
        if companies is None:
            companies = [item for item in json_data if is_company(item) is True]
  
    return valid_users, companies


def main():

    """
    takes a relative paths for config, an age limit to be set and the location 
    of the new output (directory has to exist)

    checks and cleans the relevent data before extending it
    """

    file_paths = ['./assets/company.json', './assets/user.json']
    user_age_limit = 30
    updated_data_file_path = './assets/user_with_company_data.json'

    valid_users, companies = validate_and_clean_data_from_json(file_paths, user_age_limit)

    for user in valid_users:
        add_full_name(user)
        add_related_company(user, companies)

    create_updated_json_file(updated_data_file_path, valid_users)


if __name__ == '__main__':
    main()

import logging
from datetime import date,datetime
from schema import Schema, And, Use, SchemaError


def is_user(item):

    """
    checks item from json data to see if it matches the expected user data shape 
    """
    user_schema = Schema({
        'forename': And(Use(str)),
        'surname': And(Use(str)),
        'date_of_birth': And(Use(str)),
        'location': And(Use(str)),
        'company_id': And(Use(int)),
    })

    try:
        user_schema.validate(item)
        return True
    except SchemaError:
        return False


def is_company(item):

    """
    checks item from json data to see if it matches the expected company data shape 
    """
    company_schema = Schema({
        'id': And(Use(int)),
        'name': And(Use(str)),
        'headquarters': And(Use(str)),
        'industry': And(Use(str)),
    })

    try:
        company_schema.validate(item)
        return True
    except SchemaError:
        return False


def over_age_limit(user, user_age_limit):

    """
    extracts the user's birthday and uses this to calculate the user is over provided age limit
    """

    is_over_age_limit = False

    user_dob_string = user['date_of_birth']
    birth_datetime_object = datetime.strptime(user_dob_string, '%Y/%m/%d')
    today = date.today()
    user_age = today.year - birth_datetime_object.year - ((today.month, today.day) < (birth_datetime_object.month, birth_datetime_object.day))

    if user_age > user_age_limit:
        is_over_age_limit = True

    return is_over_age_limit


def add_full_name(user):

    """
    updates user to have a fullname
    """
    full_name = f'{user["forename"]} {user["surname"]}'
    user.update({'full_name': full_name})


def add_related_company(user, companies):

    """
    by comparing the ids/company ids i then modify the user to include the related company data.
    """

    for company in companies:
        try:
            if company['id'] == user['company_id']:
                user.pop('company_id')
                user['company'] = company
                break
        except Exception as _e:
            logging.error(f'failed to match company data to user {user}', _e)

    return user

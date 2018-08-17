from datetime import datetime
from flask import (
    make_response,
    abort
)


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Data to serve the api
PEOPLE = {
    "Lou": {
        "fname": "Lou",
        "lname": "Ciamp",
        "timestamp": get_timestamp()
    },
    "Hudson": {
        "fname": "Hudson",
        "lname": "Ciamp",
        "timestamp": get_timestamp()
    },
    "Bean": {
        "fname": "Bean",
        "lname": "Ciamp",
        "timestamp": get_timestamp()
    }
}


# create handler for our read (GET) people
def read_all():
    """
    This function responds to a request for /api/people
    with the complete list of people

    :return:    sorted list of people
    """
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]


def create(person):
    """
    This function creates a new perosn in the people data structure
    based on the passed personal data
    :param person:  person to create
    :return:    201 on success, 406 on person exists
    """
    lname = person.get('lname', None)
    fname = person.get('fname', None)

    # Does the person already exsist?
    if fname not in PEOPLE and fname is not None:
        PEOPLE[fname] = {
            "fname": fname,
            "lname": lname,
            "timestamp": get_timestamp()
        }
        return PEOPLE[fname], 201

    else:
        abort(406, 'Person with first name {fname} already exists'.format(fname=fname))

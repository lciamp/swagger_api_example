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


# create handler for our read_all (GET) people
def read_all():
    """
    This function responds to a request for /api/people
    with the complete list of people

    :return:    sorted list of people
    """
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]


# create handler for our create (POST) people
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


# create handler for our read_one (GET) person
def read_one(fname):
    """
    This function responds to a request for /api/people/{fname}
    with one matching person from people
    :param fname: first name of person to find
    :return: person matching first name
    """
    # does the person exsist?
    if fname in PEOPLE:
        person = PEOPLE[fname]
        return person
    else:
        abort(404, 'Person with first name: {fname} not found'.format(fname=fname))


# create handler for our update (PUT) person
def update(fname, person):
    """
    This function updates and exsisting person in the people list
    :param fname: first name of person to update
    :param person: perso to update
    :return: updated person list
    """
    if fname in PEOPLE:
        PEOPLE[fname]['fname'] = person.get('fname')
        PEOPLE[fname]['lname'] = person.get('lname')

        return PEOPLE[fname]
    else:
        abort(404, 'Person with first name: {fname} not found'.format(fname=fname))



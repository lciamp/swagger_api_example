from datetime import datetime


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Data to serve the api
PEOPLE = {
    "lou": {
        "fname": "Lou",
        "lname": "Ciamp",
        "timestamp": get_timestamp()
    },
    "hud": {
        "fname": "Hudson",
        "lname": "Ciamp",
        "timestamp": get_timestamp()
    },
    "bean": {
        "fname": "Bean",
        "lname": "Ciamp",
        "timestamp": get_timestamp()
    }
}


# create handler for our read (GET) people
def read():
    """
    This function responds to a request for /api/people
    with the complete list of people

    :return:    sorted list of people
    """
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]
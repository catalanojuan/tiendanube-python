

class APIError(Exception):

    def __init__(self, message, code):
        Exception.__init__(self, '{}. Status code: {}'.format(message, code))

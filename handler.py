import json
from query import Query

mountains = [
    {
        'name': 'Killington',
        'url': 'https://www.onthesnow.com/vermont/killington-resort/skireport.html'
    },
    {
        'name': 'Hunter',
        'url': 'https://www.onthesnow.com/new-york/hunter-mountain/skireport.html'
    },
    {
        'name': 'Camelback',
        'url': 'https://www.onthesnow.com/pennsylvania/camelback-mountain-resort/skireport.html'
    }
]

def fetch(event, context):
    query = Query()
    result = query.run(mountains)
    response = {
        "statusCode": 200,
        "body": result
    }

    return response

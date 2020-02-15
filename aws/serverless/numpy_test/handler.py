try:
    import unzip_requirements
except ImportError:
    pass
import json
import os
print(os.listdir('.'))
import numpy as np


def hello(event, context):
    print(np.arange(10))

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event,
        "os.listdir('.')": os.listdir('.'),
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

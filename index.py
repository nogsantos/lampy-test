import json


def handler(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


# import numpy as np
# def main(event, context):
#     a = np.arange(15).reshape(3, 5)

#     print("Your numpy array:")
#     print(a)


# if __name__ == "__main__":
#     main('', '')
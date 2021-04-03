import json
from get_features import get_features
from sklearn.covariance import EllipticEnvelope
from sklearn.preprocessing import MinMaxScaler

def lambda_handler(event, context):
    scores = json.dumps(event['body'])
    x = get_features(scores)

    scaler = MinMaxScaler()
    x = scaler.fit_transform(x)
    estimator = EllipticEnvelope()

    estimator.fit(x)

    dist = estimator.dist_
    return {
        'statusCode': 200,
        'body': json.jumps(dist)
    }

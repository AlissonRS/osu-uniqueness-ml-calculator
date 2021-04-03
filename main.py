from load_scores import load_scores
from get_features import get_features
from sklearn.covariance import EllipticEnvelope
from sklearn.preprocessing import MinMaxScaler


scores = load_scores(633993)
x = get_features(scores)

scaler = MinMaxScaler()
x = scaler.fit_transform(x)
estimator = EllipticEnvelope()

estimator.fit(x)

dist = estimator.dist_


print(dist)
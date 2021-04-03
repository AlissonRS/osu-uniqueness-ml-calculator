import urllib.request, json


def load_scores(beatmap):
    url = "https://osu.ppy.sh/api/get_scores?k=6038ce8c694c108929d434f10c45b96a2782e772&b={0}&limit=100".format(beatmap)
    with urllib.request.urlopen(url) as req:
        return list(json.loads(req.read().decode()))

chunk_num = 10

###get toxicity score from Perspective API
from googleapiclient import discovery
import pandas as pd
import time

def get_toxicity_score(comment):
    # print(comment)
    analyze_request = {
      'comment': { 'text': comment},
    #  'comment': { 'text': 'friendly greetings from python'},
      'requestedAttributes': {'TOXICITY': {}}
    }

    response = service.comments().analyze(body=analyze_request).execute()
    toxicity_score = response['attributeScores']['TOXICITY']['summaryScore']['value']
    return toxicity_score

###main()
# Generates Perspective API client object dynamically based on service name and version.
API_KEY = pd.read_csv('perspective-api-keys.txt', names = ['key'])['key'][chunk_num]
service = discovery.build('commentanalyzer', 'v1alpha1', developerKey=API_KEY)
filename = "subdf-" + str(chunk_num)

# tf = tf[(tf.body != '[deleted]') & (tf.body != '[removed]')]
count = 0
toxicity_scores = []

tf = pd.read_csv(filename + ".csv")
print(chunk_num, filename, tf.shape[0])

for comment in tf.body:
    print(count)
    count += 1
    if ((comment == "[deleted]") | (comment == "[removed]")):
        score = -1.0
        toxicity_scores.append(score)
    else:
        try:
            score = get_toxicity_score(comment)
            toxicity_scores.append(score)
            time.sleep(1)      ###rate limit: 1 request per second
        except:
            score = -1.0
            toxicity_scores.append(score)

tf['toxicity'] = toxicity_scores
tf.to_csv(filename + "-toxicity.csv", index = False)

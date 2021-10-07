# quarantined-subreddits
Analysis of quarantined subreddits

We first created the notebook 'collectTRPUsers'. This notebook looks at all the comments and submissions submitted by users in TRP in the period of exactly six months before to exactly six months after the quarantine. It then selects users who posted at least 2 and at most 10,000 posts in TRP before the quarantine, and store them to a file, which will be later used for data collection outside TRP. This notebook also tests Hypothesis 1, and finds that the pre-quarantine activity of departed users is significantly higher than the pre-quarantine activity of non-departed users, thereby rejecting Hypothesis 1. However, when comparing the total posts, Hypothesis 1 is not rejected.

Next, we collected the Reddit-wide activity (submissions as well as comments) for all users who posted (submitted or commented) on TRP before the quarantine.

Following this, in 'getCandidateControlSubreddits', we collected a candidate set of subreddits that could be control subreddits.
For each subreddit, we calculated how many TRP users posted (submitted or commented) on that subreddit at least five times before the quarantine, calling them active users. Next, we sorted these subreddits based on the number of active TRP users on them, and collected 1000 subreddits with the highest number of active TRP users for further inspection.

Next, for each of these 1000 subreddits, we calculated the number of unique users who posted (submitted or commented) in them in the six months prior to the quarantine, again using Google BigQuery.

In 'getControlSubreddits', we calculate the ratio (# of TRP users)/(# of unique users) for each of the 1000 candidate control subreddits, and sort subreddits based on this ratio in a descending order. We manually review the top subreddits in order to verify that (1) they are not quarantined and (2) they are appropriate to be considered a control subreddit.

In 'whereDoOldTimersGo', we calculate the number of posts made by pre-quarantined TRP users across all Reddit before and after the quarantine, and for each subreddit where users posted before as well as after the quarantine, we calculate the ratio of 
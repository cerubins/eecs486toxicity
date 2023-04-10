import glob

# iterates through all subreddit BERT predictions
toxicScores = dict()
for file in glob.glob('output/*'):
    with open(file) as f:
        subreddit = file.lstrip('output/')
        lines = file.readlines()

        # counts number of "toxic" labeled comments in identifier
        lineCount = 0
        toxicCount = 0
        for line in lines:
            lineCount += 1
            if lineCount % 2 == 1 and line == 'Toxic':
                toxicCount += 1

        toxicScores[subreddit] = toxicCount/len(lines)

# outputs subreddits sorted by toxicity percentage
sortedScores = sorted(toxicScores)
print(sortedScores)

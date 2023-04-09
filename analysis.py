import glob

toxicScores = dict()
for file in glob.glob('output/*'):
    with open(file) as f:
        subreddit = file.lstrip('output/')
        lines = file.readlines()

        toxicCount = 0
        for line in lines:
            words = line.split()
            if words[-1] == 'Toxic':
                toxicCount += 1

        toxicScores[subreddit] = toxicCount/len(lines)

sortedScores = sorted(toxicScores)
print(sortedScores)

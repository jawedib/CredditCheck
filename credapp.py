import praw
#import time
from statistics import mean
from credentials import reddit


def creditCheck(name):
    redditor = reddit.redditor(name)
    comments = redditor.comments.new(limit=60)
    scores = []

    try:
        for comment in comments:
            
            parent = comment.parent()
            parentscore = parent.score
            
            if (parentscore>0):
                if (parent.author != redditor): #if statement checks if person is replying to own post 
                   myscore = comment.score
                   scores.append(myscore/parentscore)
    
    
        if (len(scores)>45): #len() is O(1), so why not. Adds credibility(ayy!) to the tool itself
           final = str(round(mean(scores)*1000))
           #print("Your score : " + final) # multiplying score by 1000 to have a whole number
    
        else:
            final="Account does not have enough comments/information"
    
        dict = {'final': final, 'name': name}
    	
    except:
        return {'final': "No account/comments found", 'name': name}
    
    return (dict)
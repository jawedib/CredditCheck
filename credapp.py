import praw
#import time
from statistics import mean
from credentials import reddit


def creditCheck(name):
    redditor = reddit.redditor(name)
    comments = redditor.comments.new(limit=50)
    scores = []

    try:
        for comment in comments:
            
            parent = comment.parent()
            parentscore = parent.score
            
            if (parentscore>0):
                if (parent.author != redditor): #if statement checks if person is replying to own post 
                   myscore = comment.score
                   scores.append(myscore/parentscore)
    
    
        if (len(scores)>35): #len() is O(1), so why not. Adds credibility(ayy!) to the tool itself
           finalscore = round(mean(scores)*10)
           # multiplying score by 10 to have a whole number
    
        else:
            return {'finalscore': "Account does not have enough comments/information", 'name': name, 'grade': "N/A"}
    
        grade = getGrade(int(finalscore))
        dict = {'finalscore': finalscore, 'name': name, 'grade': grade}
    	
    except:
        return {'finalscore': "No account/comments found", 'name': name, 'grade': "N/A"}
    
    return (dict)

def getGrade(score):
    try:
        if (score>=4 and score<8):
            return "C"
        elif (score>=0 and score<4):
            return "D"
        elif (score>=8 and score<12):
            return "B"
        elif (score>=12 and score<16):
            return "A"
        elif (score>=16):
            return "A+"
        elif (score>=-4 and score<0):
            return "F"
        elif (score<-4):
            return "Delete Account."
    except:
        return "No grade available."
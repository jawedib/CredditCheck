# CredditCheck

Currently live at: https://credditcheck.herokuapp.com/

Reddit user credibility checker. Web app version of my Reddit bot. Personal project to get familiar with Django, Bootstrap and Jinja. 
Purpose of the bot is to gauge the credibility of a user without having to go through their account history. Your questions on subreddits such as r/LearnProgramming or r/HomeworkHelp might not necessarily gain any traction or votes. At best you might have 3 to 4 comments with one vote each and each reply's solution might be heading in a different direction. CredditCheck can help here to see which user has historically provided popular answers and help you reach the best solution. Higher karma points on an account does not necessarily garner high grades on CredditCheck; users who merely respond in small subreddits may receive excellent grades on the app.

Obviously, it's Reddit, it’s user-voted and more about overall agreeability and not actual credibility but CredditCheck is a much cooler name. 

This tool can also used by marketers who buy Reddit accounts to promote their products as a message holds more weight coming from a trusted account. Another example of usage that doesn't involve buying accounts would be: a brand looking to hire a celebrity for endorsement, may use this tool and decide to approach Neil Degrasse Tyson instead of Bill Nye to promote their product on Reddit. The grades of both of these science-celebs as of 14 Jan 2019 are:

•	Neil Tyson(Reddit username: neiltyson) : A+

•	Bill Nye(Reddit username: sundialbill) : B

If I had to guess beforehand, I would guess the Neil Degrasse Tyson's grade to be much lower as Bill Nye seemingly has been the overall better liked celebrity at Reddit. It was just lately his account has been subject to negative responses by Reddit users due to several reasons explained here by other users(may contain foul language):
https://www.reddit.com/r/OutOfTheLoop/comments/7bqfhm/why_is_bill_nyes_ama_so_heavily_downvoted/

As a marketer, I could skip all of this research by simply using CredditCheck!



Sidenote: I was looking to move from PRAW API to PushShift for quicker, more consistent results but apparently they might not be around for much longer so we'll stay with PRAW for now. Source: https://www.reddit.com/r/pushshift/comments/ad1kz9/thanks_to_all_who_donated_the_minimum_needed_has/

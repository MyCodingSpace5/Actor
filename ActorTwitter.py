#Actor: Acting like a human Creates fake people based on human nature!
import time

import openai
import os
import tweepy
import imagegeneration
openai.organization = ""
openai.api_key = ""
import random
import queue


def GenerateActor(twitterApiKey,openaiApiKey,twitterSecret,twitterAcessToken,twitterAccessTokenSecret,motive):
    auth = tweepy.OAuth1UserHandler(twitterApiKey, twitterSecret, twitterAcessToken, twitterAccessTokenSecret)
    api = tweepy.API(auth)
    dms = api.direct_messages()
    conversations = {}
    APIKey = twitterApiKey
    name = random.randint(0,7)
    personality2 = random.randint(0,6)
    gender = ["M","F","F","M","M","M","F","F","F"]
    personality = ["Dickhead","Attention Seekeing","Greedy","Shady","Entitled","Power hungry","Narrasistic","Kind","Caring","Guilable"]
    poiticalviews = ["Republican","Democrat","Socalist","Enviormentalists","Libeterain","Communist","Syndcalist","Centrist","Liberal"]
    poiticalviewspicker = random.randint(0,8)
    selectedpolticalview = poiticalviews[poiticalviewspicker]
    DMList = [""]
    storedgender = gender[name]
    storedpersonality = personality[personality2]
    if(storedgender == "M"):
        openai.api_key = openaiApiKey
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt="Generate a random boy's first name and last name",
            temperature=1,
            max_tokens=60,
            top_p=1,
            frequency_penalty=0.5,
            presence_penalty=0
        )
        text = response["choices"][0]["text"]
        profilePicture = imagegeneration.imageGenerationMale()
    else:
        openai.api_key = openaiApiKey
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt="Generate a random girl's first name & last name",
            temperature=1,
            max_tokens=60,
            top_p=1,
            frequency_penalty=0.5,
            presence_penalty=0
        )
        text = response["choices"][0]["text"]
        profilePicture = imagegeneration.imageGenerationFemale()
    for dm in dms:
        q = queue.Queue()
        q.put(dm.text)
        if sender not in conversations:
            conversations[sender] = []
        queueLength = len(q)
        sender = dm.sender.screen_name
        sendername = dm.sender.name
        openai.api_key = openaiApiKey
    if(queueLength < 250):
        for i in range(queueLength):
            dmnow = q.get()
            conversations[sender].append(dmnow)
            response = openai.Completion.create(
                model="text-davinci-002",
                prompt=f"Generate a response to this:{dmnow} in a {storedpersonality} way. And also their name is {sendername}  And also when generating your response remember the previous conversations {conversations[sender]} For this response your motive is to {motive}",
                temperature=1,
                max_tokens=1024,
                top_p=1,
                frequency_penalty=0.5,
                presence_penalty=0
            )
            ResponseToDM = response["choices"][0]["text"]
            api.new_direct_message(user=sender, text=ResponseToDM)
    else:
        api.new_direct_message(user=sender, text="The Actor Chatbot is exprencing diffucultes keeping up! Please wait")

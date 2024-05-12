
vowel = ["A","E","I","O","U","a","e","i","o","u"]

tweet = input("Input: ")

for i in vowel:
    if i in tweet:
        tweet = tweet.replace(i,"")

print(tweet)

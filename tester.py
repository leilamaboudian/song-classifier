from textblob import TextBlob

t = '''Girl, I been thinkin' 'bout us
And you know I ain't good at this stuff
But these feelings pilin' up won't give me no rest
This might come out a little crazy
A little sideways, yeah maybe
I don't know how long it'll take me
But I'll do my best
You'll be my soft and sweet
I'll be your strong and steady
You'll be my glass of wine
I'll be your shot of whiskey
You'll be my sunny day
I'll be your shade tree
You'll be my honeysuckle
I'll be your honey bee
Yeah, that came out a little country
But every word was right on the money
And I got you smilin' honey right back at me
Now hold on 'cause I ain't done
There's more where that came from
Well you know I'm just havin' fun, but seriously
If you'll be my Louisiana
I'll be your Mississippi
You'll be my Little Loretta
I'll be your Conway Twitty
You'll be my sugar, baby
I'll be your sweet iced tea
You'll be my honeysuckle
I'll be your honey bee
Your kiss just said it all
I'm glad we had this talk
Nothing left to do
But fall in each others arms
I coulda said I love you
Coulda wrote you a line or two
Baby, all I know to do
Is speak right from the heart
If you'll be my soft and sweet
I'll be your strong and steady
You'll be my glass of wine
I'll be your shot of whiskey
You'll be my sunny day
I'll be your shade tree
You'll be my honeysuckle
I'll be your honey bee
You'll be my Louisiana
I'll be your Mississippi
You'll be my Little Loretta
I'll be your Conway Twitty
You'll be my sugar baby
I'll be your sweet iced tea
You'll be my honeysuckle
And I'll be your honey bee
I'll be your honey bee'''

t = TextBlob(t)

print(t.sentiment)
print(t.polarity)
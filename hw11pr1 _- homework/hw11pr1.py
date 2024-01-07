# coding: utf-8
#
# The top line, above, is important -- it ensures that Python will be
# able to use this file even if you paste in text with fancy Unicode
# characters that aren't part of normal ASCII.
#
# For another example of such a file, see
# https://www.cl.cam.ac.uk/~mgk25/ucs/examples/UTF-8-demo.txt
#
# OK! Now we're ready for hw10pr3.py ...
#
# Name: Leila Maboudian
#


import random  


#
# First, some helper/example functions for files + text ...
#
# To make the examples work, you should have the text file named "a.txt"
# in the same directory as this .py file!
#
# If you _don't_ have "a.txt", create it.  Here are its contents:
"""
I like poptarts and 42 and spam.
Will I get spam and poptarts for
the holidays? I like spam poptarts!
"""


def get_text(filename):
    """Opens a file named 'filename', reads
       it, and returns its contents (as one big string).

       Example:
          In [1]: get_text("a.txt")
          Out[1]: 'I like poptarts and 42 and spam.\nWill I get spam and poptarts for\nthe holidays? I like spam poptarts!\n\n\n\n'

          In [1]: len(get_text("a.txt"))
          Out[1]: 102  # Well, _around_ 102, depending how many \n's you have at the end of a.txt.
                       # Note that '\n' is ONE character:   len('\n') == 1
    """
    #
    # First we have to open the file (just like opening a book to read it).
    # We assume the "utf-8" encoding, which accepts more characters than plain ASCII
    #
    # Other common codings welcome, e.g., utf-16 or latin1
    # See [docs.python.org/3.8/library/codecs.html#standard-encodings]
    # for the full list (it's big!).
    #
    f = open(filename, encoding = 'utf-8')

    #
    # Read the contents of the file into a string named "text", close
    # the file, and return the string.
    #
    text = f.read()
    f.close()
    return text

def word_count(text):
    """Word-counting function.
       Counts the number of "words" (space-separated sequences) in
       the string "text".

       Examples:
          In [1]: word_count('This has four words!')
          Out[1]: 4

          In [1]: word_count(get_text("a.txt"))
          Out[1]: 20                 # If it's the a.txt file above
    """
    #
    # The text of the file is one long string.  Use "split" to get words!
    #
    LoW = text.split()    # We could use text.split("\n") to get _lines_.

    #
    # LoW is a List of Words, so its length is the word count.
    #
    result = len(LoW)

    # Comment out, as needed...
    if result < 100:
        print("LoW[0:result] is", LoW[0:result])  # For sanity checking...
    else:
        print("LoW[0:100] is", LoW[0:100])        # without going too far...

    return result



# Use the string library to implement remove_punctuation:
import string    # See https://docs.python.org/3/library/string.html
                 # Note: str is different: docs.python.org/3/library/stdtypes.html#textseq

def remove_punctuation(text):
    """Accepts a string named "text".  Returns an equivalent string, _but_
       with all non-(English)-text characters removed (keeps only
       letters + digits).

       + Vary to suit the language at hand!

       Examples:
          In [1]: remove_punctuation("42_isn't_.!?41.9bar")
          Out[1]: '42isnt419bar'

          In [2]: remove_punctuation(get_text("a.txt"))
          Out[2]: 'Ilikepoptartsand42andspamWillIgetspamandpoptartsfortheholidaysIlikespampoptarts' # (Not so useful w/o spaces!)
    """
    new_text = ''
    CHARS_TO_KEEP = string.ascii_letters + string.digits # + string.whitespace + string.punctuation
    for c in text:  # c is each character
        # Use the Python string library
        if c in CHARS_TO_KEEP:
            new_text += c
        else:
            pass # don't include it  [WARNING: as written, this removes spaces!]

    # We're finished!
    return new_text


def vocab_count(text):
    """Returns a dictionary of (punctuationless, lower-cased) words in "text".

       + Removes everything not in string.ascii_letters (via the function
         above).
       + Also, lower-cases everything (alter to suit your taste or
         application!).
       + Builds and returns a dictionary of how many times each word occurs.

       Examples:
          In [1]: vocab_count("Spam, spam, I love spam!")
          There are 5 words.
          There are 3 *distinct* words in the text.

          Out[1]: {'spam': 3, 'i': 1, 'love': 1}


          In [2]: vocab_count(get_text("a.txt"))
          There are 20 words.
          There are 11 *distinct* words in the text.

          Out[2]:
                    {'i': 3,
                    'like': 2,
                    'poptarts': 3,
                    'and': 3,
                    '42': 1,
                    'spam': 3,
                    'will': 1,
                    'get': 1,
                    'for': 1,
                    'the': 1,
                    'holidays': 1}
    """
    LoW = text.split()
    print("There are", len(LoW), "words.")  # For info - comment out if you like

    d = {}
    for word in LoW:
        word = remove_punctuation(word)  # Remove punctuation!
        word = word.lower()   # Make lower case!

        if word not in d:     # If it's not already in the dictionary, d
            d[word] = 1       # Set count to 1  (the VALUE is the count, here)
        else:                 # ..or if it IS already in the dictionary, d
            d[word] += 1      # ..add 1 to count (again, the VALUE is the count)

    print("There are", len(d), "*distinct* words in the text.\n")
    return d            # This way we can _use_ or look up the keys in d...




"""

[a] What was in the file you analyzed?
    --> I populated a.txt with the first 6 stanzas of
        "We Didn't Start the Fire" by Billy Joel.

[b] How many words did it have?
    --> It had 164 words.

[c] How many characters did it have?
    --> It had 1040 chars.

[d] How many _distinct_ words did it have?
    --> It had 109 distinct words.

[e] What are words that appeared unusually often for this text?
    --> "the", "we", "didn't", and "it" appeared most often
        but this is npt unusual since they are in the chorus.

[f] Other thoughts/insights?!
    --> Will be interesting to see this at work with other texts since
        this song in particular has a very stark distinction in the
        incidence of words in the chorus and the incidence of words
        in the rest of the song (those tend to appear only 1x or 2x)...

"""

#
# Now, to the Markov modeling (createDictionary) and Markov text
# generation (generateText)
#
# Be sure to create your 500-word "CS-Essay,"" with:
#    In [1]: d = createDictionary(get_text("yourfile.txt"))
#    In [2]: generateText(d, 500)       # Then copy the "essay" below ...
#


# Function #1 (createDictionary)
# returns result
def createDictionary(text):
    """ Return: createDictionary returns a dictionary whose keys are words encountered in text
        and whose entries are a list of words that may legally follow the key word.
        Argument text: a string.
    """
    d = {}
    prev = '$'
    LoW = text.split()

    for word in LoW:
        if prev not in d:
            d[prev] = [word]
        else:
            d[prev] += [word]
        prev = word
        if prev[-1] in '.!?':
            prev = '$'
    
    return d



# Function #2   (generateText)
# prints result
# "generateText(d, n) will accept a dictionary of word transitions d (generated in your createDictionary function, above) and a positive integer, n. 
# Then, generateText should print a string of n words."
def generateText(d, N):
    
    """ generateText takes a dictionary of word transitions d and a positive int n.
        It then prints a string of n words.
        Argument d: a dictionary.
        Argument N: an int.
    """
    
    print()  # start by printing a newline
    
    item = random.choice(d['$'])
    print(item, end = ' ')

    i = 1
    
    while i < N:
        next_word = random.choice(d[item])  # Next word -- will be replaced (alas)
        # Here's how to print so that things don't always start on the next line
        # Using end = ' ' stops it going to the next line
        print(next_word, end = ' ')
        item = next_word
        if i < N and next_word[-1] in '.!?' or d.get(item) == False:
            item = '$'
        i += 1
        
    print()                  # Final print, newline



# Function #2   (generateText 2.0)
# also made a generateText2 that returns the Markov Model rather than printing it.
def generateText2(d, N):
    
    """ Return: generateText takes a dictionary of word transitions d and a positive int n
        and returns a string of n words.
        Argument d: a dictionary.
        Argument N: an int.
    """
    
    model = ""
    
    item = random.choice(d['$'])
    model += item + ' '

    i = 1
    
    while i < N:
        next_word = random.choice(d[item])  # Next word -- will be replaced (alas)
        # Here's how to print so that things don't always start on the next line
        # Using end = ' ' stops it going to the next line
        model += next_word + ' '
        item = next_word
        if i < N and next_word[-1] in '.!?' or d.get(item) == False:
            item = '$'
        i += 1
    
    return model



# Your 500-or-so-word "CS Essay" (paste into the triple-quoted strings below):

"""

SOURCE >>>
The House on Mango Street, Chapter 1 (Sandra Cisneros)

BEST LINES >>>
"I had been robbed two buildings on T.V."  # This almost sounds reasonable!
"Everybody has to anybody, or share a house, a basement and before we would be one washroom."  # This one feels prophetic?
"And inside it would have real house. Out back is a real house."  # Interesting -- the two sentences are sort of a paradox!
"Out back is ours, and Kiki, my sister "  # Cliffhanger ending!

GENERATED TEXT >>>
In [100]: generateText(dict, 500)
"And our house on the two days before we wouldn't fix them because it made me feel like the time we wouldn't fall out.
But the people downstairs, or share a house, a great big yard that we got to have a fence. I had been robbed two buildings on T.V.
Out back is ours, and at least three washrooms so swollen you have to look to have a real house. I remember most is not the house Papa talked about when he held a fence.
There. By the house on Loomis on the curb. That's why we would be white with the landlord wouldn't have to look to bed.
Once when we where living on the third floor, and before and red with the two days before and there isn't a house, a lot.
That's why we were six—Mama, Papa, Carlos and the time it would have to pay rent to pay rent to pay rent to where living on Mango Street is not hallway stairs, 
but they're ordinary hallway stairs, and the third floor, the ceiling with the flat on Mango Street we wouldn't have to anybody, or be white with the other side of town. And we'd get.
Everybody has to anybody, or share a house, a basement and before we would be one washroom. She asked. And inside it would have real house. Out back is a real house. And we'd get.
They always live there? It's small garage for the house has only one day we don't have a house, but stairs in the ceiling with the house would move into a nun from my school passed by the other side of us.
I knew then I knew then I lived on the city planted by the third floor, and we wouldn't fix them because the yard with a broom. Once when we wouldn't have a fence. I could point to. You live there?
There are crumbling in our house, but they're ordinary hallway stairs, and Papa, Carlos, Kiki, me and the house has only four little elms the third floor, the third floor, the house on the third floor.
We didn't always told it would move into a bedroom—Mama and at all. One I said it made me playing out front. But this was too old. She asked. I can't remember.
But even so, it's not the third floor, the house Papa had to leave the ceiling with the way she said pointing up in the people downstairs,
or share a small and before we don't own yet and Papa, Carlos and window so we got to have a bedroom—Mama and before that we were six—Mama, Papa, Carlos, Kiki, my sister Nenny
and before that we would be white with trees around it, a great big yard with tight steps in our house on Mango Street isn't it. By the house on T.V. We didn't always live there?
By the way they told us that worked. Out back is ours, and Kiki, my sister "

"""

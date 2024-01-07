#
# final.py
#
# TextModel project!
#
# Name: Leila Maboudian
#




import math
import string
from xml.etree.ElementTree import TreeBuilder
from textblob import TextBlob




class TextModel:
    

    """A class supporting complex models of text."""


    def __init__(self):
        """Create an empty TextModel."""
        # 
        # The text in the model, all in a single string--the original
        # and "cleaned" versions.
        #
        self.text = ''                  # No text present yet
        self.cleanedtext = ''           # Nor any cleaned text yet
                                        # ..(cleaned == only letters, all lowercase)

        #
        # Create dictionaries for each characteristic
        #
        self.words = {}                   # For counting words
        self.wordlengths = {}             # For counting word lengths
        self.stems = {}                   # For counting stems
        self.sentencelengths = {}         # For counting sentence lengths
        
        # Create another dictionary of your own
        #
        self.sentencepolarities = {}      # For counting ___________
        self.sentencesubjectivities = {}  # For counting ___________


    def __repr__(self):
        """Display the contents of a TextModel."""
        s = f'Words:\n{str(self.words)}\n\n'
        s += f'Word lengths:\n{str(self.wordlengths)}\n\n'
        s += f'Stems:\n{str(self.stems)}\n\n'
        s += f'Sentence lengths:\n{str(self.sentencelengths)}\n\n'
        s += f'MY PARAMETERS (Polarity and Subjectivity):\n{str(self.sentencepolarities)}, {str(self.sentencesubjectivities)}\n\n'
        s += '+'*55 + '\n'
        s += f'\nText[:42]    {self.text[:42]}\n\n'
        s += f'Cleaned[:42] {self.cleanedtext[:42]}\n'
        s += '+'*55 + '\n\n'
        return s


    # We provide two text-adding methods (functions) here:
    def addRawText(self, text):
        """addRawText accepts self (the object itself)
                      and text, a string of raw text to add.
           Nothing is returned from this method, but
           the text _is_ added.
        """
        self.text += text 
        self.cleanedtext += self.cleanString(self.text) 


    # The second one adds text from a file:
    def addFileText(self, filename):
        """addFileText accepts a filename.
            
           Nothing is returned from this method, but
           the file is opened and its text _is_ added.

           If the file is not present, it will crash!
        """
        f = open(filename, 'r', encoding='latin1')
                               # The above may need utf-8 or utf-16, depending
        text = f.read()        # Read all of the contents into text 
        f.close()              # Close the file
        self.addRawText(text)  # Uses the previous method!


    def makeSentenceLengths(self):
        
        """ Creates the dictionary of sentence lengths
               should use self.text, because it needs the punctuation!
        """
        
        LoW = self.text.split()
        
        words = 0
        
        for word in LoW:
            words += 1
            if word[-1] in '.!?':
                if words not in self.sentencelengths:
                    self.sentencelengths[words] = 1  # if new key (sentence length) in dictionary, value of 1
                else:
                    self.sentencelengths[words] += 1  # if existing key (sentence length) in dictionary, value increases by 1
                words = 0


    def makeWordLengths(self):
        
        """ Creates the dictionary of words lengths
               should use self.cleanedtext!
        """
        
        LoW = self.cleanedtext.split()
        
        for word in LoW:
            if len(word) not in self.wordlengths:
                self.wordlengths[len(word)] = 1  # if new key (word length) in dictionary, value of 1
            else:
                self.wordlengths[len(word)] += 1  # if existing key (word length) in dictionary, value increases by 1


    def makeWords(self):
        
        """ Creates the dictionary of words
               uses self.cleanedtext!
        """

        LoW = self.cleanedtext.split()

        for word in LoW:
            if word not in self.words:
                self.words[word] = 1  # if new key (word) in dictionary, value of 1
            else:
                self.words[word] += 1  # if existing key (word) in dictionary, value increases by 1


    def makeStems(self):
        
        """ Makes a dictionary of the *clean* stems of the words.
            Rules:
            -  if ends with 'ss':
               -  do not remove last 's'
            -  elif ends with 'sses':
               -  remove last 'es'
            -  elif ends with 's':
               -  remove last 's'
            -  if ends with 'ious':
               -  remove last 'ious':
            -  elif ends with 'ous':
               -  remove last 'ous'
            -  if ends with 'ed':
               -  remove last 'ed'
            -  if ends with 'ing':
               -  remove last 'ing'
            -  if ends with 'tion':
               -  remove last 'tion'
            -  if ends with 'er':
               -  remove last 'er'
            -  if ends with 'est':
               -  remove last 'est'
        """
        
        LoW = self.cleanedtext.split()

        for word in LoW:
            if len(word) > 3:
                if word[-2:] == 'ss':
                    word = word
                elif word[-4:] == 'sses':
                    word = word[:-2]
                elif word[-1] == 's':
                    word = word[:-1]
                if word[-4:] == 'ious':
                    word = word[:-4]
                elif word[-3:] == 'ous':
                    word = word[:-3]
                if word[-2:] == 'ed':
                    word = word[:-2]
                if word[-3:] == 'ing':
                    word = word[:-3]
                if word[-4:] == 'tion':
                    word = word[:-4]
                if word[-2:] == 'er':
                    word = word[:-2]
                if word[-3:] == 'est':
                    word = word[:-3]
            else:
                word = word
            if word not in self.stems:
                self.stems[word] = 1
            else:
                self.stems[word] += 1


    def subPolClassifier(self):

        """ Determines the sentence polarity/subjectivity distribution of a text.
            Polarity is on a scale of -1 (negative statement) to 1 (positive statement).
            Subjectivity is on a scale of 0 (objective statement) to 1 (subjective statement).
        """

        LoW = self.text.split()
        
        sentence = ''
        pol = TextBlob(sentence).polarity
        sub = TextBlob(sentence).subjectivity

        for word in LoW:  # go through all words
            sentence += ' ' + word  # create sentences
            if len(word) > 1 and word[-1] in '.!?':  # end of sentence
                pol = round(TextBlob(sentence).polarity, 1)  # sentence polarity
                if pol not in self.sentencepolarities:  # new polarity key
                    self.sentencepolarities[pol] = 1  # give it a value of 1, representing the number of sentences with this polarity
                else:  # existing polarity key
                    self.sentencepolarities[pol] += 1  # add 1, representing the number of sentences with this polarity
                sub = round(TextBlob(sentence).subjectivity, 1)  # sentence subjectivity
                if sub not in self.sentencesubjectivities:  # new subjectivity key
                    self.sentencesubjectivities[sub] = 1  # give it a value of 1, representing the number of sentences with this subjectivity
                else:  # existing subjectivity key
                    self.sentencesubjectivities[sub] += 1  # add 1, representing the number of sentences with this subjectivity
                sentence = sentence[0]  # clear sentence to read and classify the next one


    def normalizeDictionary(self, d):
        
        """ Returns a dictionary where the values are in the same ratio as in d,
            but they add up to 1.
        """
        
        # sums all of d's values (will be the denominator)
        total = sum(d.values())
        
        # initialize new
        newd = {}
        
        # divide each value in d by the sum of all values
        # put each new key-value pair into newd
        for k in d:
            newd[k] = d[k]/total
        
        # return normalized dictionary
        return newd

    def smallestValue(self, nd1, nd2):
        
        """ Returns the smallest (normalized) value across both dictionaries (nd1, nd2).
        """
        
        nd1 = self.normalizeDictionary(nd1)
        nd2 = self.normalizeDictionary(nd2)

        # initialize min
        min = 0
        for k in nd1:
            min = nd1[k]

        # search for val in nd1 that is less than min
        # if exists, make it new min
        for k in nd1:
            if nd1[k] < min:
                min = nd1[k]

        # search for val in nd2 that is less than min
        # if exists, make it new min
        for k in nd2:
            if nd2[k] < min:
                min = nd2[k]
        
        # return minimum
        return min
    

    def compareDictionaries(self, d, nd1, nd2):
        
        """ compareDictionaries calculates:
            The log-probability that dictionary d arose from the distribution of data in normalized dictionary nd1,
            and:
            The log-probability that dictionary d arose from the distribution of data in normalized dictionary nd2.
            It returns these log probabilities in a list
        """

        # make sure 1 and 2 are normalized
        nd1 = self.normalizeDictionary(nd1)
        nd2 = self.normalizeDictionary(nd2)
        
        # half of the smallest value as a filler value
        epsilon = (self.smallestValue(nd1, nd2))/2

        # initialize their log probabilities
        logprob1 = 0.0
        logprob2 = 0.0
        
        # initialize return list
        logprobs = []

        # check for keys in d in nd1, nd2
        # add log probabilities to the logprob variables
        # these depend on values in d and (if k in nd1/nd2) the logs of the values in nd1/nd2 or (if k not in nd1/nd2) variable epsilon
        for k in d:
            if k in nd1:
                logprob1 += (d[k])*(math.log(nd1[k]))
            elif k not in nd1:
                logprob1 += (d[k])*(math.log(epsilon))
            if k in nd2:
                logprob2 += (d[k])*(math.log(nd2[k]))
            elif k not in nd2:
                logprob2 += (d[k])*(math.log(epsilon))
        
        # fill list
        logprobs += [logprob1]
        logprobs += [logprob2]
        
        # return it
        return logprobs


    def createAllDictionaries(self):
        
        """ Create out all five of self's
            dictionaries in full.
        """

        self.makeSentenceLengths()
        self.makeWords()
        self.makeStems()
        self.makeWordLengths()
        self.subPolClassifier()


    def compareTextWithTwoModels(self, model1, model2):
        
        """ Runs compareDictionaries for each of the feature dictionaries in self against
            the corresponding normalized dictionaries in model1 and model2. 
            No return.
        """

        # compatibility is scored with a weighted standard
        # because this handles songs, sentence lengths are not a strong indicator of similarity
        # however, subjectivity and polarity are, as different genres of music can have very distinctive sentiments (patterns)
        # features is the number of aspects where model1 wins; score1 is 1's weighted score; score2 is 2's weighted score
        features = 0
        score1 = 0
        score2 = 0

        print(f"     {'Self':>28s}   {'vsTM1':>10s}   {'vsTM2':>10s} ")
        print(f"     {'----':>28s}   {'-----':>10s}   {'-----':>10s} ")

        # log probabilities (parameter: words)
        nd1Words = self.normalizeDictionary(model1.words)
        nd2Words = self.normalizeDictionary(model2.words)
        logProbsWords = self.compareDictionaries(self.words, nd1Words, nd2Words)
        d_name = 'Words'
        print(f"     {d_name:>28s}   {logProbsWords[0]:>10.2f}   {logProbsWords[1]:>10.2f} ")

        # words parameter - increase winning model's score by 2
        if logProbsWords[0] > logProbsWords[1]:
            features += 1
            score1 += 2
        elif logProbsWords[0] < logProbsWords[1]:
            score2 += 2

        # log probabilities (parameter: stems)
        nd1Stems = self.normalizeDictionary(model1.stems)
        nd2Stems = self.normalizeDictionary(model2.stems)
        logProbsStems = self.compareDictionaries(self.stems, nd1Stems, nd2Stems)
        d_name = 'Stems'
        print(f"     {d_name:>28s}   {logProbsStems[0]:>10.2f}   {logProbsStems[1]:>10.2f} ")

        # stems parameter - increase winning model's score by 2
        if logProbsStems[0] > logProbsStems[1]:
            features += 1
            score1 += 2
        elif logProbsStems[0] < logProbsStems[1]:
            score2 += 2

        # log probabilities (parameter: word lengths)
        nd1WLengths = self.normalizeDictionary(model1.wordlengths)
        nd2WLengths = self.normalizeDictionary(model2.wordlengths)
        logProbsWordLengths = self.compareDictionaries(self.wordlengths, nd1WLengths, nd2WLengths)
        d_name = 'Word Lengths'
        print(f"     {d_name:>28s}   {logProbsWordLengths[0]:>10.2f}   {logProbsWordLengths[1]:>10.2f} ")

        # word lengths parameter - increase winning model's score by 2
        if logProbsWordLengths[0] > logProbsWordLengths[1]:
            features += 1
            score1 += 2
        elif logProbsWordLengths[0] < logProbsWordLengths[1]:
            score2 += 2

        # log probabilities (parameter: sentence lengths)
        nd1SLengths = self.normalizeDictionary(model1.sentencelengths)
        nd2SLengths = self.normalizeDictionary(model2.sentencelengths)
        logProbsSentLengths = self.compareDictionaries(self.sentencelengths, nd1SLengths, nd2SLengths)
        d_name = 'Sentence Lengths'
        print(f"     {d_name:>28s}   {logProbsSentLengths[0]:>10.2f}   {logProbsSentLengths[1]:>10.2f} ")

        # sentence lengths parameter - increase winning model's score by 1
        if logProbsSentLengths[0] > logProbsSentLengths[1]:
            features += 1
            score1 += 1
        elif logProbsSentLengths[0] < logProbsSentLengths[1]:
            score2 += 1

        # log probabilities (parameter: subjectivities)
        nd1Subs = self.normalizeDictionary(model1.sentencesubjectivities)
        nd2Subs = self.normalizeDictionary(model2.sentencesubjectivities)
        logProbsSubs = self.compareDictionaries(self.sentencesubjectivities, nd1Subs, nd2Subs)
        d_name = 'Sentence Subjectivities'
        print(f"     {d_name:>28s}   {logProbsSubs[0]:>10.2f}   {logProbsSubs[1]:>10.2f} ")

        # sentence subjectivities parameter - increase winning model's score by 4
        if logProbsSubs[0] > logProbsSubs[1]:
            features += 1
            score1 += 4
        elif logProbsSubs[0] < logProbsSubs[1]:
            score2 += 4

        # log probabilities (parameter: polarities)
        nd1Pols = self.normalizeDictionary(model1.sentencepolarities)
        nd2Pols = self.normalizeDictionary(model2.sentencepolarities)
        logProbsPols = self.compareDictionaries(self.sentencepolarities, nd1Pols, nd2Pols)
        d_name = 'Sentence Polarities'
        print(f"     {d_name:>28s}   {logProbsPols[0]:>10.2f}   {logProbsPols[1]:>10.2f} ")

        # sentence polarities parameter - increase winning model's score by 4
        if logProbsPols[0] > logProbsPols[1]:
            features += 1
            score1 += 4
        elif logProbsPols[0] < logProbsPols[1]:
            score2 += 4

        print("\nModel1 is superior for " + str(features) + " features.")
        features = 6 - features  # the number of aspects where model 2 wins
        print("\nModel2 is superior for " + str(features) + " features.")

        print("\nThe compatibility of a model is based on a weighted score.")
        print("The model with closer sentence lengths adds 1 to its score.\n(Sentence lengths are not very revealing of *song* nature).")
        print("For words, stems, and wordlengths, the closer model adds 2 to its score.")
        print("For subjectivity and polarity, the closer model adds 4 to its score.\n(Subjectivity and polarity tend to be revealing factors in song genre).\n")

        if score1 > score2:
            print("Model1 is a better match because its weighted score is " + str(score1) + ".")
        elif score2 > score1:
            print("Model2 is a better match because its weighted score is " + str(score2) + ".")


    def cleanString(self, s):
        
        """Returns the string s, but
           with only ASCII characters, only lowercase, and no punctuation.
           See the description and hints in the problem!
        """
        
        s = s.lower()    # Not implemented fully: this just lower-cases
        
        s = s.encode("ascii", "ignore")   # Ignores non-ASCII characters
        
        s = s.decode()         # Decodes it back to a string (with the non-ACSII characters removed)  

        for p in string.punctuation:
            s = s.replace(p, '')
                              
        return s






print("\n\n +++++++++++ Model1: Pop Songs +++++++++++ ")
TM1 = TextModel()
TM1.addFileText("popsongs.txt")
TM1.createAllDictionaries()  
print(TM1)

print(" +++++++++++ Model2: Country Songs +++++++++++ ")
TM2 = TextModel()
TM2.addFileText("countrysongs.txt")
TM2.createAllDictionaries()  
print(TM2)

print(" +++++++++++ Compare to: Taylor Swift's 'Country' Songs +++++++++++ ")
TM_Unk1 = TextModel()
TM_Unk1.addFileText("taylorswift*country*.txt")
TM_Unk1.createAllDictionaries()  
print(TM_Unk1)

TM_Unk1.compareTextWithTwoModels(TM1, TM2)


print("\n\n +++++++++++ Model1: Pop Songs +++++++++++ ")
TM1 = TextModel()
TM1.addFileText("popsongs.txt")
TM1.createAllDictionaries()  
print(TM1)

print(" +++++++++++ Model2: Country Songs +++++++++++ ")
TM2 = TextModel()
TM2.addFileText("countrysongs.txt")
TM2.createAllDictionaries()  
print(TM2)

print(" +++++++++++ Compare to: Taylor Swift's 'Pop' Songs +++++++++++ ")
TM_Unk2 = TextModel()
TM_Unk2.addFileText("taylorswift*pop*.txt")
TM_Unk2.createAllDictionaries()  
print(TM_Unk2)

TM_Unk2.compareTextWithTwoModels(TM1, TM2)






###### RUNS ######

"""

Comparing Taylor Swift's 'Country' Songs to the Pop and Country Models Yielded (among other very looong information):
"
                             Self        vsTM1        vsTM2 
                             ----        -----        ----- 
                            Words    -13650.77    -13622.14 
                            Stems    -13395.28    -13379.06 
                     Word Lengths     -4307.13     -4309.53 
                 Sentence Lengths      -597.91      -597.50 
          Sentence Subjectivities      -357.52      -338.49 
              Sentence Polarities      -376.64      -370.99 

Model1 is superior for 1 features.

Model2 is superior for 5 features.

The compatibility of a model is based on a weighted score.
The model with closer sentence lengths adds 1 to its score.
(Sentence lengths are not very revealing of *song* nature).
For words, stems, and wordlengths, the closer model adds 2 to its score.
For subjectivity and polarity, the closer model adds 4 to its score.
(Subjectivity and polarity tend to be revealing factors in song genre).

Model2 is a better match because its weighted score is 13.
"

Comparing Taylor Swift's 'Pop' Songs to the Pop and Country Models Yielded (among, again, very looong information):
"
                             Self        vsTM1        vsTM2 
                             ----        -----        ----- 
                            Words    -11582.28    -11733.74 
                            Stems    -11369.51    -11479.99 
                     Word Lengths     -3682.75     -3694.53 
                 Sentence Lengths      -562.53      -557.99 
          Sentence Subjectivities      -318.35      -312.48 
              Sentence Polarities      -306.26      -310.66 

Model1 is superior for 4 features.

Model2 is superior for 2 features.

The compatibility of a model is based on a weighted score.
The model with closer sentence lengths adds 1 to its score.
(Sentence lengths are not very revealing of *song* nature).
For words, stems, and wordlengths, the closer model adds 2 to its score.
For subjectivity and polarity, the closer model adds 4 to its score.
(Subjectivity and polarity tend to be revealing factors in song genre).

Model1 is a better match because its weighted score is 10.
"

This essentially confirms the categorization of Swift's music:
- The country music was comparable to model2 (country music).
- The pop music was comparable to model1 (pop music).

Therefore, these results were (overall) as expected.

In specific categories, there were some unexpected results:
- model2 (country music) was closer to Taylor Swift's pop music in subjectivity.
  - I had previously claimed that subjectivity/polarity should be the strongest indication of genre.
  - However, in this experiment, what the program determined as two "different genres" did end up having very close subjectivity values.
  - This indicates that the significance of the program's parameters may require some re-evaluation.

In general, this program seems to have been a success!

"""
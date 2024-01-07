#
# milestone.py
#
# TextModel project!
#
# Name: Leila Maboudian
#

from textblob import TextBlob
import string
from xml.etree.ElementTree import TreeBuilder

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
        s += f'Text[:42]    {self.text[:42]}\n'
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

    # Include other functions here.
    # In particular, you'll need functions that add to the model.

    def makeSentenceLengths(self):
        
        """Creates the dictionary of sentence lengths
               should use self.text, because it needs the punctuation!
        """
        
        LoW = self.text.split()
        
        words = 0
        
        for word in LoW:
            words += 1
            if word[-1] in '.!?':
                if words not in self.sentencelengths:
                    self.sentencelengths[words] = 1
                else:
                    self.sentencelengths[words] += 1
                words = 0
        
        # return self.sentencelengths

    def makeWordLengths(self):
        
        """Creates the dictionary of words lengths
               should use self.cleanedtext!
        """
        
        LoW = self.cleanedtext.split()
        
        for word in LoW:
            if len(word) not in self.wordlengths:
                self.wordlengths[len(word)] = 1
            else:
                self.wordlengths[len(word)] += 1
        
        # return self.wordlengths
    
    def makeWords(self):
        
        """Creates the dictionary of words
               uses self.cleanedtext!
        """

        LoW = self.cleanedtext.split()

        for word in LoW:
            if word not in self.words:
                self.words[word] = 1
            else:
                self.words[word] += 1

        # return self.words

    def makeStems(self):
        
        """ rules:
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

        """determines the sentence polarity/subjectivity distribution of a text.
        """

        LoW = self.text.split()
        
        sentence = ''
        pol = TextBlob(sentence).polarity
        sub = TextBlob(sentence).subjectivity

        for word in LoW:
            sentence += ' ' + word
            if len(word) > 1 and word[-1] in '.!?':
                if pol not in self.sentencepolarities:
                    self.sentencepolarities[pol] = 1
                else:
                    self.sentencepolarities[pol] += 1
                if sub not in self.sentencesubjectivities:
                    self.sentencesubjectivities[sub] = 1
                else:
                    self.sentencesubjectivities[sub] += 1
                sentence = sentence[0]
        
        # print(self.sentencesubjectivities)
        # print(self.sentencepolarities)

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

                              # ..things for now
        return s


# And let's test things out here...
TMintro = TextModel()

# Add a call that puts information into the model
TMintro.addRawText("""This is a small sentence. This isn't a small
sentence, because this sentence contains more than 10 words and a
number! This isn't a question, is it?""")

# Put the above triple-quoted string into a file named test.txt, then run this:
#  TMintro.addFileText("test.txt")   # "comment in" this line, once the file is created

# Print it out
print("TMintro is", TMintro)


# Add more calls - and more models - here:
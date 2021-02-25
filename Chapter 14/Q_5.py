""""Write a class called Wordplay. It should have a
field that holds a
list of words. The user
of the class should pass the list of words they want to use to the class.
There should be the
following methods:
• words_with_length(length)— returns a list of all the words of length length
• starts_with(s)— returns a list of all the words that start with s
• ends_with(s)— returns a list of all the words that end with s
• palindromes()— returns a list of all the palindromes in the list
• only(L)— returns a list of the words that contain only those letters in L
• avoids(L)— returns a list of the words that contain none of the letters in L"""


class Wordplay:
    def __init__(self):
        self.words_list = []


    def words_with_length(self,length):
        wordlist = []
        for w in self.words_list:
            if len(w) == length:
                wordlist.append(w)
        return  "Words with length {} {}".format(length,wordlist)

    def start_with(self, s):
        wordlist = []
        for w in self.words_list:
            if (w[0] == s):
                wordlist.append(w)
        return "Words Start with letter {} {}".format(s,wordlist)

    def ends_with(self,s):
        wordlist =[]
        for w in self.words_list:
            if w[-1] == s:
                wordlist.append(w)
        return "Words Ending with letter {} {}".format(s,wordlist)

    def palindrome(self):
        wordlist =[]
        for w in self.words_list:
            if w[::1] == w[::-1]:
                wordlist.append(w)
        return "Palindromes {}".format(wordlist)

    def only_L(self):
        wordlist =[]
        for w in self.words_list:
            if "l" in w:
                wordlist.append(w)
        return "Words containing L {}".format(wordlist)


    def Not_L(self):
        wordlist = []
        for w in self.words_list:
            if "l" not in w:
                wordlist.append(w)
        return "Words Not containing L {}".format(wordlist)


a = Wordplay()

a.words_list=["solos","Marcus","Aurelius","Henryi","tirla","samantha","pocahontas","kayak"]

print(a.words_with_length(5))
print(a.start_with("M"))
print(a.ends_with("s"))
print(a.palindrome())
print(a.ends_with("s"))
print(a.only_L())
print(a.Not_L())

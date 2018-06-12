
def split_sent(stringy):
	anotherstr = stringy.replace('\n', ' ')
	import re
	return re.compile("(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s").split(anotherstr)
# this return compiles a pattern into an object and makes sure that the rules for a sentence are unbroken 	
#?<= matches if the current portion of the string is preceded by whatever is to the right of ?<= 
#?<!\w\.\w. makes sure that e.g. and i.e. are not mistaken for sentences. \w rerpresents unicode word characters
#(?<=\.|\?)\s makes sure that punctuation is followed by a space. 
#a sentence also cannot be immediately followed by a letter 
	

def split_words(sentence):
	somestr = sentence.replace(',', '').replace(':', '') 
#pretty straight forward gets rid of colons and commas
	somestr = somestr.rstrip('.') 
#removes period at the end of the string because we have established rules for a sentence and just need to worry about counting the words. 
	return somestr.split(' ')


def work(filestring):
	myDict = {}
#create dictionary
	sents = split_sent(filestring.lower())
#lower case
	sentno = 0
	for sentence in sents:
		sentno +=1 
		for words in split_words(sentence):
			if words.isdigit(): continue
#ignore numbers
			if words not in myDict:
				myDict[words] = 1 , [sentno]
#if word not in dictionary add it
			else:
				counter, slist = myDict[words]
				counter += 1
				slist.append(sentno)
				myDict[words] = counter, slist
#otherwise increment and add sentence number
	return myDict

def print_pretty(w):
	for key in sorted(w.iterkeys()):
#alphabetical order
		print "%s\t{%d:%s}" % (key, w[key][0], ','.join(map(str, w[key][1])))
#had to do some tricky printing stuff to prevent [] and replace with {}

example = """2 Wait a minute. Wait a minute, Doc.
Are you telling i.e. me that you built a ship out of a DeLorean? Given an arbitrary text document written in English,
write a program that will generate a concordance, i.e. an alphabetical
list of all word e.g. occurrences, 3 labeled with word frequencies. Bonus:
label each word with the 5 sentence numbers in which each occurrence
appeared."""

if __name__ == "__main__":
    import sys
print_pretty(work(example))


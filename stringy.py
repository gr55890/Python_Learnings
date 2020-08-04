
zenPython = ''' 
The Zen of Python, by Tim Peters 

Beautiful is better than ugly. 
Explicit is better than implicit. 
Simple is better than complex. 
Complex is better than complicated. 
Flat is better than nested.
Sparse is better than dense. 
Readability counts. 
Special cases aren't special enough to break the rules. 
Although practicality beats purity. 
Errors should never pass silently. 
Unless explicitly silenced. 
In the face of ambiguity, refuse the temptation to guess. 
There should be one-- and preferably only one --obvious way to do it. 
Although that way may not be obvious at first unless you're Dutch. 
Now is better than never. 
Although never is often better than *right* now. 
If the implementation is hard to explain, it's a bad idea. 
If the implementation is easy to explain, it may be a good idea.
'''

words=zenPython.split()
print(len(words))

#words= [i.strip().strip(,).strip(.).strip(-).strip(*).strip(!) for i in words]
words= [i.strip(' ,.-*!') for i in words]
print(words)
words= [i.lower() for i in words]
print(words)
unique_words=set(words)
print(unique_words)

word_frequency = dict(filter(lambda elem: elem[0] % 2 == 0, dictOfNames.items()))
#res = {test_keys[i]: test_values[i] for i in range(len(test_keys))} 
#newDict = dict(filter(lambda elem: elem >5, words.items()))

# Web Crawler (Keyword-Extractor)

Problem:        Suppose you are given a paragraph and you have to find the topic or keywords of the paragraph. Then you have to read the complete paragraph and
		searching content related to that keyword is more time consuming.

Idea:		To develop an application that takes the text as input and produce the keywords, not only keywords but data from internet related to those keywords
		as well
				
Requirement:    Python3

How this works: This application takes text in the textfield and using RAKE algorithm finds the keywords. The keyword with most value is now searched over the internet
                and application provides the more data about that keyword.
                
 [  Wondering how RAKE algorithm works? ]
 		
		In this first the text splits (parsed) into the set of candidates' keywords. First, the document text is split into an array of words then this array
		is then split into sequences of contiguous words at phrase delimiters and stop word positions.
		
		After every candidate keyword that is identified, a score is calculated with the help of word co-occurance graph
		
		The score for each candidate keyword is computed by the formula K=deg(t)/freq(t)
		
		The score of the keyword is computed as the sum of its member keyword score
		
		After candidate keywords are scored, the top T scoring candidates are selected as keywords for the document. 
		
Still in confusion??
Follow this link for PPT on RAKE:

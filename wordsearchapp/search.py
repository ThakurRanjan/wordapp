import operator

word_count = {}
words = []
# open the file read mode
with open('F:\DJANGO\Project\word_search.tsv') as datafile:
	for row in datafile:
        # split  into word and occurence
		word, frequency = row.split('\t')
        # insert into the wordcount dictionary key as word and value as frequency
		word_count[word] = int(frequency.strip())
        # insert only the word in words
		words.append(word)

#Search method to check the input word is present in word of words list.
def search(word_letter):
	results = []
	for word in words:
		if word_letter in word:
			results.append(word)
	return results

#This part sorts words based on a match the search keyword.
# 1. Matches at the start of a word ranks higher.
# 2. Common words ranks higher than rare words.
# 3. Short words ranks higher than long words.
# 4. An exact match always ranks as the first result.
def sorting(results, incomplete_word):
	result_distances = [(result, result.find(incomplete_word), word_count[result], len(result)) for result in results]
	result_distances.sort(key=operator.itemgetter(1))
	result_distances.sort(key=operator.itemgetter(3))
	searchResults = [result_distance[0] for result_distance in result_distances][:25]
	return searchResults

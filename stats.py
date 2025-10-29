def word_count(text):
	word_list = text.split()
	return len(word_list)

def letter_count(text):
	lowered_text = text.lower()
	letter_dict = {}
	for letter in lowered_text:
		if letter not in letter_dict:
			letter_dict[letter] = 1
		else:
			letter_dict[letter] += 1

	return letter_dict
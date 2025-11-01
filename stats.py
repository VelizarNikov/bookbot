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

def sort_on(items):
    return items["num"]

def sorted_list(dictionary):
	ch_list = []
	for k,v in dictionary.items():
		ch_dict = {}
		ch_dict["char"] = k
		ch_dict["num"] = v
		ch_list.append(ch_dict)
		ch_list.sort(reverse=True, key=sort_on)
	return ch_list


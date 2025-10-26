def get_book_text(path_to_file):
	with open(path_to_file) as f:
		return f.read()
	
def word_count(text):
	word_list = text.split()
	return len(word_list)

def main():
	path = "books/frankenstein.txt"
	text = get_book_text(path)
	num_words = word_count(text)
	print(f"Found {num_words} total words")

main()
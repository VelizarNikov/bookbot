import sys
if len(sys.argv) < 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

def get_book_text(path_to_file):
	with open(path_to_file) as f:
		return f.read()
	
from stats import word_count, letter_count, sorted_list

def main():
	path = sys.argv[1]
	text = get_book_text(path)
	num_words = word_count(text)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at{path}")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	sorted_counts = sorted_list(letter_count(text))
	for item in sorted_counts:
		ch = item["char"]
		if ch.isalpha():
			print(f"{ch}: {item["num"]}")
	print("============= END ===============")

main()
import sys

from stats import count_chars, count_words, sort_chars


def get_book_text(path: str):
    with open(path) as f:
        return f.read()

def print_stats(chars: list[dict]) -> None:
    for char in chars:
        print(f"{char['char']}: {char['num']}")


def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	else:
		path:str = str(sys.argv[1])

	print("============ BOOKBOT ============")
	print("Analyzing book found at books/frankenstein.txt...")
	text = get_book_text(path)
	print("----------- Word Count ----------")
	print(f"Found {count_words(text)} total words")
	print("--------- Character Count -------")
	print_stats(sort_chars(count_chars(text)))
	print("============= END ===============")


if __name__ == "__main__":
    main()

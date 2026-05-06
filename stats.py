def count_words(text:str) -> int:
	return len(text.split())

def count_chars(text:str) -> dict[str, int]:
	lower_case = text.lower()
	chars = {}
	for char in lower_case:
		if char in chars: 
				chars[char] += 1
		else: 
			chars[char] = 1
	return chars

def sort_chars(chars:dict[str,int]) -> list[dict[str,str|int]]:
	return sorted(transform_dict(chars), reverse=True, key=lambda item: item["num"])

def transform_dict(chars:dict[str,int]) -> list[dict[str,str|int]]:
	transformed_list:list[dict[str,str|int]] = []
	char_name = "char"
	count_name = "num"
	for char in chars:
		if char.isalpha():
			transformed_list.append({char_name:char, count_name:chars[char]})
	return transformed_list
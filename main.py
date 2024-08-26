def get_file_contents(filepath:str):
	with open(filepath) as f:
		contents = f.read()
	return contents

def count_words(text:str):
	words = text.split()
	return len(words)

def count_chars(text:str):
	char_dict = {}
	for c in text:
		c = c.lower()
		if c not in char_dict:
			char_dict[c] = 1
		else:
			char_dict[c] += 1
	return char_dict

def sort(dict:dict):
	list = convert_dict_to_list(dict)
	list.sort(reverse=True, key=sort_on)
	return list

def sort_on(dict):
	return dict["count"]

def convert_dict_to_list(dict:dict[str,int]):
	list = []
	for char in dict:
		if char.isalpha():
			list.append({"char": char, "count": dict[char]})
	return list

def print_report(list:list[dict], word_count:int):
	print('--- Begin report of books/frankenstein.txt ---')
	print(f"{word_count} words found in the document")
	print()
	for item in list:
		print(f"The '{item['char']}' character was found {item['count']} times")
	print('--- End report ---')
	
def main():
	contents = get_file_contents("./books/frankenstein.txt")
	words = count_words(contents)
	dict = count_chars(contents)
	sorted = sort(dict)
	print_report(sorted, words)

main()
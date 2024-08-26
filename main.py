def main():
	with open("./books/frankenstein.txt") as f:
		contents = f.read()
		words = contents.split()
		print(len(words))

main()
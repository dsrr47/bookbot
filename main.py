import sys

print(sys.argv)

if len(sys.argv) < 2:
  print(" Usage: python3 main.py <path_to_book>")
  sys.exit(1)

with open(sys.argv[1]) as f:
    file_contents = f.read()

def main():
  words = file_contents.split()
  print(f"""
        --- Begin report of {sys.argv[1]} ---
        {len(words)} words found in the document
        """)
  character_count(file_contents)
  print("--- End report ---")

def character_count(book):
    characters = list(book.lower())
    char_dict = {}

    for character in characters:
        if character not in char_dict:
            char_dict[character] = 1
        else:
            char_dict[character] += 1
    for char in char_dict:
      alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
      if char in alphabet:
        print(f"The '{char}' character was found {char_dict[char]} times")

main()
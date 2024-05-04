def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = num_of_words(text)
    chars_dict = num_of_letters(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print("--- Begin report of Frankenstein ---")
    print(f"{num_words} words found")
    print()

    for item in chars_sorted_list:
      print(f"'{item['char']}' was found {item['num']} times")

    print("--- End report ---")

def sort_on(d):
  return d["num"]

def chars_dict_to_sorted_list(chars_dict):
  sorted_list = []
  for char in chars_dict:
    sorted_list.append({"char": char, "num": chars_dict[char]})
  sorted_list.sort(reverse=True, key=sort_on)
  return sorted_list

def num_of_letters(text):
  chars_dict = {}
  for chars in text:
    if chars.isalpha() == True:
      chars_lower = chars.lower()
      if chars_lower in chars_dict:
        chars_dict[chars_lower] += 1
      else:
        chars_dict[chars_lower] = 1
  return chars_dict

def num_of_words(text):
  words = text.split()
  return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()

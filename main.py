def main():
    bookpath = "books/frankenstein.txt"
    with open(bookpath) as f:
        file_contents = f.read()
        #print(f"words count: {count_words(file_contents)}")
        #print(get_used_chars_dict(file_contents))
        #print(get_report_header(bookpath))
        print(f"--- Begin report of {bookpath} ---")
        print(f"{count_words(file_contents)} words found in the document")
        chars = get_used_chars_dict(file_contents)
        print_detailed_report(chars)
        print("--- End report ---")

def get_used_chars_dict(contents):
    lower_case = contents.lower()
    char_dict = {}
    for c in lower_case:
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1
    return char_dict

def count_words(context):
    words = context.split()
    return len(words)

def print_detailed_report(char_dict):
    sorted_chars = dict(sorted(char_dict.items(), key=lambda item:item[1], reverse=True))
    for c in sorted_chars:
        if (c.isalpha()):
            print(f"The '{c}' character was found {sorted_chars[c]} times")

        

main()
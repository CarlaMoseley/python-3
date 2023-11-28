
def count_words(*file_names):
    small_word =set()
    long_word = set()
    for file_name in file_names:
        with open (file_name, 'r') as file:
            content = file.read()
            word_list = content.split()
            count = 0
            for i in range (len(word_list)):
                count = i
            for i in word_list:
                if len(i) < 3:
                    small_word.add(i)
                else:
                    long_word.add(i)
        return count, small_word,long_word
def main():
    total_words = count_words("C:/Users/f92slpy/techprojects\python-3/files/words.txt")
    print(total_words)

if __name__ == '__main__':
    main()
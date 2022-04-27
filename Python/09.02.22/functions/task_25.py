#!/usr/bin/python3
def vowels_in_a_words(ml):
    my_dict={}
    cnt=0
    for word in ml:
        for let in word:
            if let in 'aiuoe':
                cnt+=1
        my_dict[word] = cnt
        cnt=0
    return my_dict
def sort_dict(my_dict):
    my_dict = sorted(my_dict.items(), reverse=True,  key=lambda x: x[1])
    return my_dict[0]
def main():
    ml = ["london", "is", "a", "capital", "of", "great", "britain"]
    print(sort_dict(vowels_in_a_words(ml)))
if __name__ == "__main__":
    main()

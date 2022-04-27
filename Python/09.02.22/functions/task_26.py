#!/usr/bin/python3
def longest_sentence(ml):
    sen_ml=[]
    for sentence in ml:
        nml = sentence.split()
        sen_ml.append(nml)
    return sen_ml
def sort_sentences(sen_ml):
    sen_ml = sorted(sen_ml, key=len, reverse=True)
    longest_sen = ""
    for el in sen_ml[0]:
        longest_sen += el+" "
    return longest_sen
def main():
    ml = ["Lorem Ipsum is simply dummy text of the printing and typesetting industry.", "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.", "It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.", "It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum"]
    ls=longest_sentence(ml)
    print(sort_sentences(ls))
if __name__ == "__main__":
    main()

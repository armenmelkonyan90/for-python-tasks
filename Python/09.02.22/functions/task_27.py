#!/usr/bin/python3
def find_the_numbers(mstr):
    nums=""
    num_list=[]
    for i in range(len(mstr)):
        if mstr[i].isdigit():
            nums+=mstr[i]
        else:
            if nums != "":
                num_list.append(int(nums))
                nums=""
    return num_list
def sort_nums(num_list):
    num_list=sorted(num_list, reverse=True)
    return num_list[0]



def main():
    mstr = "World War II is generally considered to have begun on 1 September 1939, when Nazi Germany, under Adolf Hitler, invaded Poland. The United Kingdom and France subsequently declared war on Germany on 3 September. Under the Molotov–Ribbentrop Pact of August 1939, Germany and the Soviet Union had partitioned Poland and marked out their 'spheres of influence' across Finland, Estonia, Latvia, Lithuania and Romania. From late 1939 to early 1941, in a series of campaigns and treaties, Germany conquered or controlled much of continental Europe, and formed the Axis alliance with Italy and Japan (along with other countries later on). Following the onset of campaigns in North Africa and East Africa, and the fall of France in mid-1940, the war continued primarily between the European Axis powers and the British Empire, with war in the Balkans, the aerial Battle of Britain, the Blitz of the UK, and the Battle of the Atlantic. On 22 June 1941, Germany led the European Axis powers in an invasion of the Soviet Union, opening the Eastern Front, the largest land theatre of war in history."
    ftn=find_the_numbers(mstr)
    print(sort_nums(ftn))
if __name__ == "__main__":
    main()


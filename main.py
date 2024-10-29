def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()
        count_dict = char_count(file_contents)
        count_list = []
        for item in count_dict:
            if item.isalpha():
                print(item)
                print(item,count_dict[item])
                count_list.append({"letter":item,"count":count_dict[item]})
        count_list.sort(reverse= True, key =sort_on)

        print(f"--- Begin report of books {path} ---")
        for item in count_list:
            print(f"The '{item["letter"]}' was found {item["count"]} times")

def char_count(text):
    count_dict = {}
    lower_list = text.lower().split()
    for word in lower_list:
        for i in range(len(word)):
            if word[i] not in count_dict:
                count_dict[word[i]] = 1
            else:
                count_dict[word[i]] +=1
    return count_dict

def sort_on(dict):
    return dict["count"]


        


main()
        


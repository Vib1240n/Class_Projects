

def reorderLogFiles(logs):
    letter_log = []
    digit_log  = []
    final_list = []
    for i in logs:
        stuff = i.split(" ")
        if stuff[1].isdigit():
            digit_log.append(i)
        else:
            letter_log.append((stuff[0]," ".join(stuff[1:])))
    letter_log.sort(key= lambda x: (x[1], x[0]))
    final_list = [ " ".join(i) for i in letter_log ]
    final_list.extend(digit_log)
    return final_list
    
    
if __name__ == "__main__":
    logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    l = reorderLogFiles(logs)
    print(l)
    
    
# dir
#         subdir1
#                 file1.ext
#                 subsubdir1
#         subdir2
#                 subsubdir2
#                         file2.ext


# def lengthLongestPath(Input) -> int:
#     dict = {}
#     long = 0
#     file = Input.split('\n')
#     for i in file:
#         if "." not in i:
#             key = i.count('\t')
#             value = len(i.replace('\t', ''))
#             dict[key] = value
#         else:
#             key = i.count('\t')
#             length = sum([dict[j] for j in dict.keys() if j < key]) + len(i.replace('\t', '')) + key
#             long = max(long, length)
#     return long


# if __name__ == "__main__":
#     Input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
#     l = lengthLongestPath(Input)
#     print(l)


# "dir/subdir1/file1.ext" of length 21
# "dir/subdir2/subsubdir2/file2.ext" of length 32.
# Explanation: We have only one file, and the absolute path is "dir/subdir2/file.ext" of length 20.

# def reverse(head):
#     nxt = None
#     while head:
#         tmp = head.next
#         head.next = nxt
#         nxt = head
#         head = tmp
#     return nxt


# def has_cycle(head):
#     visited = set()
#     f = head
#     while f:
#         i = id(f)
#         if i in visited:
#             return 1
#         visited.add(i)
#         f = f.next
#     return 0
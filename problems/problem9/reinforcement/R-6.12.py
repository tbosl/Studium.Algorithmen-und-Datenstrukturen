# What values are returned during the following sequence of deque ADT operations, on initially empty deque?
# add first(4), -> [4]
# add last(8), -> [4,8]
# add last(9), -> [4,8,9]
# add first(5), -> [5,4,8,9]
# back( ), -> 9
# delete first( ), -> 5 | [4,8,9]
# delete last( ), -> 9 | [4,8]
# add last(7), -> [4,8,7]
# first( ), -> 4
# last( ), -> 7
# add last(6), -> [4,8,7,6]
# delete first( ), -> 4 | [8,7,6]
# delete first( ). -> 8 | [7,6]

#

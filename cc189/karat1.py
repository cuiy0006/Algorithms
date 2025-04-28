def is_anagram(word, word_lst):
    freqs = {}
    for c in word:
        if c not in freqs:
            freqs[c] = 0
        freqs[c] += 1
    
    res = []
    for word in word_lst:
        dic = {}
        for c in word:
            if c not in dic:
                dic[c] = 0
            dic[c] += 1
        add = True
        for c, freq in dic.items():
            if c not in freqs or freq > freqs[c]:
                add = False
                break
        if add:
            res.append(word)
    return res

def main():
    print(is_anagram("tacjbcebef", ["cat", "baby", "bird", "fruit"])) # cat
    print(is_anagram("bacdrigb", ["cat", "baby", "bird", "fruit"])) # bird

if __name__ == "__main__":
    main()



# [("A", "3:44"), ("B", "5:00"), ("C", "3:16")] -> ["A", "C"]

SEVEN_MINTES = 7 * 60

def find_pair(input):
    length_to_music = {}
    for music, l in input:
        mins, secs = l.split(':')
        seconds = int(mins)*60 + int(secs)
        if SEVEN_MINTES-seconds in length_to_music:
            return (music, length_to_music[SEVEN_MINTES-seconds])
        length_to_music[seconds] = music
    return None

print(find_pair([("A", "3:44"), ("B", "5:00"), ("C", "3:16")]))






# We are playing a game where the player needs to follow instructions to find a treasure. 
# There are multiple rooms, aligned in a straight line, labeled sequentially from 0. 
# Each room contains one instruction, given as a positive integer. 
# An instruction directs the player to move forward a specific number of rooms. 
# The last instruction is "9" by convention, and can be ignored (there's no room to move after the last room). 
# The player starts the game in room number 0 and has to reach the treasure which is in the last room. 
# The player is given an amount of money to start the game with. 
# She must use this money wisely to get to the treasure as fast as possible. 
# The player can follow the instruction or pay $1 to change the value of the instruction by one. 
# For example, for $1, the instruction "2" may be changed to "1" or "3". 
# A player cannot pay more than $1 to change the value of an instruction by more than one unit. 
# Write a function that takes a list of instructions and a total amount of money as input 
# and returns the minimum number of instructions needed to reach the treasure room, or None/null/-1 if the treasure cannot be reached.

# Examples Note: The updated instructions are marked with *.
# Example 1
# instructions_2_1 = [1, 1, 1, 9]
# With $0, the player would follow 3
# instructions: Instructions: [ 1, 1, 1, 9]
# Itinerary: [ 1, 1, 1, 9] ^ ^ ^ ^
# With $1,
# the player would reach the treasure in 2
# instructions: she could change, for example, the first instruction to 2.
# Instructions: [ 1, 1, 1, 9]
# Itinerary: [ *2, 1, 1, 9] ^ ^ ^
# Example 2
# instructions_2_2 = [1, 1, 2, 9]
# With $0 as the initial amount, the treasure is not reachable.
# With $1 (or more) as the initial amount, the treasure can be reached in 2 instructions.
# Instructions: [ 1, 1, 2, 9] Itinerary: [ 1, *2, 2, 9]

from collections import deque

def get_minimum_step(instructions, dollars):
    end = len(instructions)-1
    q = deque([(0, dollars)])
    d = 0
    seen = set()
    while len(q) != 0:
        size = len(q)
        for _ in range(size):
            curr, left = q.popleft()
            if curr == end:
                return d
            if curr in seen or curr < 0 or curr > end:
                continue
            seen.add(curr)
            reach = curr+instructions[curr]
            q.append((reach, left))
            if left > 0:
                q.append((reach-1, left-1))
                q.append((reach+1, left-1))
        d += 1
    return -1

def main():
    print(get_minimum_step([1, 1, 1, 9], 0)) # 3
    print(get_minimum_step([1, 1, 1, 9], 1)) # 2 
    print(get_minimum_step([1, 1, 2, 9], 0)) # -1
    print(get_minimum_step([1, 1, 2, 9], 1)) # 2

if __name__ == "__main__":
    main()





from collections import deque

def destinations(teleporters, dies, start, end):
    from_to = {}
    for s in teleporters:
        [a, b] = s.split(',')
        from_to[int(a)] = int(b)
    
    res = set()
    for die in range(1, dies+1):
        curr = start+die
        if curr == end:
            res.add(curr)
            break
        if curr in from_to:
            curr = from_to[curr]
        res.add(curr)
    return res

def finishable(teleporters, dies, start, end):
    if start == end:
        return True
    q = deque([start])
    seen = set()
    while len(q) != 0:
        curr = q.popleft()
        if curr in seen:
            continue
        seen.add(curr)
        dests = destinations(teleporters, dies, curr, end)
        for dest in dests:
            if dest == end:
                return True
            if dest not in seen:
                q.append(dest)
    return False

def main():
    teleporters1 = ["3,1", "4,2", "5,10"]
    teleporters2 = ["5,10", "6,22", "39,40", "40,49", "47,29"]
    teleporters3 = ["6,18", "36,26", "41,21", "49,55", "54,52", "71,58", "74,77", "78,76", "80,73", "92,85"]
    teleporters4 = ["97,93", "99,81", "36,33", "92,59", "17,3", "82,75", "4,1", "84,79", "54,4", "88,53", "91,37", "60,57", "61,7", "62,51", "31,19"]
    teleporters5 = ["3,8", "8,9", "9,3"]

    print(destinations(teleporters1, 6, 0, 20)) #=> [1, 2, 10, 6]
    print(destinations(teleporters2, 6, 46, 100)) #=> [48, 49, 50, 51, 52, 29]
    print(destinations(teleporters2, 10, 0, 50)) #=> [1, 2, 3, 4, 7, 8, 9, 10, 22]
    print(destinations(teleporters3, 10, 95, 100)) #=> [96, 97, 98, 99, 100]
    print(destinations(teleporters3, 10, 70, 100)) #=> [72, 73, 75, 76, 77, 79, 58]
    print(destinations(teleporters4, 6, 0, 100)) #=> [1, 2, 3, 5, 6]
    print(destinations(teleporters5, 6, 0, 20)) #=> [1, 2, 4, 5, 6, 8]

    teleporters1 = ["10,8", "11,5", "12,7", "13,9"]
    teleporters2 = ["10,8", "11,5", "12,7", "13,9", "2,15"]
    teleporters3 = ["10,8", "11,5", "12,1", "13,9", "2,15"]
    teleporters4 = ["2,4", "9,8", "11,7", "12,6", "18,14", "19,16", "20,9", "21,14", "22,6", "23,26", "25,10", "28,19", "29,27", "31,29", "38,33", "39,17", "41,30", "42,28", "45,44", "46,36"]
    teleporters5 = ["4,21", "11,18", "13,17", "16,17", "18,21", "22,11", "26,25", "27,9", "31,38", "32,43", "34,19", "35,19", "36,39", "38,25", "41,31"]

    print(finishable(teleporters1, 4, 0, 20)) #=> False (Above)
    print(finishable(teleporters2, 4, 0, 20)) #=> True (Above)
    print(finishable(teleporters2, 4, 9, 20)) #=> False (Above)
    print(finishable(teleporters3, 4, 9, 20)) #=> True
    print(finishable(teleporters4, 4, 0, 50)) #=> False
    print(finishable(teleporters4, 6, 0, 50)) #=> True
    print(finishable(teleporters5, 4, 0, 50)) #=> True
    print(finishable(teleporters5, 2, 0, 50)) #=> False

if __name__ == "__main__":
    main()



# 1， 二维数组，表示两个user之间的关注操作，只有关注和取关 例如：
# events: [["Nicole", "Alice", "CONNECT"], ["Nicole", "Alice", "DISCONNECT"], ["Charlie", "Alice", "CONNECT"], ["Edward", "Alice", "CONNECT"] ]
# 2，关注的人个数，例如3
# 需要返回：二维数组，数组第一项是小于给定的connect的人，第二项是大于等于connect的人。不用排序
# 例如：
# grouping(events, 3):[[Nicole, Alice, Charlie, Pam], [Bob, Dennis, Edward]]
# grouping(events, 1):[[], [Nicole, Bob, Alice, Charlie, Dennis, Edward, Pam]]
# grouping(events, 10):[[Nicole, Bob, Alice, Charlie, Dennis, Edward, Pam], []]
# Code2 没有时间写了，说了思路
# 电影推荐，类似上题
# ratings = [ ["Alice", "Frozen", "5"], ["Bob", "Mad Max", "5"],
# ["Dennis", "Mad Max", "4"],
# ["Bob", "Lost In Translation", "5"],
# ]
# Bob 和 Dennis都看过Mad Max，打分都超过3分。认为他们两个可以互相推荐。Bob看过Lost In Translation， 但Dennis没有看过。需要Bob推荐给他这部电影
# 返回：recommendations("Dennis", ratings) => ["Lost In Translation"]

def grouping(events, limit):
    dic = {}
    for [a, b, event] in events:
        if event == 'CONNECT':
            if a not in dic:
                dic[a] = 0
            dic[a] += 1
            if b not in dic:
                dic[b] = 0
            dic[b] += 1
        else:
            dic[a] -= 1
            dic[b] -= 1
    more = []
    less = []
    for user, cnt in dic.items():
        if cnt < limit:
            less.append(user)
        else:
            more.append(user)
    return [more, less]

def recommendations(user, ratings):
    seen_movies = set()
    high_score_movies = set()
    high_score_movie_to_users = {}
    user_to_movies = {}
    for [u, movie, score] in ratings:
        if u == user:
            seen_movies.add(movie)
            if score >= '3':
                high_score_movies.add(movie)
        if score >= '3':
            if movie not in high_score_movie_to_users:
                high_score_movie_to_users[movie] = set()
            high_score_movie_to_users[movie].add(u)
        if u not in user_to_movies:
            user_to_movies[u] = set()
        user_to_movies[u].add(movie)
    qualified_users = set()
    for movie in high_score_movies:
        qualified_users |= high_score_movie_to_users[movie]
    qualified_users.remove(user)
    res = []
    for u in qualified_users:
        for movie in user_to_movies[u]:
            if movie not in seen_movies:
                res.append(movie)
    return res

ratings = [ ["Alice", "Frozen", "5"], ["Bob", "Mad Max", "5"], ["Dennis", "Mad Max", "4"], ["Bob", "Lost In Translation", "5"]]
print(recommendations('Dennis', ratings))



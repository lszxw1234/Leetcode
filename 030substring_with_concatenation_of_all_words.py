class Solution:
    def findSubstring(self, s, words):
        from collections import deque, defaultdict, Counter

        s_len, word_len = len(s), len(words[0])
        word_len_total = word_len * len(words)
        count = Counter(words)
        footprint = defaultdict(deque)
        result = []

        for start in range(word_len):
            footprint.clear()
            end = start
            while start + word_len_total <= s_len:
                sub = s[end:end + word_len]
                end += word_len
                if sub in count:
                    queue = footprint[sub]
                    queue.append(end)
                    while  queue[0] < start:
                        queue.popleft()
                    if len(queue) > count[sub]:
                        start = queue.popleft()
                    if start + word_len_total == end:
                        result.append(start)
                else:
                    start = end

        return result

A = Solution()
print(A.findSubstring("barfoothefoobarman",["foo","bar"]))


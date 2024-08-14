class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        groups = [s[i:i+k] for i in range(0, len(s), k)]
        if len(groups[-1]) < k:
            groups[-1] += fill * (k - len(groups[-1]))
        return groups
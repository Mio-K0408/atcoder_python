def count_valid_subsequences(N, A):
    ans = N  # 長さ1の部分列は常にカウント

    for i in range(N - 1):
        # 長さ2の部分列をカウント
        ans += 1

        if i < N - 2:
            # 長さ3以上の部分列をチェック
            diff1 = A[i + 1] - A[i]
            diff2 = A[i + 2] - A[i + 1]
            
            if abs(diff1) == abs(diff2):
                j = i + 3
                while j < N and abs(A[j] - A[j - 1]) == abs(diff1):
                    j += 1
                ans += j - i - 2

    return ans

# 入力
N = int(input())
A = list(map(int, input().split()))

# 結果を出力
print(count_valid_subsequences(N, A))
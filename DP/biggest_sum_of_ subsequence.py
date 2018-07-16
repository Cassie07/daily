'''
1.最大连续子序列之和

给定K个整数的序列{ N1, N2, ..., NK }，其任意连续子序列可表示为{ Ni, Ni+1, ..., Nj }，其中 1 <= i <= j <= K。
最大连续子序列是所有连续子序中元素和最大的一个， 例如给定序列{ -2, 11, -4, 13, -5, -2 }，其最大连续子序列为{ 11, -4, 13 }，最大和为20。

'''
d=[1,-2,3,-1,7]
sum=0
maxn=0
for i in range(len(d)):
    sum+=d[i]
    if(sum<0):
        sum=0
        maxn=0
    maxn=max(maxn,sum)
print(maxn)

# 状态转移方程 max_sum=max(max_sum,sum+d[i])

N=int(input())
start=N
cicle=0
while True:
    N1 = int(N/10)
    if N<10:
        N2 = N
    else:
        N2 = N-(N1*10)
    N=N1+N2
    N=(N2*10) + (N-int(N/10)*10)
    cicle=cicle+1
    if start==N:
        break 
print(cicle)

#2022.10.22 / 30 Minute / 파이썬 문법 되새기기 + 오랜만에 하는 코딩 몸풀기
#1일차 시작
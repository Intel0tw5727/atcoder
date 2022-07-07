from sys import exit

def main():
    N, K = map(int, input().split()) 
    an = list(map(int, input().split()))

    # print(an)

    counter = 0

    for i in range(2 * 10**9 + 1):
        if i == 2* 10**9:
            print('No')
            exit()

        # print(an)
        try:
            diff = an[counter+K] - an[counter]
            # print(f'diff: {diff}')
            if diff >= 0:
                # 入れ替え操作
                counter += 1
                
            else:
                # print(f'counter: {counter}')
                a, b = an[counter+K], an[counter]
                # print(a, b)
                an[counter], an[counter+K] = a, b
                # print(an)
                # 何もしない
                # counter = counter - 1
                counter += 1

        except:
            if an == sorted(an):
                print('Yes')
            else:
                print('No')
            exit()

main()

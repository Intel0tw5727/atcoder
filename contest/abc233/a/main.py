def main():
    b, c = map(int, input().split())
    
    a=c-b
    
    counter = 0
    while a >= 10:
      a -= 10
      counter += 1
      
    if a <= 0:
      print(counter)
    else:
      print(counter+1)

main()

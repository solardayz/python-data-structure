def main():
    print("Hello World")

def DFS(n):
    if n == 3:
        for i in range(1, 4):
            print(i)
    else:
        DFS(n+1)

if __name__ == "__main__":
   main()
   DFS(1)
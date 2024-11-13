
def romanToInt(s: str) -> int:
    hashmap = { 'I':1 , 'V':5 , 'X':10 , 'L':50 , 'C':100 ,
            'D':500 , 'M':1000 }
    number = 0
    x = len(s)
    i = 0
    while i < x :
        if i+1 < x and hashmap[s[i+1]] > hashmap[s[i]]:
            number -= hashmap[s[i]]
        else:
            number += hashmap[s[i]]
        i+=1
    return number

def main ():
    num = input("enter the roman number: ")
    print(f"this romen number {num} = {romanToInt(num)}.")

if __name__ == "__main__":
    main()

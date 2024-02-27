
def is_palindrome(teststr):
    auxs=teststr.lower()
    auxs2=""

    for a in auxs:
        if a.isalnum():
            auxs2+=a

    auxs3=""
    aux_index=len(auxs2)-1

    while(aux_index >= 0):
        auxs3 += auxs2[aux_index]
        aux_index-=1
    
    if auxs3 == auxs2:
        return True

    return False

def main():
    print(str(is_palindrome("ABBA!")) + " Palindrome")

if __name__ == "__main__":
    main()

    
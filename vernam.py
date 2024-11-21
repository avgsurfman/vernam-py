#!/usr/bin/env python3

import sys
import os
import ast

def szyfrowanie(text : str, key : str) -> bytearray:
    text_b = bytearray(text, 'utf-8') # immutable
    key_b = bytearray(key, 'utf-8')
    if (roznica := (len(key_b) - len(text_b))) < 0:
        print(f"Wykryto różnicę w paddingu, dodawanie {abs(roznica)} bajtów... \n")
        key_b.extend(klucz_extra := os.urandom(abs(roznica)))
        print(f"Dodano do klucza ({key_b}): {klucz_extra}")
    elif (roznica > 0):
        print(f"Tekst jest krótszy od hasła. ")
  
    # print(text_b)
    # print(key_b)
    szyfrogram = bytes(a ^ b for a, b in zip(text_b, key_b))
    # https://www.reddit.com/r/learnpython/comments/zz76oc/how_would_i_xor_2_bytes_objects/
    print(f"Szyfrogram: {szyfrogram}")
    return szyfrogram


def deszyfrowanie(text: str, key: str) -> str:
    szyfrogram = ast.literal_eval(text)
    key = ast.literal_eval(key)
    result = bytes(a ^ b for a, b in zip(szyfrogram, key)).decode('utf-8')
    print(result)


def main():
    # usage : plaintext -> cypher will be generated ( 4 you ) 
    # or -c for cyphering, -d for decyphering with bytes in double quotes ""
    # no I'm not adding help for a 50 line util 
    print(f"{sys.argv[1:]}")

    if len(sys.argv[1:]) == 3:
        if sys.argv[1] == "-c":
            szyfrowanie(sys.argv[2], sys.argv[3])
        elif sys.argv[1] == "-d":
            deszyfrowanie(sys.argv[2], sys.argv[3])
    elif len(sys.argv[1:]) == 1:
        szyfrowanie(sys.argv[1], "")
    else:
        print("Błąd: Brak wpisanego tekstu lub za dużo argumentów.")


if __name__ == "__main__":
    main()

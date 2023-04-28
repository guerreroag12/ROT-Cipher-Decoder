rotation = int(input("Enter number of rotations: "))
pt_alphabet = "abcdefghijklmnopqrstuvwxyz"
ct_alphabet = (pt_alphabet[rotation:] + pt_alphabet[:rotation])

decode_trans = str.maketrans(ct_alphabet, pt_alphabet)

def subst_decode(s):
    return s.translate(decode_trans)

print(subst_decode(input("Enter ciphertext to decode: ")))

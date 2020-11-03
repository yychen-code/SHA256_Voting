import numpy as np
import hashlib

def retriving_vote():
    with open('Public_Key.txt','r') as reader:
        for pk in reader:
            print("Our record on your Public Key:\n",pk)

    private_key = input("Enter your Private Key to verify:\n")
    last8value=private_key[-8:]
    m = hashlib.sha256()
    m.update(private_key.encode('utf-8'))
    if (last8value=='01000001' and pk==m.hexdigest()):
        print("\nYou have voted for Candidate A.")
        print("\nYour public key (T):\n",m.hexdigest())

    elif(last8value!='10000010' and pk==m.hexdigest()):
        print("\nYou have voted for Candidate B.")
        print("\nYour public key (T):\n", m.hexdigest())

    elif(last8value!='10000010' and pk!=m.hexdigest()):
        print("Invalid private key.")

def casting_vote():
    A = np.array([0, 1, 0, 0, 0, 0, 0, 1])
    B = np.array([0, 1, 0, 0, 0, 0, 1, 0])
    rand_bitsA = np.random.randint(2, size=256)
    rand_bitsB = np.random.randint(2, size=256)
    Vote_A = np.append(rand_bitsA, A)
    Vote_B = np.append(rand_bitsB, B)
    sA = [str(i) for i in Vote_A]
    resA = str("".join(sA))
    sB = [str(j) for j in Vote_B]
    resB = str("".join(sB))
    #print("\nRandom bit A:\n", resA)
    #print("\nRandom bit B:\n", resB)
    #print("Random code sequence for A:\n", Vote_A)
    #print("Random code sequence for B:\n", Vote_B)
    secret_vote = input("Please enter your desired candidate 'a' or 'b':")
    if (secret_vote == ( 'a')):
        m1=hashlib.sha256()
        m1.update(resA.encode('utf-8'))
        print("Your private Key (V):\n{}".format(resA))
        print("Your digested public Key (T):\n{}".format(m1.hexdigest()))
        print("Please copy down the information.")
        f = open("Public_Key.txt", "w")
        f.write(m1.hexdigest())
        f.close()
    elif (secret_vote == ('b')):
        m2=hashlib.sha256()
        m2.update(resB.encode('utf-8'))
        print("Your private Key (V):\n{}".format(resB))
        print("Your digested public Key (T):\n{}".format(m2.hexdigest()))
        print("Please copy down the information.")
        f=open("Public_Key.txt","w")
        f.write(m2.hexdigest())
        f.close()
    elif (secret_vote != ('A' and 'B')):
        print("Invalid Vote.")
def choose():
    print("\nWelcome to SHA256 E-voting System!")
    choice = input("1.To casting a Vote enter (1)\n2.To retriving a Vote enter (2)\n                               :")
    if (choice == '1'):
        casting_vote()
    elif (choice == '2'):
        retriving_vote()
    elif (choice != ('2' or '1')):
        print("Invalid input, please try again")
        choose()

if __name__ == "__main__":
    choose()

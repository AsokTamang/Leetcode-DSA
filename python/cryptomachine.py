def enigma():
    keys='abcdefghijklmnopqrstuvwxyz !'  #here we are making a key with abcdefghijklmnopqrstuvwxyz(space)!
    values=keys[-1] + keys[0:-1]   #here the values variable store the keys last word and the words from the beginning to the second last word
    encode=dict(zip(keys,values))
    decode={value:key for key,value in encode.items()}  #here we are just flipping the key and value from pair1 and we must use .items() while we are using the key-value of dict
    msg=input('Enter your secret message: ')
    ask=input('Wanna encode(e) or decode(d)?')
    if(ask=='e'):
        new_msg=''.join([encode[letter] for letter in msg])  #then for encoding we are passing each letters of our word 
    elif (ask=='d'):
        new_msg=''.join([decode[letter] for letter in msg])    #then for decoding also we are passing each letters of our word 
    print (new_msg)

enigma()    
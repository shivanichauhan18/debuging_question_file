def encrypt():
  message = raw_input("Enter the message you want to encrypt")
  ascii_message = [ord(char)+3 for char in message]
  encrypt_message = [ chr(char) for char in ascii_message]  
  print (''.join(encrypt_message))

  
def decrypt():
  message = raw_input("Enter the message you want to decrypt ")
  ascii_message = [ord(char)-3 for char in message]
  decrypt_message = [ chr(char) for char in ascii_message]  
  print (''.join(decrypt_message))

flag = True
while flag == True:
	choice = raw_input("What do you want to do?\n 1. Encrypt a message\n 2. Decrypt a message Enter\n e or d respectively! ")
	if choice == 'e':
		encrypt() 
	elif choice == 'd':
  		decrypt()    
	
	play_again = raw_input("Do you want to try agian or Do you want to exit? (y/n) ")
	if play_again == 'y':
        	continue
	elif play_again == 'n':
        	break

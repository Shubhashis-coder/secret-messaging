# Python program to implement Morse Code Translator 
from tkinter import *
''' 
VARIABLE KEY 
'cipher' -> 'stores the morse translated form of the english string' 
'decipher' -> 'stores the english translated form of the morse string' 
'citext' -> 'stores morse code of a single character' 
'i' -> 'keeps count of the spaces between morse characters' 
'message' -> 'stores the string to be encoded or decoded' 
'''

# Dictionary representing the morse code chart 
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
					'C':'-.-.', 'D':'-..', 'E':'.', 
					'F':'..-.', 'G':'--.', 'H':'....', 
					'I':'..', 'J':'.---', 'K':'-.-', 
					'L':'.-..', 'M':'--', 'N':'-.', 
					'O':'---', 'P':'.--.', 'Q':'--.-', 
					'R':'.-.', 'S':'...', 'T':'-', 
					'U':'..-', 'V':'...-', 'W':'.--', 
					'X':'-..-', 'Y':'-.--', 'Z':'--..', 
					'1':'.----', '2':'..---', '3':'...--', 
					'4':'....-', '5':'.....', '6':'-....', 
					'7':'--...', '8':'---..', '9':'----.', 
					'0':'-----', ', ':'--..--', '.':'.-.-.-', 
					'?':'..--..', '/':'-..-.', '-':'-....-', 
					'(':'-.--.', ')':'-.--.-'} 

# Function to encrypt the string 
# according to the morse code chart 
def encrypt(message): 
	cipher = '' 
	for letter in message: 
		if letter != ' ': 

			# Looks up the dictionary and adds the 
			# correspponding morse code 
			# along with a space to separate 
			# morse codes for different characters 
			cipher += MORSE_CODE_DICT[letter] + ' '
		else: 
			# 1 space indicates different characters 
			# and 2 indicates different words 
			cipher += ' '

	return cipher 

# Function to decrypt the string 
# from morse to english 
def decrypt(message): 

	# extra space added at the end to access the 
	# last morse code 
	message += ' '

	decipher = '' 
	citext = '' 
	for letter in message: 

		# checks for space 
		if (letter != ' '): 

			# counter to keep track of space 
			i = 0

			# storing morse code of a single character 
			citext += letter 

		# in case of space 
		else: 
			# if i = 1 that indicates a new character 
			i += 1

			# if i = 2 that indicates a new word 
			if i == 2 : 

				# adding space to separate words 
				decipher += ' '
			else: 

				# accessing the keys using their values (reverse of encryption) 
				decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT 
				.values()).index(citext)] 
				citext = '' 

	return decipher 


#===============================================================================================
# import tkinter module 

def mainpage(q):
        try:
                q.destroy()
        except:
                pass
# creating root object 
        root = Tk() 

# defining size of window 
        root.geometry("12000x6000") 

# setting up the title of window 
        root.title("Message Encryption and Decryption") 
        logo = PhotoImage(file="11 (2).png")
        logo_final= Label(root,image=logo,bg='#FFFFFF',fg = "Blue").place(x=0,y=0)
        lblInfo = Label(root, font = ('algerian', 50), 
		text = "SECRET MESSAGING \n SHUBHASHIS MONDAL", 
					fg = "red",bg='black' ,bd = 10, anchor='w') 
        lblInfo.place(x= 400, y= 0) 
        rand = StringVar() 
        Msg = StringVar() 
        mode = StringVar() 
        Result = StringVar() 

        # exit function 
        def qExit(): 
                root.destroy() 

        # Function to reset the window 
        def Reset(): 
                rand.set("") 
                Msg.set("") 
                key.set("") 
                mode.set("") 
                Result.set("") 


        # reference 
        lblReference = Label(root, font = ('arial', 16, 'bold'), 
                                        text = "Name:", bd = 16, anchor = "w") 
                                        
        lblReference.place(x = 0, y =240) 

        txtReference = Entry(root, font = ('arial', 16, 'bold'), 
                                textvariable = rand, bd = 10, insertwidth = 4, 
                                                        bg = "powder blue", justify = 'right') 
                                                        
        txtReference.place(x = 150, y =240) 

        # labels 
        lblMsg = Label(root, font = ('arial', 16, 'bold'), 
                        text = "MESSAGE", bd = 16, anchor = "w") 
                        
        lblMsg.place(x = 0, y = 340) 

        txtMsg = Entry(root, font = ('arial', 26, 'bold'), 
                        textvariable = Msg, bd = 10, insertwidth = 4, 
                                        bg = "powder blue", justify = 'right') 
                                        
        txtMsg.place(x = 150, y =340) 


        lblmode = Label(root, font = ('arial', 16, 'bold'), 
                        text = "MODE(e for encrypt, d for decrypt)", 
                                                                        bd = 16, anchor = "w") 
                                                                        
        lblmode.place(x = 0, y = 445) 

        txtmode = Entry(root, font = ('arial', 10, 'bold'), 
                        textvariable = mode, bd = 10, insertwidth = 4, 
                                        bg = "powder blue", justify = 'right') 
                                                
        txtmode.place(x = 400, y = 450) 

        lblService = Label(root, font = ('arial', 16, 'bold'), 
                                text = "The \n Result-", bd = 16, anchor = "w") 
                                
        lblService.place(x = 0, y = 550) 

        txtService = Entry(root, font = ('arial', 60, 'bold'), 
                                textvariable = Result, bd = 10, insertwidth = 4, 
                                                bg = "powder blue", justify = 'right') 
                                                        
        txtService.place(x =150, y = 510) 


        def Ref(): 
                print("Message= ", (Msg.get())) 

                clear = Msg.get() 
                m = mode.get() 

                if (m == 'e'): 
                        Result.set(encrypt(clear.upper())) 
                else: 
                        Result.set(decrypt(clear.upper())) 

        # Show message button 
        btnTotal = Button(root, padx = 16, pady = 8, bd = 16, fg = "black", 
                                                        font = ('arial', 16, 'bold'), width = 10, 
                                                text = "Show Message", bg = "powder blue", 
                                                        command = Ref).place(x =200, y =650) 

        # Reset button 
        btnReset = Button(root, padx = 16, pady = 8, bd = 16, 
                                        fg = "black", font = ('arial', 16, 'bold'), 
                                                width = 10, text = "Reset", bg = "green", 
                                        command = Reset).place(x = 700, y = 650) 

        # Exit button 
        btnExit = Button(root, padx = 16, pady = 8, bd = 16, 
                                        fg = "black", font = ('arial', 10, 'bold'), 
                                                width = 5, text = "Exit", bg = "red", 
                                        command = qExit).place(x = 1430, y = 0) 

        # keeps window alive 
        root.mainloop() 
mainpage('')


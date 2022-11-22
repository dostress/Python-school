#TamarraJP3
#Programmer: Joshua Tamarra
#Email: jtamarra@cnm.edu
#Purpose: provides user capability to translate a few simple phrases in a different language

#Common Japanese phrases translated to English.

#Japanese phrases
jphrase = {

    'Konnichiwa': 'Hello',
    'Ohayogozaimasu': 'Good morning',
    'Konbanwa': 'Good evening',
    'Sayonara': 'Goodbye'
    
    }
        
#Welcome message
print("Hello! Thank you for using this Japanese to English translator.\n")

print("Which phrase would you like to translate? \n")

#Prints the list of Japanese phrases using .keys()
print(jphrase.keys())

#User input
translate = input("Translate: ")

#Output
if translate in jphrase:
    print("Your phrase in English is: " + jphrase[translate])




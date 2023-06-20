#Ill need to find what i'll need to import first.
print("i'll be there...")
player = "messiagh"
intro = """Welcome to the Threat Assessment program. This will ask a series of questions in reaguards 
to your "mental health". Please answer them truthfuly, we cannot help you otherwise"""
print(intro)
ageInput = input("Are you 80+ years old? Y/N" )
magsInput = input("Remember that infamous code?")
nGageInput = input("Have you been treated before? Y/N")

def ageGap(old_folk):
    if old_folk == "Y":
        print("You're nothing but a false idol! You'll meet the lord soon enough, count the days!")
    else:
        print("You have potential, but are you the One?")
    
def oldCode(memory):
    if memory == str(451):
        print("451... That number. A meme. The inclusion of this number is getting progressively redundant as of late. Is it a joke? It's meaningless.")
    else:
        print("You wouldn't uderstand.")
def treatHist(health):
    if health == "N":
        print("You'll need to reach out to your local physician to aquire legal documents for your mental history")
    elif health == "Y":
        print("Please exit the program")
    else:
        print("Please imput the character correctly!")
ageGap(ageInput)
oldCode(magsInput)
treatHist(nGageInput)
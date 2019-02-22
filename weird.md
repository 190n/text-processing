# # Basics 1 To start cd folder where virtual environment activate replace first_env name virtual environment `` ` source first_env / bin / activate `` ` makes sure running version python created project Honestly though step annoying skip Your project work long installed competing versions Python its packages Just figure deeper Python work 2 Create new file called ` hello.py ` put `` ` python print("Hello Python nice meet `` ` 3 Run script editor Atom ` COMMAND ` via command line ` python hello.py ` Hello Python nice meet printed screen # # # Expressions An expression set instructions computer execute Python read evaluate expressions return result For example add numbers 4 Add these numbers print results `` ` python print(1 + 1 print(10/2 print(100 6.2 70/3.5 `` ` test different expressions relate each ` = = ` tests equality  
 ` < ` less  
 ` > ` greater  
 ` < = ` less equal  
 ` > = ` greater equal  

 `` ` python print(1 = = 1 print(1 = = 2 print(1 < 2 print(5 20 > = 100/13 `` ` All these expressions evaluate either ` True ` ` False ` 5 Try evaluating few own expressions Check 1 = = 2 etc  

 # # Python sort monster calculator great working data So where focus # # # Variables store value expressions inside named variables using ` = ` symbol Notice need semi colons Hooray `` ` python x = 2 y = 5 z = x + y print(x 100 print(z `` ` 6 Store name variable print 7 Add ages everyone table print total # # # # Types Values stored variables values actually different types categories For example 1 integer 1.5 float hello string type value using ` type ` function `` ` python print(type(1 `` ` Some important types `` ` python a_number = 1 				 # integer another_number = 5.1 		 # float some_string = Hello 		 # string some_boolean = True 		 # boolean notice capitalization a_list = bunch stuff a_number some_string a_dictionary = { key1 10 key2 string } # dictionary key / value pairs `` ` In Python need declare variable types declaring variable simply type name equals sign value expression 8 Create new variable each type For example `` ` python people_at_table = 4 	         # integer sandwiches_I_ate = 1.5 		 # float best_friend = Abbas 		 # string is_raining = False 		 # boolean notice capitalization print(people_at_table `` ` 9 Create list lot array JavaScript `` ` colors = blue pink turquoise sand dark_blue = 10 27 56 random_info = people_at_table sandwiches_I_ate best_friend is_raining `` ` 10 Print stuff list `` ` print(colors[2 print(dark_blue[0 print(random_info[-1 `` ` Did notice check last element list scrolling around back -1 Yup awesome # # # Strings Strings variable type stores text To create string surround text within quotation marks matter use single double quotes long consistent 11 Create string someone name `` ` python first_name = Cardi last_name = B print(first_name print(last_name `` ` add two strings together Python combine new string 12 Add those strings `` ` python first_name = Cardi last_name = B print(first_name + last_name print(first_name + + last_name `` ` Notice add space putting quotes around empty space ----- # # # # Speaking space let rid code wrote far Highlight everything file delete From delete each code snippet before typing new million lines repetitive code # # # # Also case noticed Python code lot closer English languages might used Instead copying pasting typing code hand better Moving ----- Each character string indexed numerically access individual characters using ` ` square brackets 13 Print first second letters person name `` ` python name = Cardi B first_letter = name[0 print(first_letter second_letter = name[1 print(second_letter `` ` character index begins number 0 wish access last character use ` -1 ` second last ` -2 ` 14 Get last letter person name `` ` python name = Cardi B last_letter = name[-1 print(last_letter `` ` range characters string entering starting ending index square brackets 15 Get first three letters person name feel free use different person getting bored `` ` python name = Cardi B first_three_letters = name[0:3 print(first_three_letters `` ` To total length string use ` len ` function 16 Try How long word curious `` ` python print(len("California `` ` determine string exists within another string ` ` keyword 17 Check word inside song lyric obviously become powerful writing lyric hand patient learning process `` ` python sentence = print("do sentence print("boss sentence `` ` # # # # String methods Python lot powerful tools messing text We spend here let dive strings 18 Make string uppercase `` ` python sentence = Now here little story tell About three bad brothers well uppercase = sentence.upper print(uppercase `` ` 19 Choose lyric play these things `` ` python sentence =    STILL SEE YOUR SHADOWS IN MY ROOM    # uppercase lowercase_sentence = sentence.lower # title case titlecase_sentence = sentence.title # remove white space start end stripped = sentence.strip # replace set characters another less_poetic_sentence = sentence.replace("SHADOWS SWEATSHIRT `` ` 20 Print those results already `` ` print(lowercase_sentence print(titlecase_sentence print(stripped print(less_poetic_sentence `` ` Here full list things strings https://docs.python.org/3.7/library/stdtypes.html#string-methods](https://docs.python.org/3.7/library/stdtypes.html#string-methods # # # Lists A list numerically ordered collection values known array 21 Make empty list `` ` python # empty list dreams = `` ` 22 Add list `` ` # add our list append method dreams.append("flying dream # list look flying dream `` ` 23 Add things list `` ` # add stuff dreams.append("forgot dreams.append("saw friend long ago dreams.append(100 dreams.append("whatever `` ` 24 Print sure looks `` ` print(dreams # flying dream forgot saw friend long ago 100 whatever `` ` 25 Do stuff list `` ` # length list len(dreams # access individual items list referrring index value print dreams[0 # prints flying dream print dreams[2 # prints saw friend long ago # use negative numbers start back print dreams[-1 # prints whatever last item # access part list print(dreams[1:4 `` ` iterate through every value list ` ` keyword `` ` python item my_list 
	 print(item `` ` A normal loop JavaScript looks `` ` javascript var = 0 < 3 i++ { 
     print(i 
   } `` `  
  
 In Python different structure same thing `` ` python x range(0 3 
   print(x `` `    
 Pythonic use 4 spaces indent code inside loop function definition must # # # Reading files To open file Python use ` open ` keyword function function takes two arguments first name file open second flag states opening file intent reading use r writing use w Once opened file use ` read ` function grab contents return string In example open file store its contents string We uppercase entire file print screen `` ` python content = open("frozen_lyrics.txt r").read loud_frozen = content.upper print(loud_frozen `` ` store file list lines using ` readlines ` instead ` read ` example prints first 5 characters text file `` ` python all_lines = open("frozen_lyrics.txt r").readlines line all_lines 
	 print(line[0:5 `` ` # # Beyond Basics 


 Go online find text file exciting full text Harry Potter Sorcerer Stone here)[http://www.glozman.com / textpages.html Save file next python script We ’ll read text file store variable In our python script 

    
     text = open("harrypotter1.txt").read # name file relative where script 
    
     print(text # Outputs entire text 
    
    
 issues few troubleshooting tips Is console outputting unicode error possible characters text file scaring python Try adding command `` ` text = open("harrypotter.txt encoding="ascii errors="surrogateescape").read `` ` Is text file next .py file python ca find Try printing file path `` ` import os print os.getcwd `` ` wrong directory cd around python command line called chdir instead cd `` ` os.chdir .. `` ` Hopefully working Now stuff Count many times Harry mentioned `` ` python text = open("harry_potter_1.txt encoding="ascii errors="surrogateescape").read count = text.count("Harry print(count 
  `` ` To read every single lines Instead read use readlines 
    
     text = open("harrypotter.txt").readlines 
     # text list string items each line file 
    

 Now iterate over lines 
   
     line text 
       print(line # Outputs each line 
      

 problem ’s putting space between each line ’s extra character after line break called newline character We rid strip 

    
     line text 
       line = line.strip 
       print(line # Outputs each line without whitespace extra line breaks 
 

 Each lines string print parts each line 
    
     line text 
       line = line.strip 
       print(line[0:4 
    
     # Output first four characters each line 
    

 Or fun stuff replacing 
   
     line text 
       line = line.strip 
       print(line.replace('e eeeeeee 
      

 # # Processing text We ’re gon na use function called split break downs string according delimiter character use split return string list separated character use join join list back string 

    
     line text 
       line = line.strip 
       words = line.split ") # Separates lines empty space getting list words 
      
       print(words[0 # Outputs first word each sentence 
      
       # Chain together 
       print(words[0].center(30 ~').upper 
      

 We use random methods interesting stuff Sometimes tell python add modules import keyword add functionality need Here ’ll import random module](https://docs.python.org/3.5/library / random.html Use documentation find module Make sure ’re seeing documentation python version ’re using e.g. 3.5 # Import module `` ` python    
     import random 
    
     text = open("harrypotter.txt").readlines 
    
     line text 
       line = line.strip 
       words = line.split ") 
      
       random_word = random.choice(words # Get random item word list 
      
       random.shuffle(words # Randomizes order items list `` `    


 We use join method join randomized word list string 

    
    
     line text 
       line = line.strip 
       words = line.split ") 
       random.shuffle(words 
      
       new_line = .join(words # Joins each element list sticking space character between words outputs string 
      
 We sort sorted 
    
     line text 
       line = line.strip 
       words = line.split ") 
       random.shuffle(words 
      
       words = sorted(words # Sort words list alphabetically 
      
       new_line = .join(words 
      

 Final script 

     # Import module 
     import random 
    
     text = open("harrypotter.txt").readlines 
     line text 
       line = line.strip 
       words = line.split ") 
       random.shuffle(words 
       words = sorted(words 
       new_line = .join(words 
       print(new_line 


 # # List comprehension Make new file comps.py 


 We list upper case’d items 

     names = Hermione Harry Ron Dumbledore 
    
     uppercase_names = 
     name names 
       uppercase_names.append(name.upper 
    
    

 There ’s handier doing python called list comprehension same thing example above 

     names = Hermione Harry Ron Dumbledore 
    
     uppercase_names = name.upper name names 
    

 ’s saying every value list names temporarily store variable name upper case store new list called uppercase_names 


    
     names = name.replace('r arrrrr name names 
    

 We filter adding statements inside 

    
     names = name name names name[0 = = l 
     # returns elements inside list whose first letter l 
    


 We add filtering technique words our previous example 

     import random 
    
     text = open("harrypotter.txt").readlines 
     line text 
       line = line.strip 
       words = line.split ") 
    
       words = word word words word.startswith("a 
    
       new_line = .join(words 
        
       print(new_line 
       # prints words start  

 OR 

       words = word word words len(word > 5 
       # words 5 characters 


       words = word word words word.endswith("ing 
       # words end ing # # # Ready interesting these skills # # # # Creative Mathy assigments located Python Puzzles](https://github.com / lizzybrooks / python possible / blob / master/5-python puzzles.mdf page 

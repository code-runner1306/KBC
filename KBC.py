import random
questions=[["Current Railway Minister of India is:","Mamta Banarjee","Ram Vilash,Ashwini Vaishnaw", "Piyush Goyal"] ,["Which god is also known as ‘Gauri Nandan'?","Agni","Indra","Hanuman","Ganesha"],["What does not grow on tree according to a popular Hindi saying?","Money","Flowers","Leaves","Fruits"],["Which city is known as Pink City in India?","Banglore","Mysore","Jaipur","Kochi"],["Who wrote Indias National Anthem?","Rabindranath Tagore","Lal Bahadur Shastri","Chetan Bhagat","RK Narayan"],
           ["How many religions are there in India?","6","7","8","9"],["When is the National Hindi Diwas celebrated?","13 September","14 September","14 July","15 August"],["How many states are there in India?","28","29","30","31"],["Where in India Gate located?","Agra","Punjab","Mumbai","New Delhi"],["Who wrote Vande Mataram?","Sarat Chandra Chattopadhyay","Rabindranath Tagore","Bankim Chandra Chatterjee","Ishwar Chandra Vidyasagar"],
           [" Which one of the following places is famous for the Great Vishnu Temple?","Bordubar, Indonesia","Bamiyan, Afghanistan","Panja Sahib, Pakistan","Ankorvat, Cambodia"],["The largest Buddhist Monastery in India is located at:","Sarnath, Uttar Pradesh","Tawang, Arunachal Pradesh","Dharmashala, Himachal Pradesh","Gangtok, Sikkim"],["Which of the following musical instruments is NOT of foreign origin?","Tabla","Flute","Sitar","Violin"],["Who among the following was killed during 'Operation Bluestar' of 1984?","Baba Santa Singh","Haji Mastan","Jarnail Singh Bhindrawale","Homi Jehangir Bhabha"],["Which former Indian President died as a result of a road accident?","Rajendra Prasad","Faqruddin Ali Ahmed","Giani Zail Singh","R.Venkatraman"],
           ["Who is the founder of the political party Dravida Munnetra Kazhagam (DMK)?","C.N. Annadurai","M. Karunanidhi","M.G. Ramachandran","Jayalalitha"],["Who was the first Indian woman to win a medal in the Olympics?","P.T. Usha","Kunjarani Devi","Bachendri Pal","Karnam Maleshwari"],["Which Mughal Emperor was deported to Rangoon by the British?","Shah Jahan","Bahadur Shah II","Akbar Shah I","Bahadur Shah I"],["Which of the following is not a state of India?","Vrindachal","Goa","Jharkhand","Chattisgarh"],["Who among the following is said to have witnessed the reigns of eight Delhi Sultans?","Minhaj-us-Siraj","Ziauddin Barani","Amir Khusro","Shams-i-Siraj Afif"],
           ["The fine step-well complex of 'Agrasen ki Baoli' is located at","Gwalior","Amritsar","Agra","New Delhi"],["The National Stadium in Delhi was earlier known by the name","Irwin Stadium","Mountbatten Stadium","Wellington Stadium","Canning Stadium"],["Which James Bond movie was shot in the Indian city of Udaipur?","Diamonds Are Forever","License to Kill","Live and Let Die","Octopussy"],["Which Indian city hosts Indian movie industry?","Goa","Mumbai","Chennai","Calcutta"],["Which city is known as the 'Silicon Valley Of India'?","Delhi","Mumbai","Chennai","Bangalore"],
           ["How do you say Hello in India?","Neeche","Ladki","Namaste","Chor"],["Taj Mahal was made of ","Brick","Marble","Granite","Sandstone"],["The International Literacy Day is observed on","Sep 8","Nov 28","May 2","Sep 22"],["Which day is observed as the World Standards  Day?","June 26","Oct 14","Nov 15","Dec 2"],["The language of Lakshadweep. a Union Territory of India, is","Tamil","Hindi","Malayalam","Telugu"],
           ["Which of the following was the theme of the World Red Cross and Red Crescent Day?","Dignity for all - focus on women","Dignity for all - focus on Children","Focus on health for all","Nourishment for all-focus on children"],["September 27 is celebrated every year as","Teachers' Day","National Integration Day","World Tourism Day","International Literacy Day"],["Who is the author of 'Manas Ka-Hans' ?","Khushwant Singh","Prem Chand","Jayashankar Prasad","Amrit Lal Nagar"],["The death anniversary of which of the following leaders is observed as Martyrs' Day?","Smt. Indira Gandhi","PI. Jawaharlal Nehru","Mahatma Gandhi","Lal Bahadur Shastri"],["Who is the author of the epic 'Meghdoot'?","Vishakadatta","Valmiki","Banabhatta","Kalidas"],
           ["Good Friday' is observed to commemorate the event of","birth of Jesus Christ","birth of St. Peter","crucification of Jesus Christ","rebirth of Jesus Christ"],["Who is the author of the book 'Amrit Ki Ore'?","Mukesh Kumar","Narendra Mohan","Upendra Nath","Nirad C. Choudhary"],["Which of the following is observed as Sports Day every year?","22nd April","26th  july","29th August","2nd October"],["World Health Day is observed on","Apr 7","Mar 6","Mat 15","Apr 28"],["Pongal is a popular festival of which state?","Karnataka","Kerala","Tamil Nadu","Andhra Pradesh"],
           ["Ghototkach in Mahabharat was the son of","Duryodhana","Arjuna","Yudhishthir","Bhima"],["Which of the following Muslim festivals is based on the 'Holy Quran' ?","Id -ul-Zuha","Id -ul-Fitr","Bakri-id","Moharram"],["Van Mahotsav was started by","Maharshi Karve","Bal Gangadhar Tiiak","K.M, Munshi","Sanjay Gandhi"],["The first month of the Indian national calendar is","Magha","Chaitra","Ashadha","Vaishakha"],["Which of the following is not a dance from Kerala?","Kathakali","Mohiniattam","Ottan Thullal","Yaksha Gana"],
           ["The festival of Nabanna is celebrated predominatly in","Andhra Pradesh","Rajasthan","Karnataka","Orissa"],["Rath Yatra is famous festival at","Ayodhya","Mathura","Dwaraka","Puri"],["Onam is the main festival of","Tamil Nadu","Karnataka","Andhra Pradesh","Kerala"],["The Lalit Kala Academy is devoted to the promotion of","Dance & Drama","Fine Arts","Literature","Music"],["Which one of the following is essentially a solo dance? ","Kuchipudi","Kathak","Manipuri","Mohiniattam"]]
answers=["C","D","A","C","A","A","B","A","D","C","D","B","B","C","C","A","D","B","A","C","D","A","D","B","D","C","B","A","B","C","B","C","D","C","D","C","B","C","A","C","D","A","C","B","D","D","D","D","B","D"]
earn=["₹1,000/-","₹2,000/-","₹3,000/-","₹5,000/-","₹10,000/-","₹20,000/-","₹40,000/-","₹80,000/-","₹1,60,000/-","₹3,20,000/-","₹6,40,000/-","₹12,50,000/-","₹25,00,000/-","₹50,00,000","₹75,00,000/-","₹1,00,00,000/-","₹7,50,00,000/-"]
earnings=0
count=0
numset=set()
while(len(numset)!=17):
    i=int(random.randint(0,len(questions)-1))
    numset.add(i)
for _ in numset:
    print("To earn rupees: ",earn[count])
    print(f"{questions[i][0]} \n A. {questions[i][1]}           B. {questions[i][2]} \n C. {questions[i][3]}           D. {questions[i][4]}")
    ans=str(input("Enter the option: "))
    if(ans==answers[i]):
        print("Correct answer \n Total earnings: ",earn[count])
        count+=1
        if(count==16):
            earnings="₹7,50,00,000/-"
            print("Congratulations! You have earned ",earnings)
            break
        elif(count==14):
            earnings="₹75,00,000/-"
            cont=input("Would you like to quit? (yes or no) ")
            if(cont=='yes'):
                break
        elif(count==9):
            earnings="₹3,20,000/-"
            cont=input("Would you like to quit? (yes or no) ")
            if(cont=='yes'):
                break
        elif(count==4):
            earnings="₹10,000/-"
            cont=input("Would you like to quit? (yes or no) ")
            if(cont=='yes'):
                break
    else:
        print("Wrong answer. Try again next time")
        print("Congratulations! You have earned ",earnings)
        break
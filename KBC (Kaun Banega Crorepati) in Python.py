import random

questions = [
    [
    "Which language was used to create facebook?", "Python", "JavaScript", "Java", "Php", "None", 4
    ],

    [
    "When was google founded?", "1999", "1998", "1997", "1995", "None", 1
    ],

    [
    "What is the name of the company that made facebook?", "Meta", "Google", "Microsoft", "None", "None", 1
    ],

    [
    "Who founded Microsoft?", "Paul Allen", "Steve Jobs", "Tim Cook", "Bill Gates", "None", 4
    ],

    [
    "when apple launched its first smartphone?", "2000", "2007", "2010", "2005", "None", 2
    ],

    [
    "When first Pixel phone was launched?", "2016", "2015", "2020", "2012", "None", 1
    ],

    [
    "Which language was used to create Instagram?",
    "Python", "Java", "French", "Php", "None", 1
    ],

    [
    "When Amazon was founded?", "1994", "1998", "1997", "1995", "None", 1
    ],

    [
    "Who founded Amazon?", "Sundar Pichai", "Jeff Bezos", "Bill Gates", "Elon Musk", "None", 2
    ],

    [
    "Who founded Tesla?", "Martin Eberhard and Marc Tarpenning", "Elon Musk and Mark Zuckerberg", "Bill Gates and Jeff Bezos", "Ambani and Adani", "None", 1
    ],

    [
    "When Tesla was founded?", "2001", "2005", "2003", "2004", "None", 3
    ],

    [
    "Who founded Tata?", "Ratan Tata", "Jamsetji Tata", "Ratanji Tata", "J.R.D. Tata", "None", 2
    ],

    [
    "When Tata was founded?", "1885", "1865", "1869", "1868", "None", 4
    ],

    [
    "When Samsung was founded?", "1965", "1968", "1969", "1970", 3
    ],

    [
    "Who founded Jio?", "Muskesh Ambani", "Anil Ambani", "Gautam Adani", "Bill Gates", 1
    ],

]

random.shuffle(questions)

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]
money = 0
for i in range(0, len(questions)):

    question = questions[i]
    print(f"Question for Rs. {levels[i]} \n")
    print(f"{question[0]}")
    print(f"a.{question[1]}      b.{question[2]} ")
    print(f"c.{question[3]}      d.{question[4]} ")
    reply = int(input("Enter Your Answer (1-4) or 0 to quit "))


    if (reply == 0):
        money = levels[i-1]
        break

    
    if (reply == question[-1]):
        print(f"Correct answer, you have won Rs. {levels[i]}\n")

        if(i == 4):
            money = 10000
        elif(i == 9):
            money = 320000
        elif(i == 14):
            money = 10000000

    else:
        print("Wrong answer!")
        break

print(f"Your take home money is Rs. {money}")
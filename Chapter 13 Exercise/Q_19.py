"""Write a function called verbose that, given an integer less than 1015, returns the name of
the integer in English. As an example, verbose(123456) should return one hundred
twenty-three thousand, four hundred fifty-six."""



def verbose(num):
    d ={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",
        11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fiftheen",16:"sixteen",17:"seventeen",18:"eighteen",
        19:"nineteen",20:"twenty",30:"30",40:"fourty",50:"fifthy",60:"sixty",70:"Seventy",80:"eighty",90:"Ninety"}

    if num <20:
       return d[num]

    if num <100 :
        if num % 10 == 0:
            return d[num]
        else:
            return d[num //10 * 10] + verbose(num % 10)

    if num < 10 **3:
       if num % 100 == 0:
          return d[num] + "hundred"
       else:
           return d[num//100] + "hundred and " + verbose(num % 100)

    if num < 10 **6:
       if num % 10**3 == 0:
          return verbose(num) + "Thousand"

       else:
          return verbose(num//10**3)+ "Thousand " + verbose(num % 10**3)

    if num < 10 ** 9:
       if num % 10 **6 == 0:
          return verbose(num//10**6) + "Million"
       else:
           return verbose(num // 10**6) + " Million " + verbose(num % 10**6)








print(verbose(123456))
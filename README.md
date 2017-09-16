# randomNumberGenerator
This random number generator is a pseudorandom number generator which is basedon linear congruential generator.
Which uses the given mathematical formula:-
    Sn+1=(a*Sn+c)mod m
    Where a, m and c are fixed integers.
    Sn+1 is the next integer generated in the series which is generated using a fixed number Sn known as seed.

So this formula gives numbers in the range 0 to m-1.
so that we can generate number in a large range.

In our program we used time() function to set the value of see. We can also set any random value to a but it will
give evry time the same series of numbers So i used time() function.

In our random_number(first,last,count):- 
3 parameters first,last, count are passed to the function. As first is the starting point and last is ending point
of our range and count is the number of random numbers.

Now this random_number() algorithm should be 73% biased to the higher number. So we set one variable c1 to 0.27 of "count".
c1 = int(0.27*count) is used to make it an integer and i consider the lower value(when c1 is not multiple of 100).
variable var is set to zero which is used to count number which we store in list and at the end will be equal to "count" variable.
variable lower and upper are set to zero which are used to count numbers less than middle value and higher than middle value.

Now a while loop is used 
        s=(a*s+c)%m
        m is set to large integer so it will produce numbers(s) in a large range.
        temp=s%last
        but some times s is out of user's range so we perform modulus operation to set it less than end value and sometimes
        temp is less than starting value so we add starting value to temp to set it in range if it is lesser than starting value.
        if temp < start:
            temp=temp+start
            
value of temp is added to a list "values" when the the condition satisfies.
To add a value to list it should satisfy one of two condition.
      1. variable left should be lesser than c1 and value of temp should be less than or equal to mid value.
      (left will increase by 1 if this condition satisfy)
      2.variable right should be lesser than value of "count"-c1 and value of temp should be higher than mid value.
      (right will increase by 1 if this condition satisfies)
      
      variable var increase by 1 in any of condition satisfy.
while loop terminates when both the conditions are false.(left greater than c1 and right greater than count-c1)


random_number() function returns a list of random values which are 73% bias to higher values.


        
       

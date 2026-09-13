num = int(input("enter a number:"))
original=num
reverse = 0
while num > 0:
     digit = num%10
     reverse = reverse*10 + digit
     num//=10
if original == reverse:
     print("its palindrome......")
else:
     print("its not palindrome......")
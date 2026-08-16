par = input("Enter the bracket: ")
lis = ['(', ')', '{', '}', '[', ']']
if "()" == par:
    print(True)
elif "[]" == par:
    print(True)
elif "{}" == par:
    print(True)
elif "{}[]()" == num or "(){}[]" == num or "{}()[]" == num or "()[]{}" == num or "[](){}" == num or
    "[]{}()" == num or "(){}[]" == num:
    print(True)
           
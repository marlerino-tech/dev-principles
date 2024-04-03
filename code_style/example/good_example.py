# ruff: noqa: D100 D103

def number_operations(num1, num2, num3):
    if num1 > num2:
        print(num1, "is greater than", num2)
    else:
        print(num2, "is greater or equal to", num1)

    for i in range(0, num3):
        print("Number:", i)
    list_example = [1, 2, 3, 4]
    if list_example[0] == 1:
        list_example[0] = "one"
    elif list_example[0] == "1":
        list_example[0] = "one"
    return (
        num3 + num1 - num2
    )

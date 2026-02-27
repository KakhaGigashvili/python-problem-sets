expression = input("Expression: ")

x, y, z = expression.split()

x = int(x)
z = int(z)

match y:
    case "+":
        answer = x + z
    case "-":
        answer = x - z
    case "*":
        answer = x * z
    case "/":
        answer = x / z

print(f"{answer:.1f}")
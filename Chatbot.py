import datetime
import json
import os
import ast
import operator

FILE_NAME = "learned_responses.json"

DEFAULT_RESPONSES = {
    "hello": "Hi! How can I help you?",
    "hi": "Hello! Nice to meet you.",
    "how are you": "I am doing great. Thank you!",
    "who are you": "I am a rule-based Python chatbot.",
    "motivate me": "Keep going! Every bug makes you a better developer.",
    "happy": "Great to hear that!",
    "sad": "I hope things get better. Keep going!",
    "thank you": "You're welcome!",
    "your name": "I am your Python Rule-Based Chatbot."
}


def load_responses():
    if not os.path.exists(FILE_NAME):
        return DEFAULT_RESPONSES.copy()

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, dict):
            responses = DEFAULT_RESPONSES.copy()
            responses.update(data)
            return responses

    except (json.JSONDecodeError, OSError):
        pass

    return DEFAULT_RESPONSES.copy()


def save_responses(responses):
    try:
        custom_responses = {
            key: value for key, value in responses.items()
            if key not in DEFAULT_RESPONSES
        }

        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(custom_responses, file, indent=4)

    except OSError:
        print("Bot: Unable to save the new response.")


def get_greeting(name):
    hour = datetime.datetime.now().hour

    if 5 <= hour < 12:
        greeting = "Good Morning"
    elif 12 <= hour < 17:
        greeting = "Good Afternoon"
    elif 17 <= hour < 21:
        greeting = "Good Evening"
    else:
        greeting = "Good Night"

    return f"{greeting}, {name}!"


def calculate(expression):
    operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv
    }

    try:
        tree = ast.parse(expression, mode="eval")

        def solve(node):
            if isinstance(node, ast.Expression):
                return solve(node.body)

            if isinstance(node, ast.Constant):
                if isinstance(node.value, (int, float)):
                    return node.value
                raise ValueError

            if isinstance(node, ast.BinOp):
                operation = operators.get(type(node.op))
                if operation is None:
                    raise ValueError
                return operation(solve(node.left), solve(node.right))

            raise ValueError

        return solve(tree)

    except (ValueError, SyntaxError, ZeroDivisionError):
        return None


def get_response(user_input, responses):
    user_input = user_input.lower().strip()

    for keyword, response in responses.items():
        if keyword in user_input:
            return response

    return None


def main():
    responses = load_responses()

    print("=" * 50)
    print("       PYTHON RULE-BASED AI CHATBOT")
    print("=" * 50)

    name = input("Please enter your name: ").strip()

    if not name:
        name = "User"

    print(get_greeting(name))

    print("\nNamaste! Welcome to your chatbot.")
    print("Type 'help' to see available commands.")
    print("Type 'bye' to exit.")

    while True:
        user_input = input("\nYou: ").strip()

        if not user_input:
            print("Bot: Please type something.")
            continue

        command = user_input.lower()

        if command in ["bye", "exit", "quit"]:
            print(f"Bot: Goodbye {name}! Have a great day!")
            break

        elif command == "help":
            print("\nBot: Available commands:")
            print("- time")
            print("- date")
            print("- calculator")
            print("- basic questions")
            print("- bye / exit / quit")

        elif command == "time":
            current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
            print("Bot: Current time is", current_time)

        elif command == "date":
            current_date = datetime.datetime.now().strftime("%d-%m-%Y")
            print("Bot: Today's date is", current_date)

        elif command == "calculator":
            expression = input("Enter calculation (example: 10 + 5): ")
            result = calculate(expression)

            if result is None:
                print("Bot: Invalid calculation.")
            else:
                print("Bot: Result =", result)

        else:
            reply = get_response(user_input, responses)

            if reply:
                print("Bot:", reply)

            else:
                print("Bot: I don't know the answer to that yet.")

                learn = input(
                    "Would you like to teach me a response? (yes/no): "
                ).lower()

                if learn == "yes":
                    new_response = input("What should I reply? ").strip()

                    if new_response:
                        responses[user_input.lower()] = new_response
                        save_responses(responses)
                        print("Bot: Thanks! I learned a new response.")


if __name__ == "__main__":
    main()
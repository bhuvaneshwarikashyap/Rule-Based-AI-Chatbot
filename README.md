🤖 Rule-Based AI Chatbot

A simple and interactive Rule-Based AI Chatbot built with Python.
The chatbot can respond to basic questions, provide date and time, perform safe arithmetic calculations, and learn new responses from the user.

✨ Features

- 👋 Personalized time-based greeting
- 💬 Rule-based conversation using keyword matching
- 🧠 Learns new responses and saves them locally
- 📅 Shows the current date
- 🕐 Shows the current time
- 🧮 Safe basic calculator
- ❓ Help command
- 🚪 Exit command
- ⚠️ Handles invalid and empty inputs
- 💾 Stores learned responses using JSON

🛠️ Technologies Used

- Python
- JSON
- File Handling
- Functions
- Dictionaries
- Loops & Conditional Statements
- Exception Handling
- AST-based expression parsing

📂 Project Structure

python-rule-based-chatbot/
│
├── chatbot.py
└── README.md

«"learned_responses.json" is created automatically when the chatbot learns a new response. It is stored locally and is not required to be uploaded to the public repository.»

▶️ How to Run

Make sure Python is installed on your system.

Run the following command:

python chatbot.py

💬 Example Commands

hello
how are you
motivate me
time
date
calculator
help
bye

📷 Sample Output

The chatbot starts with a personalized greeting and provides a menu of available commands.

==================================================
       PYTHON RULE-BASED AI CHATBOT
==================================================

Please enter your name: Bhuvi
Good Afternoon, Bhuvi!

Namaste! Welcome to your chatbot.
Type 'help' to see available commands.
Type 'bye' to exit.

You: hello
Bot: Hi! How can I help you?

You: time
Bot: Current time is 04:30:25 PM

You: calculator
Enter calculation (example: 10 + 5): 25 + 15
Bot: Result = 40

You: bye
Bot: Goodbye Bhuvi! Have a great day!

🧠 How It Works

The chatbot checks the user's message against predefined keywords and returns the corresponding response.

If it does not recognize the input, the user can teach it a new response. The new response is stored locally in a JSON file and can be used in future sessions.

🔮 Future Improvements

- Graphical User Interface (GUI)
- Voice input and output
- More conversation categories
- Sentiment-based responses
- Chat history
- Web-based interface
- Database integration

👩‍💻 Author

Bhuvaneshwari Kashyap

Built as a Python learning and portfolio project.
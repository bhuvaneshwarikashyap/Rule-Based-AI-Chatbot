🤖 Rule-Based AI Chatbot

A simple and interactive rule-based chatbot built with Python.
It can respond to basic questions, provide date and time, perform basic calculations, and learn new responses from the user.

✨ Features

- 👋 Personalized time-based greeting
- 💬 Keyword-based responses
- 🧠 Learns new responses
- 💾 Saves learned responses locally using JSON
- 📅 Current date
- 🕐 Current time
- 🧮 Safe basic calculator
- ❓ Help command
- 🚪 Exit command
- ⚠️ Handles invalid and empty inputs

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

Rule-Based-AI-Chatbot/
│
├── Chatbot.py
└── README.md

«"learned_responses.json" is created automatically when the chatbot learns a new response. It is stored locally.»

▶️ How to Run

Make sure Python is installed on your system.

python Chatbot.py

💬 Example

Please enter your name: Bhuvi
Good Evening, Bhuvi!

Namaste! Welcome to your chatbot.

You: hello
Bot: Hi! How can I help you?

You: time
Bot: Current time is 06:30:15 PM

You: calculator
Enter calculation (example: 10 + 5): 25 + 15
Bot: Result = 40

You: bye
Bot: Goodbye Bhuvi! Have a great day!

🧠 How It Works

The chatbot uses keyword matching to find a suitable response for the user's message.

If no matching response is found, the user can teach the chatbot a new response. The learned response is stored locally in a JSON file.

🔮 Future Improvements

- GUI interface
- Voice input and output
- Chat history
- More conversation categories
- Sentiment-based responses
- Web-based interface
- Database integration

👩‍💻 Author

Bhuvaneshwari Kashyap

Built as a Python learning and portfolio project.
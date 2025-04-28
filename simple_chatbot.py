>>> def simple_chatbot(user_query):
...     # Convert user input to lowercase and strip extra spaces
...     user_query = user_query.strip().lower()
... 
...     # Predefined queries with simple responses
...     if user_query == "what is the total revenue?":
...         return "The total revenue is [amount]."
...     elif user_query == "how has net income changed over the last year?":
...         return "The net income has [increased/decreased] by [amount] over t\
he last year."
...     elif user_query == "what is the total revenue for apple?":
...         return "The total revenue for Apple is 391035000000."
...     elif user_query == "what is the net income for microsoft in 2023?":
...         return "The net income for Microsoft in 2023 is 72361000000."
...     # Add more conditions for other predefined queries
...     else:
...         return "Sorry, I can only provide information on predefined queries\
."
... 
... # Test the chatbot
... if __name__ == "__main__":
...     print("Chatbot: Hello! Ask me a financial question.")
...     while True:
...         user_input = input("You: ")
...         if user_input.lower() == "exit":
...             print("Chatbot: Goodbye!")
...             break
...         print("Chatbot:", simple_chatbot(user_input))
... 
Chatbot: Hello! Ask me a financial question.
You: What is the net income for Microsoft in 2023?
Chatbot: The net income for Microsoft in 2023 is 72361000000.
You: What is the total revenue for Apple?
Chatbot: The total revenue for Apple is 391035000000.
You: What is the net income for Microsoft in 2023?
Chatbot: The net income for Microsoft in 2023 is 72361000000.


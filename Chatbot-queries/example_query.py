# Based on https://beta.openai.com/docs/quickstart

import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def main():
    query = input("Type a query: ")
    while query != "" and query != "exit":
        response = openai.Completion.create(
                model="text-davinci-003",
                prompt=query,
                # Randomness?
                temperature=0.6,
            )
        print("Chat response: ", response.choices[0].text)
        query = input("Your Respone: ")
    
    print("Thank you for chatting!")

    return 0

if __name__ == "__main__":
    main()
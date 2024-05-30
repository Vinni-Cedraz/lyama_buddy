import os
import time
import sys
import threading
from groq import Groq
from termcolor import colored
from art import text2art
from rich.console import Console
from rich.markdown import Markdown


ascii = """ \\/
<'l
 ll
 llama~
 || ||
 '' ''"""


class LoadingAnimation(threading.Thread):
    """Simple loading animation"""

    def __init__(self):
        super().__init__()
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            for char in "|/-\\":
                sys.stdout.write("\r" + char)
                time.sleep(0.1)
                sys.stdout.flush()
        sys.stdout.write("\r ")

    def stop(self):
        self.running = False


def main():
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

    os.system("clear")
    print(text2art("Speedy Lyama Chat"))  # ASCII art
    print(ascii)
    while True:
        user_input = input(colored("$> ", "green"))
        if user_input.lower() == "exit":
            break

        loading_animation = LoadingAnimation()
        loading_animation.start()

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": user_input
                    + "keep your answer veryy short whenever possible",
                }
            ],
            model="llama3-70b-8192",
        )

        loading_animation.stop()
        loading_animation.join()

        os.system("clear")
        print(ascii)
        Console().print("[cyan]You: [/cyan]\n" + user_input)
        Console().print("[cyan]Bot: [/cyan]")
        Console().print(Markdown(chat_completion.choices[0].message.content))


if __name__ == "__main__":
    main()

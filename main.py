import threading
import queue
import time
import kwairylite

class ChatWithLLM:
    def __init__(self):
        self.query_queue = queue.Queue()
        self.stop_event = threading.Event()
        self.kwairy = kwairylite.KwairyLite()
        self.agent = self.kwairy.getSQLagent()

    def call_llm_function(self, query):
        """function for LLM processing."""
        response = self.agent.run(query)
        return f"Kwairy:\n ---> {response}"

    def llm_thread(self):
        """Thread function that processes queries and prints the LLM's response."""
        while not self.stop_event.is_set():
            if not self.query_queue.empty():
                query = self.query_queue.get()
                response = self.call_llm_function(query)
                print(f"\nYou: {query} \n")
                print(f"{response}\n")
                self.query_queue.task_done()
            else:
                time.sleep(0.5)

    def user_input_thread(self):
        """Thread function to get user input."""
        print("Enter your query. Type 'EXIT' to stop.")
        while not self.stop_event.is_set():
            try:
                user_input = input("You: ").strip()
                if not user_input:  # Check for empty input
                    print("Please enter a query.")
                    continue
                if user_input == 'EXIT':
                    self.stop_event.set()
                    break
                self.query_queue.put(user_input)
            except (KeyboardInterrupt, EOFError):
                # Handle keyboard interrupts gracefully
                print("\nReceived interrupt. Exiting...")
                self.stop_event.set()
                break

    def start(self):
        """Starts the CLI interface and the LLM processing thread."""
        llm_worker = threading.Thread(target=self.llm_thread)
        input_worker = threading.Thread(target=self.user_input_thread)

        try:
            llm_worker.start()
            input_worker.start()

            input_worker.join()
            llm_worker.join()
            print("Exiting... Processed all queries.")
        except Exception as e:
            # Catching any unforeseen exceptions
            print(f"Error occurred: {e}")
            self.stop_event.set()
            input_worker.join()
            llm_worker.join()



import time

class ChatWithLLM2:
    def __init__(self):
        self.query_queue = queue.Queue()
        self.stop_event = threading.Event()
        self.kwairy = kwairylite.KwairyLite()
        self.agent = self.kwairy.getSQLagent()

    def placeholder_llm_function(self, query):
        """Placeholder function to simulate LLM processing."""
        print(f"\nYou:> {query} \n")
        response = self.agent.run(query)
        return f"{response}"

    def start(self):
        """Starts the CLI interface."""
        print("Ready to formulate SQL queries. Type 'EXIT' to stop.")
        while True:
            try:
                user_input = input("You: ").strip()
                if not user_input:  # Check for empty input
                    print("Please enter a valid query.")
                    continue
                if user_input == 'EXIT':
                    break
                response = self.placeholder_llm_function(user_input)
                print(f"Kwairy:> {response}\n")
            except (KeyboardInterrupt, EOFError):
                # Handle keyboard interrupts gracefully
                print("\nReceived interrupt. Exiting...")
                break



if __name__ == "__main__":
    chat = ChatWithLLM2()
    chat.start()




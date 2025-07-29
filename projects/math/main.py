from agent import run_agent

def main():
    print("Welcome to the Math Assistant Agent!")
    user_input = input("Enter your math question: ")
    
    result = run_agent(user_input)
    print(f"\nFinal Answer: {result}")

if __name__ == "__main__":
    main()

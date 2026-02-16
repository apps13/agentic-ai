from tools.multiply import multiply

def run_agent(prompt: str) -> str:
    print(f"\nQuestion: {prompt}")

    # Very simple parse: extract 2 numbers from the prompt
    numbers = [int(word) for word in prompt.split() if word.isdigit()]
    
    if len(numbers) != 2:
        return "I can only handle prompts with exactly 2 numbers for now."

    x, y = numbers
    print(f"\nThought: I need to multiply {x} by {y}.")
    result = multiply(f"{x} {y}")
    print(f"Observation: {result}")

    return result

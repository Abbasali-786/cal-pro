import streamlit as st

def main():
    st.title("Simple Calculator")

    # Input fields for user to enter numbers
    num1 = st.number_input("Enter the first number:", value=0.0)
    num2 = st.number_input("Enter the second number:", value=0.0)

    # Operation selection (addition, subtraction, multiplication, division)
    operation = st.selectbox("Select an operation:", ["Add", "Subtract", "Multiply", "Divide"])

    # Perform the selected operation
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero"

    # Display the result
    st.write(f"Result: {result}")

if __name__ == "__main__":
    main()

import streamlit as st

# Title
st.set_page_config(page_title="Calculator App", page_icon="🧮")
st.title("🧮 Simple Calculator")
st.write("Perform basic arithmetic operations easily!")

# Inputs
a = st.number_input("Enter your first number", value=0.0)
b = st.number_input("Enter your second number", value=0.0)

operator = st.selectbox(
    "Select an operator",
    ["+", "-", "*", "/", "//", "%"]
)

# Button
if st.button("Calculate 🚀"):

    try:
        if operator == "+":
            result = a + b
            st.success(f"Addition of {a} and {b} is: {result}")

        elif operator == "-":
            result = a - b
            st.success(f"Subtraction of {a} and {b} is: {result}")

        elif operator == "*":
            result = a * b
            st.success(f"Multiplication of {a} and {b} is: {result}")

        elif operator == "/":
            if b == 0:
                st.error("❌ Cannot divide by zero")
            else:
                result = a / b
                st.success(f"Division of {a} and {b} is: {result}")

        elif operator == "//":
            if b == 0:
                st.error("❌ Cannot divide by zero")
            else:
                result = a // b
                st.success(f"Floor Division of {a} and {b} is: {result}")

        elif operator == "%":
            if b == 0:
                st.error("❌ Cannot divide by zero")
            else:
                result = a % b
                st.success(f"Modulus of {a} and {b} is: {result}")

        # 🎈 Balloons on success
        if 'result' in locals():
            st.balloons()

    except Exception as e:
        st.error(f"Something went wrong: {e}")
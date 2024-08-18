import streamlit as st

# Title of the app
st.title('Simple Calculator')

# User inputs
num1 = st.number_input('Enter first number', value=0.0)
num2 = st.number_input('Enter second number', value=0.0)

# Select operation
operation = st.selectbox('Choose an operation', ('Add', 'Subtract', 'Multiply', 'Divide'))

# Perform calculation
if operation == 'Add':
    result = num1 + num2
elif operation == 'Subtract':
    result = num1 - num2
elif operation == 'Multiply':
    result = num1 * num2
elif operation == 'Divide':
    if num2 != 0:
        result = num1 / num2
    else:
        result = 'Error! Division by zero.'

# Display result
st.write(f'Result: {result}')


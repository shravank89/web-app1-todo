import streamlit as st
from functions import get_todos, write_todos

todos = get_todos()

if 'something' not in st.session_state:
    st.session_state.something = ''


def add_todo():
    todo_local = st.session_state["new_todo"] + "\n"
    todos.append(todo_local)
    write_todos(todos)
    st.session_state.something = st.session_state.new_todo
    st.session_state.new_todo = ""


st.title("My ToDo App")
st.subheader("This is my to-do app")
st.write("This app will increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label = "", placeholder="Add a new todo..", on_change=add_todo, key='new_todo')

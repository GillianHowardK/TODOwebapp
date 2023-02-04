import streamlit as st
import functions


todo_items = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todo_items.append(todo)
    functions.alter_todos(todo_items)


st.title("To Do List by Gillian")


for index, todo_item in enumerate(todo_items):
    checkbox = st.checkbox(todo_item, key=todo_item)
    if checkbox:
        todo_items.pop(index)
        functions.alter_todos(todo_items)
        del st.session_state[todo_item]
        st.experimental_rerun()


st.text_input(label="", placeholder=">",
              on_change=add_todo, key="new_todo")



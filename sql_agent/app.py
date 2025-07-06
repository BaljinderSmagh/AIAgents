import streamlit as st
from agent import write_query, execute_query, generate_answer  # Make sure these are importable

st.title("SQL Agent Chat")

if "history" not in st.session_state:
    st.session_state.history = []

if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# user_input = st.text_input("Ask a question about your database:", value=st.session_state.user_input, key="chat_input")
user_input = st.chat_input("What would you like to know?")



if  user_input:
    state = {"question": user_input, "query": "", "result": "", "answer": ""}
    try:
        query_dict = write_query(state)
        state["query"] = query_dict["query"]
        result_dict = execute_query(state)
        state["result"] = result_dict["result"]
        answer_dict = generate_answer(state)
        state["answer"] = answer_dict["answer"]
        st.session_state.history.append(
            {"question": user_input, "answer": state["answer"]}
        )
        
       
    except Exception as e:
        st.error(f"Error: {e}")

# Display chat history
for chat in st.session_state.history:
    with st.chat_message("user"):
        st.markdown(chat["question"])
    with st.chat_message("assistant"):
        st.markdown(chat["answer"])

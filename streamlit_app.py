import streamlit as st

st.sidebar.markdown("Headquarters")
    
add_selectbox = st.sidebar.selectbox(
    "List of your agents",
    ("1", "2", "Mobile phone")
)

add_selectbox = st.sidebar.selectbox(
    "List of opponent agents",
    ("Email", "Home phone", "Mobile phone"))

st.sidebar.markdown("Scoring pile")
    
add_selectbox = st.sidebar.selectbox(
    "Your scoring pile",
    ("1", "2", "Mobile phone")
)

add_selectbox = st.sidebar.selectbox(
    "Opponent scoring pile",
    ("Email", "Home phone", "Mobile phone"))
    
add_selectbox = st.sidebar.selectbox(
    "Objective Deck",
    ("1", "2", "Mobile phone")
)

add_selectbox = st.sidebar.selectbox(
    "Group deck",
    ("Email", "Home phone", "Mobile phone")
)

add_selectbox = st.sidebar.selectbox(
    "Graveyard",
    ("Email", "Home phone", "Mobile phone")
)

if st.sidebar.button('Help'):
    st.sidebar.write('OK')

st.header('Test')

if st.button('Draw group card'):
    st.write('OK')

if st.button('Pass'):
    st.write('OK')

if st.button('Close game'):
    st.write('OK')

with st.container():
     st.balloons()
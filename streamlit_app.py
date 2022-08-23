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
    "Objective deck",
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
     
col1, col2 = st.columns(2)

with col1:
    with st.container():
    st.write("This is inside the container")

    # You can call any Streamlit command, including custom components:
    st.bar_chart(np.random.randn(50, 3))
    
    with st.container():
     st.balloons()

with col2:
    if st.button('Draw group card'):
    st.write('OK')

    if st.button('Pass'):
    st.write('OK')

    if st.button('Close game'):
    st.write('OK')
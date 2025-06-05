import streamlit as st

# Initialize the session state to hold the list of links
if 'links' not in st.session_state:
    st.session_state.links = []

st.title("Link Collector")

# Input box to take a link
new_link = st.text_input("Enter a link")

# Button to add link to the list
if st.button("Add"):
    if new_link.strip():
        st.session_state.links.append(new_link.strip())
        st.success(f"Added: {new_link}")
    else:
        st.warning("Please enter a valid link.")

# Show all links added so far with a remove button
st.subheader("Links Added:")
if st.session_state.links:
    for idx, link in enumerate(st.session_state.links):
        col1, col2 = st.columns([6, 1])
        with col1:
            st.write(f"{idx+1}. {link}")
        with col2:
            if st.button("❌", key=f"remove_{idx}"):
                st.session_state.links.pop(idx)
                st.rerun()  
else:
    st.write("No links added yet.")

# Submit button at the end
if st.button("Submit"):
    st.subheader("Submitted Links:")
    st.write(st.session_state.links)

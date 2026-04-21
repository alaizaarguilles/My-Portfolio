import streamlit as st

st.title("📞 Contact Me")

name = st.text_input("Alaiza M. Arguilles")
email = st.text_input("alaizaarguilles4@gmail.com")
message = st.text_area("Hello I Would like to ask about your project")

if st.button("Send"):
    if name and email and message:
        st.success("Message sent successfully! ✅")
    else:
        st.error("Please fill all fields.")

st.markdown("Social Links")
st.write("- GitHub: https://alaizaarguilles.github.io/")
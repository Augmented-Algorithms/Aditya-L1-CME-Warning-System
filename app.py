import streamlit as st

page_bg_img = """
<style>
.stApp {
    background-image: url("https://mrwallpaper.com/images/hd/hd-solar-flare-8rxanecj76jxibxm.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    position: relative;
}

.stApp::before {
    content: "";
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    background-color: rgba(211, 211, 211, 0.3); /* white translucent overlay */
    z-index: 0;
}

.stApp > * {
    position: relative;
    z-index: 1;
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
st.write("Hello")
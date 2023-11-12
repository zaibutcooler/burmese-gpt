import streamlit as st

def main():
    st.title("Simply say Uwu xD")

    video_source = st.sidebar.radio("Select feature:", ("Audio Generator", "Text Predictor",))

    if video_source == "Audio Generator":
        pass

    else:
        pass


if __name__ == "__main__":
    main()

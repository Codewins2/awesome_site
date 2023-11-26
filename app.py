import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title= "My Webpage", page_icon= ":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# user local css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html= True)

local_css("style/style.css")



# --- Load Assets ---
lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_xos4y1jg.json")

# img_contact_form = Image.open("F:\newsite\images")
# img_lottie_animation = Image.open("F:\newsite\images")



# header section --
with st.container():
        
    st.subheader("Sup, I am Ismail🙂")
    st.title("A programmer from Sirajgonj")
    st.write("I am passionate about coding and I like to code in my leisure time")
    st.write("[Here's a blog that I wrote >] (https://www.blogger.com/blog/post/edit/preview/7986157041660776728/4977350398324982955)")



# what I do


with st.container():
    st.write("___")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            - Hello, my name is Ismail.
            - I'm 16 years old. 
            - I'm from Bangladesh
            - My native language is Bangla
            - I can speak English semi fluently
            - One of my hobbies are coding, travelling, hanging out with friends.
            
            If you are interested to talk with me, here's my tweeter profile link
            """
        )
        st.write("[My social media link > ](https://twitter.com/Ismail78932)")


    with right_column:
        st_lottie(lottie_coding, height= 300,key = "coding")


with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    # with image_column:
    #     st.image(img_lottie_animation)
    with text_column:
        st.subheader(
        """
        If you don't know
        The basic difference -
        between a hacker and a programmer,
        you gotta check out my blog.
        """
        )

        st.markdown("[Here's the blog's link > ](https://ismailhossain23.blogspot.com/2022/10/Differences%20between%20hackers%20and%20programmers.html)")


#contact---
with st.container():
    st.write("---")
    st.header("Get in touch with me!")
    st.write("##")


    contact_form = """
    <form action="https://formsubmit.co/iiismail789@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value = "False">
        <input type="text" name="name" placeholder= "Your name" required>
        <input type="email" name="email" placeholder = "Your email" required>
        <textarea name = "message" placeholder = "Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form,unsafe_allow_html=True)
    with right_column:
        st.empty()


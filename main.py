import streamlit as st
from yoga import display_yoga_page
from bharatnatyam import display_bharatnatyam_page

def main():
    # Set page title
    st.set_page_config(page_title="Pose Perfect Preacher")
    
    add_bg_from_url()
    
    
   
    
    
    
 


    # Create a top bar widget
    st.title("Pose Perfect Preacher")
    menu_choice = st.sidebar.radio("Menu", ["Home", "Yoga", "Bharatnatyam"])

    # Display content based on menu choice
    if menu_choice == "Home":
        display_home()
    elif menu_choice == "Yoga":
        display_yoga_page()
    elif menu_choice == "Bharatnatyam":
        display_bharatnatyam_page()

def display_home():
    
    image_path = "logo.png"  # Replace with the path to your image file

   
    st.image(image_path,width=250)
    
    
    page_bg_color = "orange"  # Replace with your desired background color
    page_style = f"background-color: {page_bg_color}; padding: 1rem;"
    st.markdown(
        f"""
        <div style="{page_style}">
            <h1>Online Teaching Module</h1>
            <p>Welcome to AI based Dance and Yoga learning platform for all age groups</p>
            <!-- Add your app content here -->
        </div>
        """,
        unsafe_allow_html=True,
    )
    
def add_bg_from_url():
    st.markdown(
    f"""
     <style>
     .stApp {{
             background-image: url("data:image/jpeg;base64,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");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

    
   
if __name__ == "__main__":
    main()

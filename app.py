import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt

@st.cache_data
def load_requirement():
    try:
        requirement = pd.read_csv(r'C:\Users\Olamilekan .A. David\Downloads\Telegram Desktop\datajobs_desc_req.csv', encoding='MacRoman')
        return requirement
    except Exception as e:
        st.error(f"Error loading file: {e}")
        return None

@st.cache_data
def load_title():
    try:
        title = pd.read_csv(r'C:\Users\Olamilekan .A. David\Downloads\Telegram Desktop\dataset1.csv', encoding='MacRoman') 
        return title
    except Exception as e:
        st.error(f"Error loading file: {e}")
        return None

def home_page():
    st.title("The Data Compass: Guiding Data Professionals through Nigeria’s Job Market")
    st.write("""
             Welcome to Data Jobs in Nigeria, a finding carried out by a team spearheaded by Dr Victor Adekunle. 
             
             I am Olamilekan David
             """)
    st.write("""
In late September 2023, a pioneering project took flight in Nigeria's data landscape, driven by a quest to illuminate the path for data professionals navigating career choices. Eager to decipher the secrets of employer preferences and industry demands, we embarked on an ambitious mission—to uncover what employers seek and where they seek it.

Armed with determination but lacking readily available data, we ventured into uncharted territory—scraping multiple job websites. It was a steep learning curve, but we embraced the challenge wholeheartedly, pioneering a groundbreaking initiative tailored for our unique environment.

Following the arduous data collection phase, we meticulously wrangled the information, preparing it for analysis and visualization. Our goal? Empowering ourselves and fellow data enthusiasts to seize opportunities with strategic foresight.

Now, with Streamlit as our canvas, we proudly present the fruits of our labor—a testament to persistence and innovation on a remarkable journey. This project is our brainchild—a labor of love, conceived to redefine how we approach our careers in the data realm.

We welcome feedback and suggestions for improvement, striving always to enhance our offering. A heartfelt thank you to Dr. Victor Adekunle for inspiring us to reach higher, and to our dedicated team members—@genius, @diced_apple, @Oluwafemi, @ofure, @ohlight, @joana, @damilare—for their unwavering commitment and collaboration throughout this transformative journey.

Explore our dashboard and discover the insights that await—your compass in the dynamic world of data careers.
""")

    requirement = load_requirement()
    if requirement is not None:
        st.write(requirement.head())  # Display the first few rows of the first dataset

    title = load_title()
    if title is not None:
        st.write(title.head())  # Display the first few rows of the second dataset

def dashboard_page():
    st.title("The Data Compass: What can you see?")
    st.write("Welcome to our findings about data jobs in Nigeria! Do with this information what you like")
    st.write("""
This isn’t just any dashboard, it’s a treasure trove of insights waiting to be discovered. Think of yourself as a data detective, sifting through the clues to uncover the secrets of Nigeria’s job market.

Now these are the things we have provided to help you understand what we found, but you see that insight? Na you gho run am lol

🔍 Job Type Count bar chart, the quick peek into the minds of employers!

🥧 Job Type Proportion pie chart. That’s a pie that everyone wants a piece of!

☁️ Ever wondered what words pop up the most in job titles? As you be data professional, you suppose know this one sha lol

📊 Grouped Bar Chart shows the count of each job type for each location. It’s like having a bird’s eye view of the job landscape across different locations.

So go ahead, start exploring! You fit see wetin I no see for there sha? Remember, every insight is a step towards making informed career decisions in the dynamic world of data
             
Did you think I forgot the frequency of terms? Never, na smart man you be, so you know what to do 😂
""")  # Add your project insights here

    requirement = load_requirement()
    if requirement is not None:
        # Exclude any term that is in digits
        requirement = requirement[~requirement['Term'].str.isdigit()]

        # Select the top 20 rows
        top_20 = requirement.head(20)

        fig = px.bar(top_20, x='Term', y='Frequency', labels={'x':'Terms', 'y':'Frequency'}, title='Frequency of Terms')
        fig.update_layout(autosize=False, width=700, height=600)
        st.plotly_chart(fig)  # Display the plot in Streamlit

    title = load_title()
    if title is not None:
        # Bar Chart for Job Type Count
        job_type_counts = title['job_type'].value_counts()
        fig1 = px.bar(job_type_counts, x=job_type_counts.index, y=job_type_counts.values, labels={'x':'Job Type', 'y':'Count'}, title='Job Type Count')
        st.plotly_chart(fig1)  # Display the bar chart in Streamlit

        # Pie Chart for Job Type Proportion
        fig2 = px.pie(job_type_counts, names=job_type_counts.index, values=job_type_counts.values, title='Job Type Proportion')
        st.plotly_chart(fig2)  # Display the pie chart in Streamlit

        # Word Cloud for Title
        wordcloud = WordCloud(width = 1000, height = 500).generate(' '.join(title['title']))
        fig3, ax = plt.subplots()
        ax.imshow(wordcloud)
        ax.axis("off")
        st.pyplot(fig3)  # Display the word cloud in Streamlit

        # Grouped Bar Chart for Job Type and Location
        title_copy = title.copy()  # Create a copy of the DataFrame
        title_copy['count'] = 1
        fig4 = px.bar(title_copy, x="location", y="count", color="job_type", title="Job Type based on Location", labels={'location': 'Location', 'count': 'Count', 'job_type': 'Job Type'})
        st.plotly_chart(fig4)  # Display the grouped bar chart in Streamlit

def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", ["Home", "Dashboard"])

    if selection == "Home":
        home_page()
    elif selection == "Dashboard":
        dashboard_page()

if __name__ == "__main__":
    main()

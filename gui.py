# app.py
import streamlit as st
from analyzer import analyze_jobs
from dataset_loader import load_datasets
from scraper import scrape_learning_resources
import time

@st.cache_data
def load_cached_datasets():
    with st.spinner("Loading datasets..."):
        start = time.time()
        data = load_datasets()
        st.write(f"Datasets loaded in {time.time() - start:.2f} seconds")
    return data

def main():
    st.title("Job Skill Analyzer")
    st.markdown("Extract skills and learning resources from job postings—unfiltered and raw!")

    role = st.text_input("Enter Job Role:", "e.g., Software Engineer")
    if st.button("Analyze", key="analyze_btn"):
        combined_df = load_cached_datasets()
        
        with st.spinner("Analyzing..."):
            start = time.time()
            sentences_output, common_skills, _ = analyze_jobs(role, combined_df)
            analysis_time = time.time() - start
            
            start = time.time()
            resources = scrape_learning_resources(role)
            scrape_time = time.time() - start

            st.subheader("Results")
            st.markdown(f"**Analysis Time:** {analysis_time:.2f}s | **Scraping Time:** {scrape_time:.2f}s")
            
            st.markdown("### Skills You Need")
            if sentences_output == "No jobs found.":
                st.write("No skills found.")
            else:
                sentences = sentences_output.split("\n")
                filtered_sentences = [s.strip() for s in sentences if len(s.split()) >= 4]  # Min 4 words
                if not filtered_sentences:
                    st.write("No sentences with 4+ words found.")
                else:
                    for i, sentence in enumerate(filtered_sentences, 1):
                        st.write(f"{i}. {sentence}")
            
            st.markdown("### Learning Resources")
            if resources:
                for res in resources:
                    st.write(f"- {res}")
            else:
                st.write("No resources found.")

if __name__ == "__main__":
    main()
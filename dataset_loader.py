import pandas as pd


## The other linked datasets can be downloaded and loaded here.
DATASETS = [
        
        'linkedin_canada.csv'
        
        
    ]

def load_datasets():
    title_candidates = ["title", "Job_Ttl"]
    skills_candidates = ["description", "Job_Desc"]
    combined_df = pd.DataFrame()
    print("in load datasets function")

    for path in DATASETS:
        try:
            df = pd.read_csv(path)
            title_col = next((col for col in title_candidates if col in df.columns), None)
            skills_col = next((col for col in skills_candidates if col in df.columns), None)
            if title_col and skills_col:
                df = df.rename(columns={title_col: "Title", skills_col: "Skills"})
                df = df[["Title", "Skills"]].dropna().reset_index(drop=True)
                combined_df = pd.concat([combined_df, df], ignore_index=True)
        except Exception as e:
            print(f"Error loading {path}: {e}")
    return combined_df

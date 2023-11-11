import streamlit as st
import json
import pandas as pd

def quiz(json_data):
    dict2 = json_data['messages']
    que = []
    op1 = []
    op2 = []
    op3 = []
    op4 = []
    for i in dict2:
        if 'poll' in i:
            que.append(i['poll']["question"])
            try:
                op1.append(i["poll"]["answers"][0]["text"])
            except:
                op1.append(None)
            try:
                op2.append(i["poll"]["answers"][1]["text"])
            except:
                op2.append(None)
            try:
                op3.append(i["poll"]["answers"][2]["text"])
            except:
                op3.append(None)
            try:
                op4.append(i["poll"]["answers"][3]["text"])
            except:
                op4.append(None)
    dict89 = {'Question': que, 'option1': op1, 'option2': op2, 'option3': op3, 'option4': op4}
    df2 = pd.DataFrame(dict89)
    return df2

def main():
    st.title("Telegram -Quiz -Scraper")
    # Upload JSON file through Streamlit
    uploaded_file = st.file_uploader("Choose a JSON file", type="json")
    if uploaded_file is not None:
        # Read and parse the JSON file
        try:
            json_data = json.load(uploaded_file)
            dict2 = quiz(json_data)
        except json.JSONDecodeError as e:
            st.error(f"Error decoding JSON file: {e}")
            return

        # Display the parsed JSON data
        st.dataframe(dict2)
        csv_file = dict2.to_csv(index=False)

        # Add a button to download the DataFrame as a CSV file
        #if st.button("Download CSV"):
        st.download_button(label="Download CSV", data=csv_file, file_name="quiz_data.csv", mime="text/csv")

if __name__ == "__main__":
    main()

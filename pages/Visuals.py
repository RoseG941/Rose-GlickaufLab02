# PAGE TITLE
st.title("Data Visualizations")

# PART 1: GRAPHS FROM data.json

infile=open("data.json")
data=json.load(infile)
infile.close()
table=pd.DataFrame(data["data_points"])
table.columns=["Contestant", "Score"]
st.subheader(data["chart_title"])
st.dataframe(table)
bars=alt.Chart(table, title="Judges Scores").mark_bar().encode(x="Contestant", y="Score")
st.altair_chart(bars)
st.subheader("Scores Above Minimum")
cutoff=st.slider("Minimum Score", 13, 25, 13,)
small_table=table[table["Score"] >= cutoff]
line=alt.Chart(small_table).mark_line(point=True).encode(x="Contestant",y="Score")
st.altair_chart(line)


table=pd.read_csv("data.csv")
table["Value"]=pd.to_numeric(table["Value"])
st.subheader("My Survey Results")
st.dataframe(table)
bars=alt.Chart(table, title="Survey Scores")
bars=bars.mark_bar()
bars=bars.encode(x="Value", y="Category")
st.altair_chart(bars)
st.subheader("Pick a Minimum Score")
st.slider("Minimum score", 0, 30, 0, key="csv_cutoff")
cutoff_number=st.session_state["csv_cutoff"]
small=table[table["Value"] >= cutoff_number]
pie=alt.Chart(small, title="Scores at or above the minimum")
pie=pie.mark_arc()
pie=pie.encode(theta="Value", color="Category")
st.altair_chart(pie)

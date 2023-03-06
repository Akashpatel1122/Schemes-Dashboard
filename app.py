import pandas as pd
import streamlit as st
import numpy as np
st.set_page_config(
    page_title="Surguja Schemes Dashboard",
    page_icon="random",
    layout="wide"
)

df=pd.read_excel("data.xlsx",index_col=0)
df=df.drop("Remark",axis=1)


st.markdown('<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" crossorigin="anonymous">', unsafe_allow_html=True)

def bootstrap_card(title, value):
    card = f"""<div class="card text-center border border-warning">
            <div class="card-header text-dark text-weight-bold">
                <lead>{title}</lead>
            </div>
            <div class="card-body">
                <h4 class="card-title text-primary">{value}</h4>
            </div>
        </div>
    """
    return card

def calculate_metric(filtered_data):
    metric_value = dict()
    # Here, we can calculate any metric we want based on the filtered data
    metric_value["Total_Work"] =  filtered_data["Village Name"].count()
    metric_value["Total_Budget"] = round(filtered_data["Budget (In Lakhs)"].sum(),1)
    metric_value["Total_Scheme"] = filtered_data["Scheme"].nunique()
    return metric_value

# Add Streamlit sidebar elements
st.sidebar.title("Drop Down Filters")

metric_value=calculate_metric(df)

st.markdown("""
<div class="jumbotron bg-light text-dark text-center border border-warning ">
  <h1 class="display-6 text-dark">Surguja Schemes Dashboard</h1>
  <hr class="my-2">
</div>
""", unsafe_allow_html=True)

# Create the Bootstrap cards
def header(metric_value):
    # Use st.empty to create an empty element to hold the cards
    container = st.empty()
    # Use container.markdown to add the cards to the empty element
    container.markdown(f"""
    <div class="row text-center pb-5">
    <div class="col-sm-4">{bootstrap_card("Total Works",metric_value["Total_Work"])}</div>
    <div class="col-sm-4">{bootstrap_card("Total Budget(Lakhs)",metric_value["Total_Budget"])}</div>
    <div class="col-sm-4">{bootstrap_card("Total Schemes",metric_value["Total_Scheme"])}</div>
    </div>
    """,unsafe_allow_html=True)
    # Return the container so it can be updated later
    return container

cards=header(metric_value)
new_df=df.copy()
# Create the dropdowns with default values
options1 = df['Vidhansabha'].unique().tolist()
options1.insert(0,"All")
choice1 = st.sidebar.selectbox('Select Vidhansabha', options1, index=0)

options2 = df["Block"].unique().tolist()
if choice1 != "All":
    df = df[df['Vidhansabha'] == choice1]
    options2 = df["Block"].unique().tolist()

options2.insert(0, "All")
choice2 = st.sidebar.selectbox('Select Block', options2, index=0)
options3 = df["Sector"].unique().tolist()
if choice1 != "All" and choice2 != "All":
    df = df[(df['Vidhansabha'] == choice1) & (df["Block"] == choice2)]
    options3 = df["Sector"].unique().tolist()
elif choice1 != "All" and choice2 == "All":
    df = df[df['Vidhansabha'] == choice1]
    options3 = df["Sector"].unique().tolist()
elif choice1 == "All" and choice2 != "All":
    df = df[df['Block'] == choice2]
    options3 = df["Sector"].unique().tolist()

options3.insert(0, "All")
choice3 = st.sidebar.selectbox('Select Sector', options3, index=0)

options4 = df["Village Name"].unique().tolist()
if choice1 != "All" and choice2 != "All" and choice3 != "All":
    df = df[(df['Vidhansabha'] == choice1) & (df["Block"] == choice2) & (df["Sector"] == choice3)]
    options4 = df["Village Name"].unique().tolist()
elif choice1 != "All" and choice2 != "All" and choice3 == "All":
    df = df[(df['Vidhansabha'] == choice1) & (df["Block"] == choice2)]
    options4 = df["Village Name"].unique().tolist()
elif choice1 != "All" and choice2 == "All" and choice3 == "All":
    df = df[df['Vidhansabha'] == choice1]
    options4 = df["Village Name"].unique().tolist()
elif choice1 == "All" and choice2 == "All" and choice3 == "All":
    options4 = df["Village Name"].unique().tolist()
options4.insert(0, "All")
choice4 = st.sidebar.selectbox('Select Booth/Village', options4, index=0)

options5 = df["Scheme"].unique().tolist()
if choice1 != "All" and choice2 != "All" and choice3 != "All" and choice4 != "All":
    df = df[(df['Vidhansabha'] == choice1) & (df["Block"] == choice2) & (df["Sector"] == choice3) & (df["Village Name"] == choice4)]
    options5 = df["Scheme"].unique().tolist()
elif choice1 != "All" and choice2 != "All" and choice3 != "All" and choice4 == "All":
    df = df[(df['Vidhansabha'] == choice1) & (df["Block"] == choice2) & (df["Sector"] == choice3)]
    options5 = df["Scheme"].unique().tolist()
elif choice1 != "All" and choice2 != "All" and choice3 == "All" and choice4 == "All":
    df = df[(df['Vidhansabha'] == choice1) & (df["Block"] == choice2)]
    options5 = df["Scheme"].unique().tolist()
elif choice1 != "All" and choice2 == "All" and choice3 == "All" and choice4 == "All":
    df = df[df['Vidhansabha'] == choice1]
    options5 = df["Scheme"].unique().tolist()
elif choice1 == "All" and choice2 == "All" and choice3 == "All" and choice4 == "All":
    options5 = df["Scheme"].unique().tolist()
options5.insert(0, "All")
choice5 = st.sidebar.selectbox('Select Scheme', options5, index=0)

options6 = df["Department"].unique().tolist()
if choice1 != "All" and choice2 != "All" and choice3 != "All" and choice4 != "All" and choice5 != "All":
    df = df[(df['Vidhansabha'] == choice1) & (df["Block"] == choice2) & (df["Sector"] == choice3) & (df["Village Name"] == choice4) & (df["Scheme"] == choice5)]
    options6 = df["Department"].unique().tolist()
elif choice1 != "All" and choice2 != "All" and choice3 != "All" and choice4 != "All" and choice5 == "All":
    df = df[(df['Vidhansabha'] == choice1) & (df["Block"] == choice2) & (df["Sector"] == choice3) & (df["Village Name"] == choice4)]
    options6 = df["Department"].unique().tolist()
elif choice1 != "All" and choice2 != "All" and choice3 != "All" and choice4 == "All" and choice5 == "All":
    df = df[(df['Vidhansabha'] == choice1) & (df["Block"] == choice2) & (df["Sector"] == choice3)]
    options6 = df["Department"].unique().tolist()
elif choice1 != "All" and choice2 != "All" and choice3 == "All" and choice4 == "All" and choice5 == "All":
    df = df[(df['Vidhansabha'] == choice1) & (df["Block"] == choice2)]
    options6 = df["Department"].unique().tolist()
elif choice1 != "All" and choice2 == "All" and choice3 == "All" and choice4 == "All" and choice5 == "All":
    df = df[df['Vidhansabha'] == choice1]
    options6 = df["Department"].unique().tolist()
elif choice1 == "All" and choice2=="All" and choice3=="All" and choice4=="All" and choice5=="All":
    options6 = df["Department"].unique().tolist()
options6.insert(0, "All")
choice6 = st.sidebar.selectbox('Select Department', options6, index=0)

options7 = df["Approval Year"].unique().tolist()
if choice1 != "All" and choice2 != "All" and choice3 != "All" and choice4 != "All" and choice5 != "All" and choice6 != "All":
    df = df[(df['Vidhansabha'] == choice1) & (df["Block"] == choice2) & (df["Sector"] == choice3) & (df["Village Name"] == choice4) & (df["Scheme"] == choice5) & (df["Department"] == choice6)]
    options7 = df["Approval Year"].unique().tolist()
elif choice1 != "All" and choice2 != "All" and choice3 != "All" and choice4 != "All" and choice5 == "All" and choice6 == "All":
    df = df[(df['Vidhansabha'] == choice1) & (df["Block"] == choice2) & (df["Sector"] == choice3) & (df["Village Name"] == choice4)]
    options7 = df["Approval Year"].unique().tolist()
elif choice1 != "All" and choice2 != "All" and choice3 != "All" and choice4 == "All" and choice5 == "All" and choice6 == "All":
    df = df[(df['Vidhansabha'] == choice1) & (df["Block"] == choice2) & (df["Sector"] == choice3)]
    options7 = df["Approval Year"].unique().tolist()
elif choice1 != "All" and choice2 != "All" and choice3 == "All" and choice4 == "All" and choice5 == "All" and choice6 == "All":
    df = df[(df['Vidhansabha'] == choice1) & (df["Block"] == choice2)]
    options7 = df["Approval Year"].unique().tolist()
elif choice1 != "All" and choice2 == "All" and choice3 == "All" and choice4 == "All" and choice5 == "All" and choice6 == "All":
    df = df[df['Vidhansabha'] == choice1]
    options7 = df["Approval Year"].unique().tolist()
elif choice1 == "All" and choice2=="All" and choice3=="All" and choice4=="All" and choice5=="All" and choice6=="All":
    options7 = df["Approval Year"].unique().tolist()
options7.insert(0, "All")
choice7 = st.sidebar.selectbox('Select Approval Year', options7, index=0)




# Filter the data based on selected options
filter_button=st.sidebar.button("Filter Data")

if filter_button:
    # Filter the dataframe based on the selected values
    if choice1 != 'All':
        df = df[df['Vidhansabha'] == choice1]
    if choice2 != 'All':
        df = df[df['Block'] == choice2]
    if choice3 != 'All':
        df = df[df['Sector'] == choice3]
    if choice4 != 'All':
        df = df[df['Village Name'] == choice4]
    if choice5 != 'All':
        df = df[df['Scheme'] == choice5]
    if choice6 != 'All':
        df = df[df['Department'] == choice6]
    if choice7 != 'All':
        df = df[df['Approval Year'] == choice7]

    st.dataframe(df,use_container_width=True)

    metric_value = calculate_metric(df)
    cards.markdown(f"""
        <div class="row text-center pb-5">
        <div class="col-sm-4">{bootstrap_card("Total Works", metric_value["Total_Work"])}</div>
        <div class="col-sm-4">{bootstrap_card("Total Budget(Lakhs)", metric_value["Total_Budget"])}</div>
        <div class="col-sm-4">{bootstrap_card("Total Schemes", metric_value["Total_Scheme"])}</div>
        </div>
        """, unsafe_allow_html=True)

else:
    st.dataframe(new_df,use_container_width=True)


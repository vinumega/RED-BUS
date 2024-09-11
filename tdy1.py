import mysql.connector
import pandas as pd
import streamlit as st

# Connect to MySQL database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="bus_details"
)
cursor = con.cursor(dictionary=True)

# Execute initial query to fetch data from MySQL
cursor.execute("SELECT * FROM bus_details")
data = cursor.fetchall()

# Close the cursor after fetching data
cursor.close()

# Convert data to Pandas DataFrame
df = pd.DataFrame(data)

# Streamlit UI Title
st.title('RedBus')


# Sidebar filters
st.sidebar.title('Filters')
# Unique route names
route_names = df['Route_name'].unique().tolist()
route_name = st.sidebar.selectbox('Select Route Name', ['', *route_names])

# Bus types
bus_types = ['AC', 'Non AC', 'Others']
bus_type = st.sidebar.selectbox('Select Bus Type', ['', *bus_types])

# Hours of departure
bus_hours_disp = {}
for i in range(24):
    if i != 23:
        bus_hours_disp[i] = f"{i}:00 to {i+1}:00"
    else:
        bus_hours_disp[i] = f"{i}:00 to 0:00"

bus_hours = list(range(24))

Start_time_options = [''] + bus_hours

Start_time = st.sidebar.selectbox("Starting time hour",Start_time_options, format_func=lambda x: bus_hours_disp[x] if x in bus_hours_disp else '')

# Minimum star rating slider
min_ratings = st.sidebar.slider('Minimum Ratings', min_value=0.0, max_value=5.0, step=0.1, value=0.0)

# Maximum ticket price
max_price = st.sidebar.number_input('Maximum Ticket Price', min_value=0.0, format="%.2f", value=10000.0)


# SQL queries for filtering data
query = "SELECT * FROM bus_details WHERE 1=1"

# Apply filters based on user selections
if route_name:
    query += f" AND route_name = '{route_name}'"

if bus_type == 'AC':
    query += " AND (bus_type REGEXP 'AC|A.C|A/C') AND (bus_type NOT REGEXP 'Non AC|Non A/C|Non A.C|NON-AC')"
elif bus_type == 'Non AC':
    query += " AND (bus_type REGEXP 'Non AC|Non A/C|Non A.C|NON-AC')"
elif bus_type == 'Others':
    query += " AND (bus_type NOT REGEXP 'AC|A.C|A/C|Non AC|Non A/C|Non A.C|NON-AC') AND (bus_type IS NOT NULL)"


if Start_time != '':
    if Start_time or Start_time == 0:
        query += f" AND HOUR(Start_time) = {(Start_time)}"

query += f" AND Ratings >= {min_ratings} AND price <= {max_price}"

# Execute final query
cursor = con.cursor(dictionary=True)
cursor.execute(query)
filtered_data = cursor.fetchall()
cursor.close()

# Convert filtered data to DataFrame to display in streamlit
filtered_df = pd.DataFrame(filtered_data)

# Display the filtered data in a table
if not filtered_df.empty:
    st.write("Total Results:", len(filtered_df))
    st.dataframe(filtered_df.drop(columns=['Route_link']))
else:
    st.warning('No bus routes found with the specified filters.')

# Close MySQL connection
con.close()
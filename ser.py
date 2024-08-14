
import streamlit as st
import mysql.connector
import pandas as pd
def main():
    st.title("RedBus - Bus Details Management")
   

# Connect to the MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="project2"
)
st.header("Enter Bus Details")
bus_name = st.text_input("Bus Name")
bus_type = st.selectbox("Bus Type", ["AC", "Non-AC", "Sleeper", "Seater"])
start_time = st.time_input("Start Time")
end_time = st.time_input("End Time")
total_duration = st.time_input("Total Duration")
price = st.number_input("Price", min_value=0.0, step=0.1)
seats_available = st.number_input("Seats Available", min_value=1, step=1)
ratings = st.slider("Ratings", min_value=0.0, max_value=5.0, step=0.1)
route_link = st.text_input("Route Link")
route_name = st.text_input("Route Name")
if st.button("Insert Bus_Details"):
        bus_data = (
            bus_name,
            bus_type,
            start_time,
            end_time,
            total_duration,
            price,
            seats_available,
            ratings,
            route_link,
            route_name
        )
        insert_bus_details(conn, bus_data)
        st.success("Bus details inserted successfully!")

    # Display all bus details
st.header("BusDetails")
my_cursor = conn.cursor()
my_cursor.execute("SELECT * FROM bus_details")
rows = my_cursor.fetchall()
df = pd.DataFrame(rows, columns=[
        "Bus ID", "Bus Name", "Bus Type", "Start Time", "End Time",
        "Total Duration", "Price", "Seats Available", "Ratings", "Route Link", "Route Name"
    ])
st.dataframe(df)

conn.close()

if __name__ == "__main__":
    main()
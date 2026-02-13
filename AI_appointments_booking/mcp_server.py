
import csv
import os
from typing import Any

import httpx
from mcp.server.fastmcp import FastMCP



CSV_FILE = "appointments1.csv"

def create_appointment(name: str, date: str,time:str):
    file_exists = os.path.isfile(CSV_FILE)

    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["name", "date", "time"])
        writer.writerow([name, date, time])

    return f"Appointment booked for {name} on {date} at {time}"

def list_appointments():
    appointments = []

    if not os.path.isfile(CSV_FILE):
        return appointments

    with open(CSV_FILE, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            appointments.append(row)

    return appointments
def cancel_appointment(name: str, date: str, time: str):
    if not os.path.isfile(CSV_FILE):
        return f"No appointments found to cancel."
    
    name = name.strip().lower()
    date = date.strip().lower()
    time = time.replace("-", " to ").strip().lower()

    appointments = []
    appointment_found = False

    with open(CSV_FILE, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row_name = row["name"].strip().lower()
            row_date = row["date"].strip().lower()
            row_time = row["time"].replace("-", " to ").strip().lower()
            if row_name== name and row_date == date and row_time== time:
                appointment_found = True
            else:
                appointments.append(row)

    if not appointment_found:
        return f"No matching appointment found for {name} on {date} at {time}."

    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "date", "time"])
        writer.writeheader()
        writer.writerows(appointments)

    return f"Appointment for {name} on {date} at {time} has been canceled."



mcp = FastMCP("mcp_server")
#@mcp.tool()
#def create_appointment_tool(name: str, date: str, starttime: str,endtime:str):
#    return create_appointment(name, date, starttime,endtime)

@mcp.tool(
    name="create_appointment",
    description="Book an appointment in the weekly schedule.",
)
def create_appointment_tool(
    name: str,
    date: str,
    time: str
):
    """
    name: person name
    date: weekday name exactly one of [Monday, Tuesday, Wednesday, Thursday, Friday]
    time: time slot exactly like '4:00 to 5:00'
    """
    return create_appointment(name, date, time)

@mcp.tool(
        name="list_appointment",
        description="list the appointments on a specific weekday"
)
def list_appointments_tool():
    return list_appointments()


@mcp.tool(
        name="cancel_appointment",
        description="""
        "delete or cancel an appointment in the weekly schedule
        use this tool when the user asks to delete,cancel or remove an appointment"""
)
def cancel_appointment_tool(
    name:str,
    date:str,
    time:str
):
    """
    Docstring for cancel_appointment_tool
    
    name:person name
    date: weekday name exactly one of [Monday, Tuesday, Wednesday, Thursday, Friday]
    time: time slot exactly like '4:00 to 5:00'
    use this tool when the user asks to delete,cancel or remove an appointment
    """
    return cancel_appointment(name,date,time)
    

#def cancel_appointment_tool(name: str, date: str, time: str):
 #   return cancel_appointment(name, date, time)


if __name__ == "__main__":
    mcp.run()

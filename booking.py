# Defining/declaring functions
# Task 1: Add Room Function
def add_room(rooms, room_number, bed_type="Double", smoking=False):
  new_room = {
      "room_number": room_number,
      "bed_type": bed_type,
      "smoking": smoking,
      "availability": True
  }
  rooms.append(new_room)

# Task 2: Book Room Function
def book_room(rooms, preferred_bed_type="Double", smoking_preference=False):
  for room in rooms:
      if (room["availability"]) and (room["bed_type"] == preferred_bed_type) and (room["smoking"] == smoking_preference):
          room["availability"] = False
          return f"Room {room['room_number']} booked successfully."
  return "No matching room available."

# Task 3: List Available Rooms Function
def list_available_rooms(rooms):
  available_rooms = [room["room_number"] for room in rooms if room["availability"]]
  return ("Available Rooms:", available_rooms)

# Calling functions
# Task 1 continued: Adding rooms
rooms = []
add_room(rooms, 101)
add_room(rooms, 102, "Single", True)
add_room(rooms, 103)
add_room(rooms, 104, "Single")
add_room(rooms, 105, "Double", True)
print(rooms)

# Task 3 continued: List available rooms before booking 
print("Available Rooms before booking:", list_available_rooms(rooms))

# Task 2 continued: booking rooms  
book_room(rooms)
book_room(rooms, "Single")
book_room(rooms, smoking_preference=True)

# Task 3: List available rooms after booking continued
print("Available Rooms after booking:", list_available_rooms(rooms))

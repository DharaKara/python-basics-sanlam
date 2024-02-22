# Task 1: Add Room Function
def add_room(rooms, room_number, bed_type="Double", smoking=False):
  new_room = {
      "room_number": room_number,
      "bed_type": bed_type,
      "smoking": smoking,
      "availability": True
  }
  rooms.append(new_room)

# adding rooms:
rooms = []
add_room(rooms, 101)
add_room(rooms, 102, "Single", True)
add_room(rooms, 103)
add_room(rooms, 104, "Single")
add_room(rooms, 105, "Double", True)
print(rooms)

# Task 2: Book Room Function
def book_room(rooms, preferred_bed_type="Double", smoking_preference=False):
  for room in rooms:
      if room["availability"] and room["bed_type"] == preferred_bed_type and room["smoking"] == smoking_preference:
          room["availability"] = False
          print(f"Room {room['room_number']} booked successfully.")
          return
  print("No matching room available.")

book_room(rooms)
book_room(rooms, "Single")
book_room(rooms, smoking_preference=True)

# Task 3: List Available Rooms Function
def list_available_rooms(rooms):
  print("Available Rooms:")
  for room in rooms:
      if room["availability"]:
          print(f"Room {room['room_number']}: {room['bed_type']} Bed, Smoking: {room['smoking']}")

list_available_rooms(rooms)


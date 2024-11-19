# Create the 2D Boolean array Evening[] using nested loops
Evening = []
for rows in range(10):  # Create 10 rows
    row = []
    for seats in range(20):  # Create 20 seats per row
        row.append(False)
    Evening.append(row)


# Count and output the number of seats already booked
booked_seats = 0
for i in range(10):  # Iterate through rows
    for j in range(20):  # Iterate through columns
        if Evening[i][j]:  # Check if the seat is booked
            booked_seats += 1

print("Total number of seats already booked:", booked_seats)

# Allow user to input the number of seats required
print("Enter the number of seats you want to book (1 to 4):")
seats_required = int(input())

# Validate input
if seats_required < 1 or seats_required > 4:
    print("Invalid input. You can only book between 1 and 4 seats.")
else:
    # Check if enough seats are available
    available_seats = 200 - booked_seats  # Total seats = 10 rows x 20 seats
    if available_seats < seats_required:
        if available_seats == 0:
            print("House full. No seats are available.")
        else:
            print("Only", available_seats, "seats are available.")
    else:
        # Allocate seats
        seats_booked = 0
        print("Booking the seats:")
        for i in range(10):  # Iterate through rows
            for j in range(20):  # Iterate through columns
                if not Evening[i][j]:  # If the seat is available
                    Evening[i][j] = True  # Mark the seat as booked
                    seats_booked += 1
                    row_number = i + 1  # Row numbers are 1-based
                    seat_number = j + 1  # Seat numbers are 1-based
                    print("Seat booked: Row", row_number, "Seat", seat_number)
                    if seats_booked == seats_required:
                        break  # Exit inner loop
            if seats_booked == seats_required:
                break  # Exit outer loop

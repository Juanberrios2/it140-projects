"""Project Two starter for the student's text-based adventure game."""

# Created by: Juan Berrios


def show_instructions():
    """Display the game objective and available commands."""
    print("Welcome to The Final Haul!")
    print("A winter storm has stranded you at an abandoned trucking facility.")
    print("Your truck needs repairs, and a cargo thief is searching the property.")
    print("Collect all 6 trucking supplies before entering the Loading Dock.")
    print("Move commands: go North, go South, go East, go West")
    print("Collect items: get 'item name'")
    print("Type 'exit' to quit the game.")
    print("-----------------------------------")


def show_status(current_room, inventory, rooms):
    """Display the player's current game status."""
    print("\n----------------------------------------")
    print("Current location:", current_room)
    print("Inventory:", inventory)

    if "item" in rooms[current_room]:
        print("You see:", rooms[current_room]["item"])

    print("----------------------------------------")


def main():
    """Run the main gameplay loop."""
    
    rooms = {
        "Truck Cab": {
            "North": "Dispatch Office",
            "South": "Repair Garage",
            "East": "Driver Lounge",
            "West": "Fuel Station"
        },
        "Dispatch Office": {
            "South": "Truck Cab",
            "North": "Loading Dock",
            "item": "Route Map"
        },
        "Repair Garage": {
            "North": "Truck Cab",
            "East": "Maintenance Bay",
            "item": "Tool Kit"
        },
        "Maintenance Bay": {
            "West": "Repair Garage",
            "North": "Driver Lounge",
            "item": "Tire Chains"
        },
        "Driver Lounge": {
            "West": "Truck Cab",
            "South": "Maintenance Bay",
            "item": "Flashlight"
        },
        "Fuel Station": {
            "East": "Truck Cab",
            "South": "Parts Warehouse",
            "item": "Diesel Can"
        },
        "Parts Warehouse": {
            "North": "Fuel Station",
            "item": "Spare Battery"
        },
        "Loading Dock": {
            "South": "Dispatch Office",
            "villain": "Cargo Thief"
        }
    }


    
    current_room = "Truck Cab"

    
    inventory = []
    required_items = 6

    
    show_instructions()

    
    while True:
        show_status(current_room, inventory, rooms)

        if current_room == "Loading Dock":
            if len(inventory) == required_items:
                print("\nYou collected all 6 trucking supplies!")
                print("You repaired your truck and secured the load.")
                print("The cargo thief was unable to stop you.")
                print("Congratulations! You completed The Final Haul!")
                print("YOU WIN!")
            else:
                print("\nThe cargo thief found you at the Loading Dock!")
                print("You did not collect all 6 supplies.")
                print("Your valuable cargo has been stolen.")
                print("GAME OVER!")
            break

        command = input("\nEnter your move: ").strip()

        if command.lower() == "exit":
            print("You ended your trucking adventure.")
            break

        elif command.lower().startswith("go "):
            direction = command[3:].strip().title()

            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
                print("\nYou travel", direction, "to the", current_room + ".")
            else:
                print("\nYou cannot travel that direction!")

        elif command.lower().startswith("get "):
            requested_item = command[4:].strip()

            if "item" in rooms[current_room]:
                room_item = rooms[current_room]["item"]

                if requested_item.lower() == room_item.lower():
                    inventory.append(room_item)
                    del rooms[current_room]["item"]
                    print("\nYou collected the", room_item + "!")
                    print("Supplies collected:",
                          str(len(inventory)) + "/" + str(required_items))
                else:
                    print("\nThat item is not in this location.")
            else:
                print("\nThere are no supplies to collect here.")

        else:
            print("\nInvalid command!")
            print("Use 'go North' or 'get Item Name'.")
            print("Type 'exit' to quit.")


if __name__ == "__main__":
    main()

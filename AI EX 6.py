def vacuum_cleaner(environment, initial_location):
    location = initial_location
    cost = 0

    print(f"Initial State: {environment}, Location: {location}\n")

    while any(status == 'Dirty' for status in environment.values()):
        if environment[location] == 'Dirty':
            print(f"Location {location} is Dirty. Action: Clean (Suck)")
            environment[location] = 'Clean'
            cost += 1
        else:
            print(f"Location {location} is already Clean.")

        # Move to the other location
        if location == 'A':
            location = 'B'
            print("Action: Move to Location B")
        else:
            location = 'A'
            print("Action: Move to Location A")
        cost += 1
        print("---")

    print(f"Final Clean Environment State: {environment}")
    print(f"Total Cost/Steps: {cost}")

# Environment: A and B are both Dirty
env = {'A': 'Dirty', 'B': 'Dirty'}
vacuum_cleaner(env, initial_location='A')

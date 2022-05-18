movie_name = input()

total_tickets = 0
student_tickets = 0
standard_tickets = 0
kids_tickets = 0
end_day = True
while movie_name != "Finish":
    end_day = True
    free_seats = int(input())
    seats_taken = 0
    while seats_taken != free_seats:
        ticket_type = input()
        if ticket_type == "End":
            break
        elif ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        else:
            kids_tickets += 1
        seats_taken += 1
        total_tickets += 1
    print(f"{movie_name} - {seats_taken / free_seats * 100:.2f}% full.")
    movie_name = input()
if end_day:
    print(f"Total tickets: {total_tickets}")
    print(f"{student_tickets / total_tickets * 100:.2f}% student tickets.")
    print(f"{standard_tickets / total_tickets * 100:.2f}% standard tickets.")
    print(f"{kids_tickets / total_tickets * 100:.2f}% kids tickets.")

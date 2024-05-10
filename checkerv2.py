def check_tickets(tickets_file, winning_numbers_file):
    matching_tickets = []

    with open(tickets_file, 'r') as file:
        tickets = [line.strip() for line in file]

    with open(winning_numbers_file, 'r') as file:
        winning_numbers = [line.strip() for line in file]

    for ticket in tickets:
        for number in winning_numbers:
            if ticket.endswith(number):
                matching_tickets.append(ticket)
                break

    return matching_tickets

if __name__ == "__main__":
    tickets_file = "/Users/dimmybrave/Documents/scripts/my_tickets.txt"  # Путь к вашему текстовому файлу с билетами
    winning_numbers_file = "/Users/dimmybrave/Documents/scripts/win_teckets.txt"  # Путь к вашему текстовому файлу с выигрышными номерами

    matching_tickets = check_tickets(tickets_file, winning_numbers_file)
    if matching_tickets:
        print("Совпадающие билеты:")
        for ticket in matching_tickets:
            print(ticket)
    else:
        print("Нет совпадающих билетов.")

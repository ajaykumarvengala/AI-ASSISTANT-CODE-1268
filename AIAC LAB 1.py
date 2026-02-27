#Task 1:
#“Generate a Python function merge_sort(arr) that sorts a list in ascending order using the Merge Sort algorithm. Include time complexity and space complexity in the function docstring. Also provide test cases.”


def merge_sort(arr):
    """
    Sorts a list in ascending order using Merge Sort.

    Time Complexity:
        Best Case: O(n log n)
        Average Case: O(n log n)
        Worst Case: O(n log n)

    Space Complexity:
        O(n)

    Parameters:
        arr (list): List of elements

    Returns:
        list: Sorted list
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Test Cases
print(merge_sort([38, 27, 43, 3, 9, 82, 10]))
print(merge_sort([5, 1, 4, 2, 8]))

#Task 2:
#“Generate a Python function binary_search(arr, target) that performs binary search on a sorted list and returns the index of the target or -1 if not found. Include best, average, and worst-case time complexities in the docstring and provide test cases.”

def binary_search(arr, target):
    """
    Performs Binary Search on a sorted list.

    Time Complexity:
        Best Case: O(1)
        Average Case: O(log n)
        Worst Case: O(log n)

    Space Complexity:
        O(1)

    Parameters:
        arr (list): Sorted list
        target: Element to search

    Returns:
        int: Index of target or -1 if not found
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Test Cases
arr = [1, 3, 5, 7, 9, 11]
print(binary_search(arr, 7))
print(binary_search(arr, 4))

#Task 3:
#“For a healthcare appointment system storing appointment ID, patient name, doctor name, appointment time, and consultation fee: Suggest efficient searching and sorting algorithms. Justify your choices.  Implement searching by appointment ID and sorting by time or fee in Python.”

appointments = [
    (101, "Ravi", "Dr. Kumar", "10:30", 500),
    (102, "Anu", "Dr. Meena", "09:30", 300),
    (103, "Raj", "Dr. Arun", "11:00", 700)
]

# Sort by consultation fee
sorted_by_fee = sorted(appointments, key=lambda x: x[4])
print("Sorted by Fee:", sorted_by_fee)

# Search by Appointment ID
def search_by_id(data, target):
    data_sorted = sorted(data, key=lambda x: x[0])
    ids = [item[0] for item in data_sorted]
    return binary_search(ids, target)

print("Search ID 102:", search_by_id(appointments, 102))

#Task 4:
#“Suggest efficient searching and sorting algorithms for a railway reservation system that searches by ticket ID and sorts by travel date or seat number. Justify and implement in Python.”

tickets = [
    (201, "Ramesh", "12345", 12, "2026-03-10"),
    (202, "Sita", "54321", 5, "2026-02-28"),
    (203, "Arun", "67890", 20, "2026-03-05")
]

# Sort by travel date
sorted_tickets = sorted(tickets, key=lambda x: x[4])
print("Sorted by Date:", sorted_tickets)

# Search by Ticket ID
ids = [t[0] for t in sorted(tickets, key=lambda x: x[0])]
print("Search Ticket 202:", binary_search(ids, 202))

#Task 5:
#“Recommend optimized searching and sorting algorithms for hostel allocation records (search by student ID, sort by room number or allocation date). Justify and implement.”

rooms = [
    (1, 101, 1, "2026-01-10"),
    (2, 203, 2, "2026-01-05"),
    (3, 102, 1, "2026-01-12")
]

sorted_rooms = sorted(rooms, key=lambda x: x[1])
print("Sorted by Room Number:", sorted_rooms)

#Task 6:
#“For a movie streaming platform, suggest suitable searching and sorting algorithms to search by movie ID and sort by rating or release year. Justify and implement.”

movies = [
    (301, "MovieA", "Action", 4.5, 2022),
    (302, "MovieB", "Drama", 3.8, 2020),
    (303, "MovieC", "Sci-Fi", 4.9, 2023)
]

sorted_movies = sorted(movies, key=lambda x: x[3], reverse=True)
print("Sorted by Rating:", sorted_movies)

#Task 7:
#“Suggest optimized algorithms for searching crop data by crop ID and sorting by moisture level or yield estimate. Justify and implement.”

crops = [
    (401, "Wheat", 45, 30, 500),
    (402, "Rice", 60, 28, 700),
    (403, "Corn", 50, 32, 650)
]

sorted_crops = sorted(crops, key=lambda x: x[4], reverse=True)
print("Sorted by Yield:", sorted_crops)

#Task 8:
#“Recommend suitable searching and sorting algorithms for an airport flight system (search by flight ID, sort by departure or arrival time). Justify and implement in Python.”

flights = [
    (501, "Indigo", "10:00", "12:00", "On Time"),
    (502, "Air India", "09:00", "11:30", "Delayed"),
    (503, "SpiceJet", "13:00", "15:00", "On Time")
]

sorted_flights = sorted(flights, key=lambda x: x[2])
print("Sorted by Departure Time:", sorted_flights)
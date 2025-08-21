def count_max_request(log_entries):
    max_request_count = 0

    for i in range(len(log_entries)):
        start_time = log_entries[i]
        end_time = start_time + 60

        request_count = 0
        for j in range(len(log_entries)):
            if start_time <= log_entries[j] <= end_time:
                request_count += 1

        if request_count > max_request_count:
            max_request_count = request_count
            exact_start_time = start_time
            exact_end_time = end_time

    return max_request_count, exact_start_time, exact_end_time

log_entries_1 = [10, 20, 30, 70, 80, 90, 100, 150]
log_entries_2 = [0, 5, 10, 30, 45, 60, 62, 65, 70, 100, 120, 130]

max_request_count, exact_start_time, exact_end_time = count_max_request(log_entries_2)

print(F"Start Time: {exact_start_time},", F"End Time: {exact_end_time},", F"Max Request Counts: {max_request_count}")
record_to_be_conquered_seconds = float(input())
distance_meters = float(input())
time_seconds_to_swim_1m = float(input())


resistance_total = (distance_meters // 15) * 12.5 
time_to_switm = distance_meters * time_seconds_to_swim_1m



total_distance_time = resistance_total + time_to_switm

if record_to_be_conquered_seconds < total_distance_time:
    print(f"No, he failed! He was {total_distance_time - record_to_be_conquered_seconds:.2f} seconds slower.")
else:
    print(f" Yes, he succeeded! The new world record is {total_distance_time:.2f} seconds.")







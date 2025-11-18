import pandas as pd
from kafka import KafkaProducer
import time
import json

# Connect to Kafka
producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Load data to simulate traffic
columns = ['duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes', 'land', 'wrong_fragment', 'urgent', 'hot', 'num_failed_logins', 'logged_in', 'num_compromised', 'root_shell', 'su_attempted', 'num_root', 'num_file_creations', 'num_shells', 'num_access_files', 'num_outbound_cmds', 'is_host_login', 'is_guest_login', 'count', 'srv_count', 'serror_rate', 'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate', 'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count', 'dst_host_same_srv_rate', 'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate', 'dst_host_rerror_rate', 'dst_host_srv_rerror_rate', 'class']
df = pd.read_csv('kdd.csv', names=columns)

print("--- STARTED IoV TRAFFIC SIMULATION ---")
for index, row in df.iterrows():
    traffic_data = row.to_dict()
    # Send to Kafka topic 'iov_network'
    producer.send('iov_network', traffic_data)
    
    # Print status every 100 packets so we know it's working
    if index % 100 == 0:
        print(f"[+] Vehicle sent packet #{index}")
    
    # Slight delay to look like real streaming
    time.sleep(0.00001)

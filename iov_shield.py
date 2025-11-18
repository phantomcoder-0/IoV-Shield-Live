from kafka import KafkaConsumer
import json
import joblib
import pandas as pd
import numpy as np

# 1. Load the trained brain
print("Initializing IoV Shield...")
model = joblib.load('iov_brain.joblib')

# 2. Connect to the Live Stream
consumer = KafkaConsumer('iov_network',
                         bootstrap_servers='localhost:9092',
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))

print("SHIELD ACTIVE: Monitoring Traffic...")

# 3. Real-time Loop
for message in consumer:
    data = message.value
    
    # Prepare data for prediction (drop the label if it exists in simulation)
    df_row = pd.DataFrame([data])
    if 'class' in df_row.columns:
        df_row = df_row.drop(columns=['class'])
    
    # Quick Preprocessing (Simplification for demo)
    # In a full prod system, we load the exact encoders, here we force numeric conversion
    for col in df_row.columns:
        if df_row[col].dtype == 'object':
            df_row[col] = 0 # Simplified encoding for streaming demo
            
    # 4. PREDICT
    prediction = model.predict(df_row)[0]
    
    # 5. MITIGATION CONTROLLER
    if prediction == 11: # Assuming '11' is the code for Normal (checked from training)
        print(f"Packet Allowed: [Normal] - Source: {data.get('src_bytes')}")
    else:
        # --- ACTIVE MITIGATION ---
        print(f"!!! ALERT: ATTACK DETECTED !!! Type: {prediction}")
        print(f"--> ACTION: Dropping packet from Source IP.")
        print(f"--> ACTION: Alerting Traffic Control Center.")
        print("-" * 30)

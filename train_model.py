import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib

# 1. Load Data (Make sure kdd.csv is in the folder!)
print("Loading kdd.csv...")
columns = ['duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes', 'land', 'wrong_fragment', 'urgent', 'hot', 'num_failed_logins', 'logged_in', 'num_compromised', 'root_shell', 'su_attempted', 'num_root', 'num_file_creations', 'num_shells', 'num_access_files', 'num_outbound_cmds', 'is_host_login', 'is_guest_login', 'count', 'srv_count', 'serror_rate', 'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate', 'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count', 'dst_host_same_srv_rate', 'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate', 'dst_host_rerror_rate', 'dst_host_srv_rerror_rate', 'class']
try:
    df = pd.read_csv('kdd.csv', names=columns)
except FileNotFoundError:
    print("ERROR: kdd.csv not found! Please put the file in this folder.")
    exit()

# 2. Preprocessing
print("Training the AI model...")
# Encode text columns to numbers
encoders = {}
for col in ['protocol_type', 'service', 'flag', 'class']:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

# 3. Train
X = df.drop(columns=['class'])
y = df['class']
model = RandomForestClassifier(n_estimators=10, max_depth=10)
model.fit(X, y)

# 4. Save the brain
joblib.dump(model, 'iov_brain.joblib')
print("Model saved as 'iov_brain.joblib'")


cat > README.md << 'EOL'
🛡️ IoV Shield: Real-Time DDoS Defense for Internet of Vehicles

**IoV Shield** is a machine learning-based cybersecurity framework designed to detect and mitigate Distributed Denial of Service (DDoS) attacks in Internet of Vehicles (IoV) networks in real-time.

Using **Apache Kafka** for high-speed data streaming and **Scikit-Learn** for anomaly detection, this system acts as an intelligent firewall that filters malicious traffic while preserving critical safety messages.

🚀 Key Features
* **Real-Time Traffic Analysis:** Processes live network packets using a sliding window approach via Kafka.
* **ML-Powered Detection:** Uses a Random Forest classifier trained on the KDD Cup '99 dataset to identify attack signatures (Neptune, Smurf, etc.).
* **Active Mitigation:** Automatically flags and drops malicious packets to prevent network saturation.
* **CLI Monitoring:** Real-time logs and alerts directly in the terminal.

🛠️ Tech Stack
* **Core:** Python 3.10+
* **Streaming:** Apache Kafka, Zookeeper (Dockerized)
* **Machine Learning:** Scikit-Learn, Pandas, Joblib

⚙️ Installation

 1. Clone the Repository
    git clone [https://github.com/phantomcoder-0/IoV-Shield-Live.git](https://github.com/phantomcoder-0/IoV-Shield-Live.git)
    cd IoV-Shield-Live

 2. Set Up Environment
It is recommended to use a virtual environment.

    python3 -m venv venv
    source venv/bin/activate
    pip install pandas scikit-learn kafka-python joblib

 3. Start the Infrastructure (Kafka)
Ensure you have Docker installed.

    sudo docker-compose up -d

 4. Download the Dataset
The system requires the KDD Cup 99 dataset to simulate traffic.

    wget [http://kdd.ics.uci.edu/databases/kddcup99/kddcup.data_10_percent.gz](http://kdd.ics.uci.edu/databases/kddcup99/kddcup.data_10_percent.gz)
    gzip -d kddcup.data_10_percent.gz
    mv kddcup.data_10_percent kdd.csv

---

🚦 How to Run the Simulation

You will need **2 separate terminal windows** to run the full system.

 Step 1: Train the "Brain"
Before running the live system, train the AI model once.

    # In Terminal 1
    python train_model.py

 Step 2: Activate the Shield (Defender)
This script listens to the stream and logs decisions.

    # In Terminal 1 (after training)
    python iov_shield.py

 Step 3: Start Traffic Simulation (Attacker)
This script reads the dataset and blasts packets into the network.

    # In Terminal 2
    source venv/bin/activate
    python traffic_producer.py

---


📊 Project Architecture

1.  Traffic Producer: Simulates vehicles sending data (V2V/V2I) using historical attack data.
2.  Kafka Broker: The high-speed messaging backbone that handles the data stream.
3.  IoV Shield (Consumer): The AI engine that consumes packets, predicts validity, and executes mitigation logic.

---
*Created by [Rahul Siwach](https://github.com/phantomcoder-0)*
EOL

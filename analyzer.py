import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ipaddress


def load_server_logs(file_path):

    df = pd.read_csv(file_path)

    required_columns = [
        "timestamp",
        "ip_address",
        "method",
        "path",
        "status_code",
        "response_time"
    ]

    if df.empty:
        raise ValueError("Server log dataset is empty.")

    missing_columns = [
        col for col in required_columns
        if col not in df.columns
    ]

    if missing_columns:
        raise ValueError(f"Missing columns: {missing_columns}")

    if df[required_columns].isnull().any().any():
        raise ValueError("Server logs contain missing values.")

    # Convert data types
    df["timestamp"] = pd.to_datetime(
        df["timestamp"], errors="raise"
    )

    df["status_code"] = pd.to_numeric(
        df["status_code"], errors="raise"
    )

    df["response_time"] = pd.to_numeric(
        df["response_time"], errors="raise"
    )

    # Validate IP addresses
    for ip in df["ip_address"]:
        ipaddress.ip_address(ip)

    # Validate HTTP status codes
    if not df["status_code"].between(100, 599).all():
        raise ValueError("Invalid HTTP status code found.")

    if (df["response_time"] < 0).any():
        raise ValueError("Response time cannot be negative.")

    return df

def analyze_website_traffic(logs):

    total_requests = len(logs)

    unique_ips = logs["ip_address"].nunique()

    average_response_time = logs["response_time"].mean()

    # Count requests from each IP
    ip_requests = logs["ip_address"].value_counts()

    # Count HTTP status codes
    status_counts = logs["status_code"].value_counts().sort_index()

    # Count requests by HTTP method
    method_counts = logs["method"].value_counts()

    print("\n========== WEBSITE TRAFFIC ANALYSIS ==========")

    print(f"Total Requests: {total_requests}")
    print(f"Unique IP Addresses: {unique_ips}")
    print(f"Average Response Time: {average_response_time:.2f} ms")

    print("\n========== MOST ACTIVE IP ADDRESSES ==========")
    print(ip_requests)

    print("\n========== HTTP STATUS CODES ==========")
    print(status_counts)

    print("\n========== HTTP METHODS ==========")
    print(method_counts)

    return ip_requests, status_counts, method_counts



def detect_suspicious_ips(logs):

    # Filter unauthorized and forbidden requests
    failed_requests = logs[
        logs["status_code"].isin([401, 403])
    ]

    # Count failed requests per IP
    failed_ip_counts = (
        failed_requests.groupby("ip_address")
        .size()
        .reset_index(name="failed_requests")
    )

    # Identify suspicious IP addresses
    suspicious_ips = failed_ip_counts[
        failed_ip_counts["failed_requests"] >= 3
    ].copy()

    suspicious_ips["security_status"] = "SUSPICIOUS"

    print("\n========== SUSPICIOUS IP DETECTION ==========")

    if suspicious_ips.empty:
        print("No suspicious IP addresses detected.")
    else:
        print(suspicious_ips)

    return suspicious_ips

def detect_high_activity_ips(logs):
    ip_activity = (
        logs.groupby("ip_address")
        .size()
        .reset_index(name="total_requests")
    )

    high_activity = ip_activity[
        ip_activity["total_requests"] >= 4
    ].copy()

    high_activity["activity_status"] = "HIGH ACTIVITY"

    print("\n========== HIGH REQUEST ACTIVITY ==========")

    if high_activity.empty:
        print("No unusually active IP addresses found.")
    else:
        print(high_activity)

    return high_activity

def plot_traffic(ip_requests):
    plt.figure(figsize=(10, 5))

    ip_requests.plot(kind="bar")

    plt.title("Website Requests by IP Address")
    plt.xlabel("IP Address")
    plt.ylabel("Number of Requests")

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig("traffic_chart.png")
    plt.show()

    print("Traffic chart saved as traffic_chart.png")
    
def export_reports(ip_requests, status_counts, method_counts,
                   suspicious_ips, high_activity):

    traffic_report = pd.DataFrame({
        "IP Address": ip_requests.index,
        "Total Requests": ip_requests.values
    })

    traffic_report.to_csv("traffic_report.csv", index=False)

    security_report = pd.concat(
        [
            suspicious_ips.assign(detection_type="Failed Requests"),
            high_activity.assign(detection_type="High Activity")
        ],
        ignore_index=True
    )

    security_report.to_csv("security_report.csv", index=False)

    print("\nReports exported successfully!")
    print("traffic_report.csv")
    print("security_report.csv")
    

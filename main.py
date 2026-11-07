
from analyzer import (
    load_server_logs,
    analyze_website_traffic,
    detect_suspicious_ips,
    detect_high_activity_ips,
    plot_traffic,
    export_reports
)


def main():
    try:
        print("====================================")
        print(" WEBSITE SERVER LOG ANALYZER")
        print("====================================")

        # Step 1: Load and validate logs
        logs = load_server_logs("server_logs.csv")

        # Step 2: Analyze website traffic
        ip_requests, status_counts, method_counts = (
            analyze_website_traffic(logs)
        )

        # Step 3: Detect suspicious IP addresses
        suspicious_ips = detect_suspicious_ips(logs)

        # Step 4: Detect high request activity
        high_activity = detect_high_activity_ips(logs)

        # Step 5: Generate traffic visualization
        plot_traffic(ip_requests)

        # Step 6: Export reports
        export_reports(
            ip_requests,
            status_counts,
            method_counts,
            suspicious_ips,
            high_activity
        )

        print("\nAnalysis completed successfully!")

    except FileNotFoundError:
        print("Error: server_logs.csv was not found.")

    except (ValueError, KeyError) as error:
        print(f"Data validation error: {error}")

    except Exception as error:
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()

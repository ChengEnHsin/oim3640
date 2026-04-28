"""
Internship and Job Application Tracker
A Python-based application to track job applications, manage statuses, and analyze recruiting patterns.
"""

import json
import os
from datetime import datetime
from pathlib import Path


# File for persistent data storage
DATA_FILE = "applications.json"

# Application status options
VALID_STATUSES = ["Applied", "Under Review", "Interview Scheduled", "Rejected", "Offer Extended", "Offer Accepted"]

# Role categories for future analysis
ROLE_CATEGORIES = ["Software Engineering", "Product Management", "Data Science", "Operations", "Strategy", "Other"]


def load_applications():
    """Load applications from JSON file. Returns list of application dictionaries."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            print("Error reading data file. Starting fresh.\n")
            return []
    return []


def save_applications(applications):
    """Save applications to JSON file for persistence between runs."""
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(applications, f, indent=2)
        return True
    except IOError as e:
        print(f"Error saving data: {e}\n")
        return False


def add_application(applications):
    """Add a new application to the tracker."""
    print("\n--- Add New Application ---")
    
    company = input("Company name: ").strip()
    if not company:
        print("Company name cannot be empty.\n")
        return
    
    role = input("Job role/position: ").strip()
    if not role:
        print("Role cannot be empty.\n")
        return
    
    # Get date applied
    date_applied = input("Date applied (YYYY-MM-DD) or press Enter for today: ").strip()
    if not date_applied:
        date_applied = datetime.now().strftime("%Y-%m-%d")
    else:
        try:
            datetime.strptime(date_applied, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Using today's date.\n")
            date_applied = datetime.now().strftime("%Y-%m-%d")
    
    location = input("Location (city/remote): ").strip()
    if not location:
        location = "Not specified"
    
    status = "Applied"  # Default status for new applications
    
    # Create application dictionary
    application = {
        "id": len(applications) + 1,
        "company": company,
        "role": role,
        "date_applied": date_applied,
        "location": location,
        "status": status,
        "date_updated": datetime.now().strftime("%Y-%m-%d")
    }
    
    applications.append(application)
    save_applications(applications)
    print(f"\n✓ Application to {company} for {role} added successfully!\n")


def view_all_applications(applications):
    """Display all applications in formatted table."""
    if not applications:
        print("\nNo applications tracked yet.\n")
        return
    
    print("\n" + "="*120)
    print("ALL APPLICATIONS")
    print("="*120)
    print(f"{'ID':<4} {'Company':<20} {'Role':<25} {'Location':<15} {'Status':<20} {'Date Applied':<12}")
    print("-"*120)
    
    for app in applications:
        print(f"{app['id']:<4} {app['company']:<20} {app['role']:<25} {app['location']:<15} {app['status']:<20} {app['date_applied']:<12}")
    
    print("="*120 + "\n")


def view_application_details(applications):
    """View detailed information about a specific application."""
    if not applications:
        print("\nNo applications to view.\n")
        return
    
    view_all_applications(applications)
    
    try:
        app_id = int(input("Enter application ID to view details: "))
        app = next((a for a in applications if a["id"] == app_id), None)
        
        if app:
            print("\n" + "-"*50)
            print(f"Company:       {app['company']}")
            print(f"Role:          {app['role']}")
            print(f"Location:      {app['location']}")
            print(f"Date Applied:  {app['date_applied']}")
            print(f"Status:        {app['status']}")
            print(f"Last Updated:  {app['date_updated']}")
            print("-"*50 + "\n")
        else:
            print(f"Application ID {app_id} not found.\n")
    except ValueError:
        print("Invalid input. Please enter a valid ID number.\n")


def update_application_status(applications):
    """Update the status of an existing application."""
    if not applications:
        print("\nNo applications to update.\n")
        return
    
    view_all_applications(applications)
    
    try:
        app_id = int(input("Enter application ID to update: "))
        app = next((a for a in applications if a["id"] == app_id), None)
        
        if not app:
            print(f"Application ID {app_id} not found.\n")
            return
        
        print(f"\nCurrent status: {app['status']}")
        print("Available statuses:")
        for i, status in enumerate(VALID_STATUSES, 1):
            print(f"  {i}. {status}")
        
        try:
            choice = int(input("\nSelect new status (number): "))
            if 1 <= choice <= len(VALID_STATUSES):
                old_status = app['status']
                app['status'] = VALID_STATUSES[choice - 1]
                app['date_updated'] = datetime.now().strftime("%Y-%m-%d")
                save_applications(applications)
                print(f"\n✓ Status updated from '{old_status}' to '{app['status']}'!\n")
            else:
                print("Invalid choice.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")
    except ValueError:
        print("Invalid input. Please enter a valid ID number.\n")


def calculate_statistics(applications):
    """Calculate and display key metrics about applications."""
    if not applications:
        print("\nNo applications to analyze.\n")
        return
    
    total_apps = len(applications)
    
    # Count by status
    status_counts = {}
    for app in applications:
        status = app['status']
        status_counts[status] = status_counts.get(status, 0) + 1
    
    # Calculate response rate (Under Review, Interview Scheduled, Offer Extended, Offer Accepted)
    responded = sum(1 for app in applications if app['status'] in 
                   ["Under Review", "Interview Scheduled", "Offer Extended", "Offer Accepted"])
    response_rate = (responded / total_apps * 100) if total_apps > 0 else 0
    
    # Count by location
    location_counts = {}
    for app in applications:
        loc = app['location']
        location_counts[loc] = location_counts.get(loc, 0) + 1
    
    # Count rejections
    rejections = sum(1 for app in applications if app['status'] == "Rejected")
    rejection_rate = (rejections / total_apps * 100) if total_apps > 0 else 0
    
    print("\n" + "="*50)
    print("APPLICATION STATISTICS")
    print("="*50)
    print(f"Total Applications:     {total_apps}")
    print(f"Response Rate:          {response_rate:.1f}% ({responded}/{total_apps})")
    print(f"Rejection Rate:         {rejection_rate:.1f}% ({rejections}/{total_apps})")
    print(f"Offers Extended:        {status_counts.get('Offer Extended', 0)}")
    print(f"Offers Accepted:        {status_counts.get('Offer Accepted', 0)}")
    
    print("\nStatus Breakdown:")
    for status in VALID_STATUSES:
        count = status_counts.get(status, 0)
        print(f"  {status:<20} {count}")
    
    print("\nApplications by Location:")
    for location in sorted(location_counts.keys()):
        count = location_counts[location]
        print(f"  {location:<20} {count}")
    
    print("="*50 + "\n")


def delete_application(applications):
    """Delete an application from the tracker."""
    if not applications:
        print("\nNo applications to delete.\n")
        return
    
    view_all_applications(applications)
    
    try:
        app_id = int(input("Enter application ID to delete: "))
        app = next((a for a in applications if a["id"] == app_id), None)
        
        if not app:
            print(f"Application ID {app_id} not found.\n")
            return
        
        confirm = input(f"Delete application to {app['company']} for {app['role']}? (yes/no): ").strip().lower()
        if confirm == "yes":
            applications.remove(app)
            save_applications(applications)
            print("✓ Application deleted successfully!\n")
        else:
            print("Deletion cancelled.\n")
    except ValueError:
        print("Invalid input. Please enter a valid ID number.\n")


def display_menu():
    """Display the main menu options."""
    print("\n" + "="*50)
    print("INTERNSHIP TRACKER")
    print("="*50)
    print("1. Add new application")
    print("2. View all applications")
    print("3. View application details")
    print("4. Update application status")
    print("5. View statistics")
    print("6. Delete application")
    print("7. Exit")
    print("="*50)


def main():
    """Main program loop."""
    print("\n Welcome to InternTrack!")
    print("Your centralized internship and job application tracker.\n")
    
    applications = load_applications()
    
    while True:
        display_menu()
        choice = input("Select an option (1-7): ").strip()
        
        if choice == "1":
            add_application(applications)
        elif choice == "2":
            view_all_applications(applications)
        elif choice == "3":
            view_application_details(applications)
        elif choice == "4":
            update_application_status(applications)
        elif choice == "5":
            calculate_statistics(applications)
        elif choice == "6":
            delete_application(applications)
        elif choice == "7":
            print("\nThank you for using InternTrack. Good luck with your applications!\n")
            break
        else:
            print("Invalid option. Please select 1-7.\n")


if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import messagebox, ttk
import pymysql

# Database connection setup
db = pymysql.connect(
    host="localhost",
    user="root",
    password="tanya",  # Update with your own password
    database="bug_tracking_system"
)

# Main application class for the GUI
class BugTrackingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bug Tracking System")
        self.root.geometry("400x300")
        
        # Load the login screen on start
        self.login_screen()
    
    def login_screen(self):
        """Displays the login options for different roles."""
        # Clear the existing frame if any
        for widget in self.root.winfo_children():
            widget.destroy()
        
        tk.Label(self.root, text="Login as:", font=("Arial", 14)).pack(pady=20)
        
        # Button for Admin or Expert login
        tk.Button(self.root, text="Admin or Expert", font=("Arial", 12), command=self.admin_login).pack(pady=10)
        
        # Button for Customer login
        tk.Button(self.root, text="Customer", font=("Arial", 12), command=self.customer_login).pack(pady=10)
        
        # Button for creating a new account
        tk.Button(self.root, text="Create New Account", font=("Arial", 12), command=self.create_account).pack(pady=10)
    
    def admin_login(self):
        """Function for admin login (placeholder)."""
        # Here, you might add an actual login form with username/password fields
        self.admin_module()
    
    def customer_login(self):
        """Function for customer login (placeholder)."""
        # This function would handle the customer login details
        messagebox.showinfo("Info", "Customer login is under construction.")
    
    def create_account(self):
        """Function for creating a new customer account (placeholder)."""
        # This function would handle account creation
        messagebox.showinfo("Info", "Account creation is under construction.")
    
    def admin_module(self):
        """Displays the admin module screen."""
        # Clear the existing frame if any
        for widget in self.root.winfo_children():
            widget.destroy()
        
        tk.Label(self.root, text="Admin Module", font=("Arial", 16)).pack(pady=20)
        
        # Admin options
        tk.Button(self.root, text="Manage Services", font=("Arial", 12), command=self.manage_services).pack(pady=5)
        tk.Button(self.root, text="Manage Employees", font=("Arial", 12), command=self.manage_employees).pack(pady=5)
        tk.Button(self.root, text="Manage Bugs", font=("Arial", 12), command=self.manage_bugs).pack(pady=5)
        tk.Button(self.root, text="Logout", font=("Arial", 12), command=self.login_screen).pack(pady=20)
    
    def manage_services(self):
        """Function to manage services (placeholder)."""
        messagebox.showinfo("Info", "Service management is under construction.")
    
    def manage_employees(self):
        """Function to manage employees (placeholder)."""
        messagebox.showinfo("Info", "Employee management is under construction.")
    
    def manage_bugs(self):
        """Displays a list of bugs from the database in a new window."""
        # Create a new Toplevel window for displaying bugs
        bug_window = tk.Toplevel(self.root)
        bug_window.title("Bug List")
        bug_window.geometry("500x300")
        
        # Define the treeview for displaying bugs
        columns = ("Bug ID", "Description", "Status")
        tree = ttk.Treeview(bug_window, columns=columns, show="headings")
        tree.heading("Bug ID", text="Bug ID")
        tree.heading("Description", text="Description")
        tree.heading("Status", text="Status")
        tree.pack(fill=tk.BOTH, expand=True)
        
        # Connect to the database and fetch bug data
        cursor = db.cursor()
        query = "SELECT bug_id, description, status FROM bugs"  # Example query; adjust table/column names as needed
        
        try:
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                tree.insert("", tk.END, values=row)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch bugs: {e}")
        finally:
            cursor.close()

# Main Tkinter window
root = tk.Tk()
app = BugTrackingApp(root)
root.mainloop()

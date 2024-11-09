# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w2005142
# Date: 16/11/2023

# Use graphics.py file (Reference: Week 4/5 lecture - graphics.py)
from graphics import *   

# Automatic message to welcome university staff member before input of results (Reference: Week 1 lecture - Introduction to Module & Programming with Python)
print ('Welcome, this is the university progression results program!')

# Dictionary based on table to represent the combination of results (Reference: Week 7 lecture - Lists (&tuples, dictionaries)/ w3schools.com/python/gloss_python_dictionary.asp)
progression_table = {
    (120, 0, 0): "Progress", # Possibility 1
    (100, 20, 0): "Progress (module trailer)", # Possibility 2
    (100, 0, 20): "Progress (module trailer)", # Possibility 3
    (80, 40, 0): "Do not Progress (module retriever)", # Possibility 4
    (80, 20, 20): "Do not Progress (module retriever)", # Possibility 5
    (80, 0, 40): "Do not Progress (module retriever)", # Possibility 6
    (60, 60, 0): "Do not Progress (module retriever)", # Possibility 7
    (60, 40, 20): "Do not Progress (module retriever)", # Possibility 8 
    (60, 20, 40): "Do not Progress (module retriever)", # Possibility 9
    (60, 0, 60): "Do not Progress (module retriever)", # Possibility 10
    (40, 80, 0): "Do not Progress (module retriever)", # Possibility 11
    (40, 60, 20): "Do not Progress (module retriever)", # Possibility 12
    (40, 40, 40): "Do not Progress (module retriever)", # Possibility 13
    (40, 20, 60): "Do not Progress (module retriever)", # Possibility 14
    (40, 0, 80): "Exclude", # Possibility 15
    (20, 100, 0): "Do not Progress (module retriever)", # Possibility 16
    (20, 80, 20): "Do not Progress (module retriever)", # Possibility 17
    (20, 60, 40): "Do not Progress (module retriever)", # Possibility 18
    (20, 40, 60): "Do not Progress (module retriever)", # Possibility 19
    (20, 20, 80): "Exclude", # Possibility 20
    (20, 0, 100): "Exclude", # Possibility 21
    (0, 120, 0): "Do not Progress (module retriever)", # Possibility 22
    (0, 100, 20): "Do not Progress (module retriever)", # Possibility 23
    (0, 80, 40): "Do not Progress (module retriever)", # Possibility 24
    (0, 60, 60): "Do not Progress (module retriever)", # Possibility 25
    (0, 40, 80): "Exclude", # Possibility 26
    (0, 20, 100): "Exclude", # Possibility 27
    (0, 0, 120): "Exclude", # Possibility 28
}

# Defined function to provide better functionality when using codes from graphics.py (Reference: Week 8 lecture - User-defined functions/ Week 4/5 lecture - graphics.py)
def draw_histogram_window(result_counts):
    try: # Statement to prevent the program from crashing (Reference: Week 2 lecture - Built-in functions, input etc.)
        win = GraphWin("Results Histogram", 600, 500) # Name of the window and dimensions (Reference: Week 4/5 lecture - graphics.py)
        win.setBackground("azure3") # Background color of the window (Reference: Week 4/5 lecture - graphics.py)

        students_total = sum(result_counts.values()) # Sum of the students from dictionary inputs (Reference: Week 2 lecture - Built-in functions, input etc.)
        
        # Widht of the bar, size, coordinates and distance between the columns (Reference: Week 4/5 lecture - graphics.py)
        bar_width = 100 
        x_start = 80
        x_spacing = 105  
        label_spacing = 20
        label_size = 14

        # Postion for bars and to increase bar height (Reference: Week 4/5 lecture - graphics.py)
        x = x_start
        y_scale = 15 
        y_start = 300

        # Abbreviation of results for easier visualization (Reference: Week 7 lecture - Lists (&tuples, dictionaries))
        result = {
            "Progress": "Progress",
            "Progress (module trailer)": "Trailer",
            "Do not Progress (module retriever)": "Retriever",
            "Exclude": "Excluded"
        }

        # Colors defined for easier bar visualization (Reference: Week 7 lecture - Lists (&tuples, dictionaries))
        result_colors = {
            "Progress": "green",
            "Trailer": "blue",
            "Retriever": "orange",
            "Excluded": "red"
        }

        # Title of the histogram, coordinates, label size and style for display (Reference: Week 4/5 lecture - graphics.py)
        result_label = Text(Point(300, 30), "Progression results:")
        result_label.setSize(18)
        result_label.setStyle("bold")
        result_label.draw(win)
        
        # Width and coordinate to display horizontal line at the base of columns (Reference: Week 4/5 lecture - graphics.py)
        horizontal_line = Line(Point(x_start, y_start), Point(x + (len(result) - 2) * (bar_width + x_spacing), y_start))
        horizontal_line.setWidth(0.5)  
        horizontal_line.draw(win) 

        
        for result, abbreviation_name in result.items(): # Loop entries from dictionary (Reference: Week 4 lecture - Loops/ w3schools.com/python/python_for_loops.asp)
            count = result_counts.get(result, 0) # Count set access inputs (Reference: Week 7 lecture - Lists (&tuples, dictionaries)
            bar_height = count * y_scale # Height based on number of inputs (Reference: Week 4/5 lecture - graphics.py)
            bar = Rectangle(Point(x, y_start), Point(x + bar_width, y_start - bar_height)) # Rectangle is created based on the inputs (Reference: Week 4/5 lecture - graphics.py)
            bar.setFill(result_colors[abbreviation_name]) # Color used from abbreviation dictionary (Reference: Week 4/5 lecture - graphics.py)
            bar.draw(win) # Display the bar (Reference: Week 4/5 lecture - graphics.py)
            
            # Label position and size under bar for visualization (Reference: Week 4/5 lecture - graphics.py)
            label = Text(Point(x + bar_width / 2, y_start + label_spacing), abbreviation_name) 
            label.setSize(label_size)
            label.draw(win)

            # Position, size, style and color for visualization of the amount of students for each result bar (Reference: Week 4/5 lecture - graphics.py)
            count_label = Text(Point(x + bar_width / 2, y_start - bar_height / 2), str(count))
            count_label.setSize(14)
            count_label.setStyle("bold")
            count_label.setTextColor("white")  
            count_label.draw(win)

            x += x_spacing # Assign the bar to move as it loops (Reference: Week 1 lecture - Introduction to Module & Programming with Python/ Week 4/5 lecture - graphics.py)

        # Show total number of students entered 
        total_label = Text(Point(300, 480), f"Total Students: {students_total}") # Formatted string from previous variable (Reference: Week 8 lecture - User-defined functions) 
        total_label.setSize(18) # Size of label (Reference: Week 4/5 lecture - graphics.py)
        total_label.draw(win) # Display (Reference: Week 4/5 lecture - graphics.py)

        # Histogram is closed after click from user (Reference: Week 4/5 lecture - graphics.py)
        win.getMouse() 
        win.close()
    except GraphicsError: # Set to avoid error when user clicks (Reference: Week 4/5 lecture - graphics.py)
        pass  


    
# Defined function to get entries and predict actions (Reference: Week 8 lecture - User-defined functions)
def main():
    result_counts = { # Set to 0 to count number of inputs for each result from dictionary (Reference: Week 7 lecture - Lists (&tuples, dictionaries))
        "Progress": 0,
        "Progress (module trailer)": 0,
        "Do not progress (module retriever)": 0,
        "Exclude": 0,
    }
    while True: # Loop for data being inputed until is not accepted (Reference: Week 4 lecture - Loops)
        try: # Block of code to respond from user input (Reference: Week 2 lecture - Built-in functions, input etc.)
            pass_credits = int(input("Enter the number of credits at pass (0, 20, 40, 60, 80, 100 or 120): ")) # Set for user to input specific integers (Reference: Week 2 lecture - Built-in functions, input etc.)
            if pass_credits not in [0, 20, 40, 60, 80, 100, 120]: # Validate integer input from user, if not among the numbers, a message will be displayed required a valid integer (Reference: Week 3 lecture - Conditions)
                print("Pass credit entered is out of range! Please enter a valid number.") # Message displayed for integer out of range (Reference: Week 3 lecture - Conditions)
                continue  # Loop restarts

            defer_credits = int(input("Enter the number of credits at defer (0, 20, 40, 60, 80, 100 or 120): ")) # Set for user to input specific integers (Reference: Week 2 lecture - Built-in functions, input etc.)
            if defer_credits not in [0, 20, 40, 60, 80, 100, 120]: # Validate integer input from user, if not among the numbers, a message will be displayed requiring a valid integer (Reference: Week 3 lecture - Conditions)
                print("Defer credit entered is out of range! Please enter a valid number.") # Message displayed for integer out of range (Reference: Week 3 lecture - Conditions)
                continue  # Loop restarts

            fail_credits = int(input("Enter the number of credits at fail (0, 20, 40, 60, 80, 100 or 120): ")) # Set for user to input specific integers (Reference: Week 2 lecture - Built-in functions, input etc.)
            if fail_credits not in [0, 20, 40, 60, 80, 100, 120]: # Validate integer input from user, if not among the numbers (Reference: Week 3 lecture - Conditions)
                print("Fail credit entered is out of range! Please enter a valid number.") # Message displayed for integer out of range (Reference: Week 3 lecture - Conditions)
                continue  # Loop restarts

            total_credits = pass_credits + defer_credits + fail_credits # Sum of credit inputs (Reference: Week 2 lecture - Built-in functions, input etc.)
            if total_credits != 120: # If the sum of credits is not equal to 120, a message will be displayed (Reference: Week 3 lecture - Conditions)
                print("Total credits incorrect! (Not equal to 120).") # Message displayed for total not equal to 120 (Reference: Week 3 lecture - Conditions)
                continue  # Loop restarts

            result = progression_table.get((pass_credits, defer_credits, fail_credits), "Invalid credits") # Set to check if the combination is in the dictionary (Reference: Week 7 lecture - Lists (&tuples, dictionaries)

            result_key = result.replace("–", "-") # Assigned to avoid errors with dictionary (Reference: Week 2 lecture - Built-in functions, input etc.)
            
            print(f"Progression Result: {result}") # After validation of credit values, message displays the progression that matches the dictionary (Reference: Week 2 lecture - Built-in functions, input etc.)

            # Count number of results input from dictionary (Reference: Week 3 lecture - Conditions)
            if result_key in result_counts:
                result_counts[result_key] += 1
            else:
                result_counts[result_key] = 1

            while True: # Loop for data being inputed until is not accepted (Reference: Week 4 lecture - Loops)
                continue_message = input("Do you want to add another student result? Enter 'y' to continue or 'q' to quit: ").lower() # Set for user to input 'y' to continue or 'q' to quit and display (Reference: Week 2 lecture - Built-in functions, input etc.)
                if continue_message == "q": # When 'q' is entered the histogram screen is launched (Reference: Week 3 lecture - Conditions)
                    draw_histogram_window(result_counts) # Histogram window displayed (Reference: Week 4/5 lecture - graphics.py)
                    return  # Program stops when 'q' is entered (Reference: Week 3 lecture - Conditions)
                elif continue_message == "y": # When 'y' is entered, the user can continue input credits (Reference: Week 3 lecture - Conditions)
                    break # The credits are still being accepted (Reference: Week 3 lecture - Conditions)
                else: # If 'y' or 'q' are not entered, a message is displayed (Reference: Week 3 lecture - Conditions)
                    print("Please only enter 'y' or 'q'.") # Message to require only 'y' or 'q' (Reference: Week 3 lecture - Conditions)

        except ValueError: # Display an error message to validate integer input (Reference: Week 3 lecture - Conditions)
            print("Integer required! Please enter valid credit values.") # Message displayed (Reference: Week 3 lecture - Conditions)

if __name__ == "__main__": # Created from the relation of the tasks performed when program executes (Reference: Week 8 lecture - User-defined functions/ wiki.python.org)
    main()

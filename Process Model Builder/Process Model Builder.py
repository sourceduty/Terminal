# Process Model Builder

# Copyright (C) 2024, Sourceduty - All Rights Reserved.

# A terminal-based Python program for building and saving process models.
# Includes options for Super, High, Medium, and Low Process Architecture Levels.
# Includes advanced features for architecture levels, arrows, step customization, descriptions, priorities, and validation.

import os

def main():
    print_help_menu()
    while True:
        print("\nMain Menu:")
        print("1. Build Process Model")
        print("2. View Help")
        print("3. Exit")
        main_choice = input("Enter your choice (1-3): ").strip()

        if main_choice == '1':
            select_architecture_level()
        elif main_choice == '2':
            print_help_menu()
        elif main_choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def print_help_menu():
    print("\nOptimized Advanced Process Model Builder")
    print("This program allows you to build detailed and customized process models step-by-step.")
    print("\nKey Features:")
    print("1. Four architecture levels: Super, High, Medium, and Low.")
    print("2. Customizable step types, descriptions, priorities, and arrows.")
    print("3. Options to reorder, delete, and edit steps.")
    print("4. Save models to a text file.")
    print("\nHow to Use:")
    print("1. Select 'Build Process Model' to start.")
    print("2. Follow prompts to add, customize, and manage steps.")
    print("3. Save the completed model.")
    print("4. Use 'View Help' for guidance.")

def select_architecture_level():
    print("\nSelect the Process Architecture Level:")
    levels = ["Super Level", "High Level", "Medium Level", "Low Level"]
    for i, level in enumerate(levels, start=1):
        print(f"{i}. {level}")
    try:
        level_choice = int(input("Enter your choice (1-4): ").strip())
        if 1 <= level_choice <= 4:
            build_process_model(levels[level_choice - 1])
        else:
            print("Invalid choice. Returning to main menu.")
    except ValueError:
        print("Invalid input. Returning to main menu.")

def build_process_model(level):
    print(f"\nBuilding a {level} Process Model")
    process_model = []

    while True:
        print("\nProcess Step Menu:")
        print("1. Add a new step")
        print("2. Edit an existing step")
        print("3. Reorder steps")
        print("4. Delete a step")
        print("5. Customize arrows")
        print("6. View current model")
        print("7. Finish and save model")
        step_choice = input("Enter your choice (1-7): ").strip()

        if step_choice == '1':
            add_step(process_model)
        elif step_choice == '2':
            edit_step(process_model)
        elif step_choice == '3':
            reorder_steps(process_model)
        elif step_choice == '4':
            delete_step(process_model)
        elif step_choice == '5':
            customize_arrows(process_model)
        elif step_choice == '6':
            display_model(process_model)
        elif step_choice == '7':
            if process_model:
                display_model(process_model)
                save_option = input("Would you like to save this model to a file? (yes/no): ").strip().lower()
                if save_option == 'yes':
                    save_model(level, process_model)
            else:
                print("No steps to save. Returning to main menu.")
            break
        else:
            print("Invalid choice. Please try again.")

def add_step(process_model):
    step_name = input("Enter the name of the process step: ").strip()
    step_type = select_step_type()
    description = input("Enter a description for this step (optional): ").strip()
    priority = input("Enter the priority for this step (High, Medium, Low, or leave blank): ").strip()
    
    step_details = f"{step_name} {step_type}"
    if description:
        step_details += f" - {description}"
    if priority:
        step_details += f" (Priority: {priority})"
    
    process_model.append(step_details)

def select_step_type():
    print("\nSelect step type:")
    step_types = {
        "1": "[Standard]",
        "2": "[Decision]",
        "3": "[Parallel]",
        "4": "[End]"
    }
    for key, value in step_types.items():
        print(f"{key}. {value}")
    choice = input("Enter your choice (1-4): ").strip()
    return step_types.get(choice, "[Standard]")

def edit_step(process_model):
    if not process_model:
        print("No steps to edit. Add steps first.")
        return
    display_model(process_model)
    try:
        index = int(input("Enter the position of the step to edit (1-based index): ").strip()) - 1
        if 0 <= index < len(process_model):
            print(f"Editing step: {process_model[index]}")
            add_step(process_model[index])
            process_model[index] = add_step(process_model)
            print("Step edited successfully.")
        else:
            print("Invalid position. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def reorder_steps(process_model):
    if not process_model:
        print("No steps to reorder. Add steps first.")
        return
    display_model(process_model)
    try:
        old_index = int(input("Enter the current position of the step to move (1-based index): ")) - 1
        new_index = int(input("Enter the new position for this step (1-based index): ")) - 1
        if 0 <= old_index < len(process_model) and 0 <= new_index < len(process_model):
            step = process_model.pop(old_index)
            process_model.insert(new_index, step)
            print("Step reordered successfully.")
        else:
            print("Invalid positions. Please try again.")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

def delete_step(process_model):
    if not process_model:
        print("No steps to delete. Add steps first.")
        return
    display_model(process_model)
    try:
        index = int(input("Enter the position of the step to delete (1-based index): ")) - 1
        if 0 <= index < len(process_model):
            removed_step = process_model.pop(index)
            print(f"Step '{removed_step}' deleted successfully.")
        else:
            print("Invalid position. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def customize_arrows(process_model):
    if not process_model:
        print("No steps to customize. Add steps first.")
        return
    print("\nArrow Options:")
    arrows = {
        "1": "→",
        "2": "←",
        "3": "↔",
        "4": "⇄"
    }
    for key, value in arrows.items():
        print(f"{key}. {value}")
    choice = input("Select the arrow type (1-4): ").strip()
    arrow = arrows.get(choice, "→")
    for i in range(len(process_model) - 1):
        process_model[i] = f"{process_model[i]} {arrow}"

def display_model(process_model):
    if not process_model:
        print("No steps in the model yet.")
        return
    print("\nCurrent Process Model:")
    print(" → ".join(process_model))

def save_model(level, process_model):
    filename = input("Enter the filename to save the model (e.g., model.txt): ").strip()
    try:
        with open(filename, "w") as file:
            file.write(f"{level} Process Model\n")
            file.write(" → ".join(process_model))
            file.write("\n")
        print(f"Model successfully saved to {filename}.")
    except Exception as e:
        print(f"Error saving file: {e}")

if __name__ == "__main__":
    main()

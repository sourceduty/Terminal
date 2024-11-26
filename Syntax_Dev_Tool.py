import re

class LanguageSyntax:
    def __init__(self):
        self.syntax_rules = {}

    def suggest_syntax(self, rule_name):
        # Suggest helpful syntax examples based on the rule name
        suggestions = {
            'variable': "variable = identifier, e.g., x = 10",
            'function': "function definition, e.g., def function_name():",
            'operator': "operator use, e.g., +, -, *, /",
            'if': "if condition, e.g., if x > 10:",
            'while': "while loop, e.g., while x < 5:",
            'class': "class definition, e.g., class MyClass:",
            'return': "return statement, e.g., return x",
            'for': "for loop, e.g., for i in range(10):",
            'try': "try block, e.g., try: <statements> except Exception as e:",
            'import': "import statement, e.g., import math"
        }
        return suggestions.get(rule_name, "Enter the definition for the rule:")

    def add_rule(self):
        print("\nEnter the name of the rule (e.g., 'variable', 'function', 'operator', 'if', 'while', 'class', 'return'): ")
        rule_name = input("> ").lower().strip()
        
        if rule_name in self.syntax_rules:
            print(f"Rule '{rule_name}' already exists. Try a different name.")
            return
        
        print("\nSuggested Syntax:")
        suggestion = self.suggest_syntax(rule_name)
        print(f"Example: {suggestion}")
        
        print("\nPlease enter the syntax definition for this rule (e.g., format, usage, example):")
        rule_definition = input("> ").strip()
        
        # Basic validation for common syntax patterns
        if not rule_definition:
            print("Error: You must provide a definition for this rule.")
            return
        
        self.syntax_rules[rule_name] = rule_definition
        print(f"Rule '{rule_name}' added successfully.")

    def display_rules(self):
        if not self.syntax_rules:
            print("\nNo syntax rules defined.")
        else:
            print("\nCurrent syntax rules:")
            for rule, definition in self.syntax_rules.items():
                print(f"{rule}: {definition}")

    def modify_rule(self):
        print("\nEnter the name of the rule to modify:")
        rule_name = input("> ").lower().strip()
        
        if rule_name not in self.syntax_rules:
            print(f"Rule '{rule_name}' does not exist.")
            return
        
        print("\nSuggested Syntax:")
        suggestion = self.suggest_syntax(rule_name)
        print(f"Example: {suggestion}")
        
        print("\nEnter the new definition for the rule:")
        new_definition = input("> ").strip()
        
        if not new_definition:
            print("Error: You must provide a new definition.")
            return
        
        self.syntax_rules[rule_name] = new_definition
        print(f"Rule '{rule_name}' updated successfully.")

    def delete_rule(self):
        print("\nEnter the name of the rule to delete:")
        rule_name = input("> ").lower().strip()
        
        if rule_name not in self.syntax_rules:
            print(f"Rule '{rule_name}' does not exist.")
            return
        
        del self.syntax_rules[rule_name]
        print(f"Rule '{rule_name}' deleted successfully.")

    def validate_syntax(self, rule_name, rule_definition):
        # Check if the definition contains basic language structure
        if rule_name == 'variable':
            # Variables should contain an assignment, e.g., x = 10
            if not re.match(r"^\w+\s*=\s*.+", rule_definition):
                return "Invalid variable assignment syntax. Example: x = 10"
        
        elif rule_name == 'function':
            # Function should start with def and contain parentheses
            if not re.match(r"^def\s+\w+\(.*\):", rule_definition):
                return "Invalid function definition. Example: def my_function():"
        
        elif rule_name == 'if' or rule_name == 'while':
            # Conditions should start with 'if' or 'while' and have a logical expression
            if not re.match(r"^(if|while)\s+\w+\s*(==|!=|<|>|<=|>=)\s*\w+:", rule_definition):
                return f"Invalid syntax for {rule_name}. Example: {rule_name} x > 10:"
        
        return None

    def run(self):
        while True:
            print("\nProgramming Language Syntax Development Terminal")
            print("1. Add a new syntax rule")
            print("2. Display all syntax rules")
            print("3. Modify an existing rule")
            print("4. Delete a rule")
            print("5. Exit")
            
            choice = input("\nChoose an option (1-5): ").strip()
            
            if choice == '1':
                self.add_rule()
            elif choice == '2':
                self.display_rules()
            elif choice == '3':
                self.modify_rule()
            elif choice == '4':
                self.delete_rule()
            elif choice == '5':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    language_syntax = LanguageSyntax()
    language_syntax.run()

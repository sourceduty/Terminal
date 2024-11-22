import cmd

class RelativityCalculator(cmd.Cmd):
    intro = ('Relativity Calculator\n\n'
             'This program allows you to calculate phenomena from Einstein\'s theories of Special and General Relativity.\n'
             'Explore how significant relativistic effects become at speeds approaching the speed of light or near massive objects.\n\n'
             '--------------------------------------------------------------------------------\n\n'
             'Select an option by typing a number or command name and press Enter.\n\n'
             '  1: Calculate time dilation (Special Relativity)\n'
             '  2: Calculate length contraction (Special Relativity)\n'
             '  3: Calculate gravitational time dilation (General Relativity)\n'
             '  4: Calculate relativistic mass increase (Special Relativity)\n'
             '  5: Exit\n\n'
             
             'Type help or ? to list commands.\n\n')

    prompt = '> '

    def do_time(self, arg):
        'Calculate time dilation due to velocity (Special Relativity): time'
        try:
            t = float(input("Enter the proper time (in seconds): "))
            v = float(input("Enter the velocity of the moving object as a fraction of the speed of light (0 < v < 1): "))
            gamma = 1 / (1 - v**2)**0.5
            dilated_time = gamma * t
            print(f"Dilated Time: {dilated_time} seconds")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        except Exception as e:
            print("An error occurred: ", str(e))

    def do_length(self, arg):
        'Calculate length contraction (Special Relativity): length'
        try:
            l = float(input("Enter the rest length (in meters): "))
            v = float(input("Enter the velocity of the moving object as a fraction of the speed of light (0 < v < 1): "))
            gamma = 1 / (1 - v**2)**0.5
            contracted_length = l / gamma
            print(f"Contracted Length: {contracted_length} meters")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        except Exception as e:
            print("An error occurred: ", str(e))

    def do_gravitational_time(self, arg):
        'Calculate gravitational time dilation (General Relativity): gravitational_time'
        try:
            t = float(input("Enter the time experienced far from the massive object (in seconds): "))
            M = float(input("Enter the mass of the object (in kilograms): "))
            r = float(input("Enter the distance from the center of the mass (in meters): "))
            G = 6.67430e-11  # gravitational constant
            c = 299792458  # speed of light in m/s
            factor = (1 - (2 * G * M) / (r * c**2))**0.5
            dilated_time = t / factor
            print(f"Gravitational Dilated Time: {dilated_time} seconds")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        except Exception as e:
            print("An error occurred: ", str(e))

    def do_mass(self, arg):
        'Calculate relativistic mass increase (Special Relativity): mass'
        try:
            m0 = float(input("Enter the rest mass (in kilograms): "))
            v = float(input("Enter the velocity of the moving object as a fraction of the speed of light (0 < v < 1): "))
            gamma = 1 / (1 - v**2)**0.5
            relativistic_mass = m0 * gamma
            print(f"Relativistic Mass: {relativistic_mass} kilograms")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        except Exception as e:
            print("An error occurred: ", str(e))

    def do_exit(self, arg):
        'Exit the calculator: exit'
        print("Thank you for using the Relativity Calculator.")
        return True

    def postcmd(self, stop, line):
        if not stop:
            print("\n--------------------------------------------------------------------------------")
            print("Select another option or type 'exit' to leave:")
            print('  1: Calculate time dilation (Special Relativity)')
            print('  2: Calculate length contraction (Special Relativity)')
            print('  3: Calculate gravitational time dilation (General Relativity)')
            print('  4: Calculate relativistic mass increase (Special Relativity)')
            print('  5: Exit')
            print("--------------------------------------------------------------------------------")
        return stop

    def default(self, line):
        choices = { '1': self.do_time, '2': self.do_length, '3': self.do_gravitational_time, '4': self.do_mass, '5': self.do_exit }
        if line in choices:
            choices[line]('')
        else:
            print(f"'{line}' is not a valid command. Please type a valid number or 'exit'.")

if __name__ == '__main__':
    RelativityCalculator().cmdloop()

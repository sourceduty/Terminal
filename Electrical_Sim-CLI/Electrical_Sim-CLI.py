import cmd
import json
import os

class ElectricalSimulationCLI(cmd.Cmd):
    intro = (
        'WELCOME TO SOURCEDUTY ELECTRICAL SIMULATIONS.\n'
        'TYPE HELP OR ? TO LIST COMMANDS.\n'
        'SUGGESTED INPUTS:\n'
        '  - select <component> <value>: add a component to your circuit.\n'
        '  - set <parameter> <value>: set simulation parameters.\n'
        '  - sim <circuit_definition>: run a simulation.\n'
        '  - show: display current components in the circuit.\n'
        '  - save <filename>: save the current simulation state.\n'
        '  - load <filename>: load a saved simulation state.\n'
        '  - templates: list available circuit templates.\n'
        '  - examples: list available example simulations.\n'
        '  - exit: exit the simulator.\n'
    )
    prompt = '(simulator) '

    # Predefined circuit templates and example simulations
    templates = {
        'series_resistor': 'R1: 100 Ohms, R2: 200 Ohms',
        'parallel_resistor': 'R1: 100 Ohms, R2: 200 Ohms',
        'simple_rc_circuit': 'R: 100 Ohms, C: 10uF, V: 5V',
        'rl_circuit': 'R: 100 Ohms, L: 10mH, V: 5V',
        'rc_circuit': 'R: 100 Ohms, C: 10uF',
        'rcl_circuit': 'R: 100 Ohms, L: 10mH, C: 10uF, V: 5V',
        'voltage_divider': 'R1: 100 Ohms, R2: 200 Ohms, V: 10V',
    }

    examples = {
        'series_resistor': 'Example simulation of two resistors in series.',
        'parallel_resistor': 'Example simulation of two resistors in parallel.',
        'simple_rc_circuit': 'Example simulation of a simple RC circuit with a capacitor charging.',
        'rl_circuit': 'Example simulation of an RL circuit with a voltage source.',
        'rc_circuit': 'Example simulation of an RC circuit.',
        'rcl_circuit': 'Example simulation of an RLC circuit.',
        'voltage_divider': 'Example simulation of a voltage divider circuit.',
    }

    # Available components
    components = {
        'resistor': 'R',
        'capacitor': 'C',
        'inductor': 'L',
        'voltage_source': 'V',
        'current_source': 'I',
        'diode': 'D',
        'transistor': 'Q',
        'led': 'LED',
        'op_amp': 'OPAMP',
        'ground': 'GND',
    }

    def __init__(self):
        super().__init__()
        self.current_circuit = []
        self.default_params = {
            'voltage': 5,  # Default voltage
            'frequency': 50  # Default frequency for AC circuits
        }

    def do_sim(self, arg):
        'RUN A CIRCUIT SIMULATION: sim <circuit_definition>'
        if arg:
            print(f"SIMULATING CIRCUIT: {arg}")
            # Placeholder for simulation logic
            print("Simulation completed successfully!")
        else:
            print("PLEASE PROVIDE A CIRCUIT DEFINITION. EXAMPLE: sim 'R1: 100 Ohms, R2: 200 Ohms'.")

    def do_select(self, arg):
        'SELECT COMPONENTS: select <component> <value>'
        if arg:
            try:
                component, value = arg.split()
                if component in self.components.keys():
                    if len(self.current_circuit) < 100:
                        self.current_circuit.append({component: value})
                        print(f"ADDED {component} WITH VALUE {value}. CURRENT COMPONENTS: {len(self.current_circuit)}")
                    else:
                        print("CANNOT ADD MORE THAN 100 COMPONENTS.")
                else:
                    print("INVALID COMPONENT. AVAILABLE COMPONENTS ARE:", ', '.join(self.components.keys()))
            except ValueError:
                print("INVALID INPUT. PLEASE PROVIDE A COMPONENT AND ITS VALUE. EXAMPLE: select resistor 100 Ohms")
        else:
            print("PLEASE PROVIDE A COMPONENT AND ITS VALUE.")

    def do_set(self, arg):
        'SET SIMULATION PARAMETERS: set <parameter> <value>'
        if arg:
            try:
                param, value = arg.split()
                self.default_params[param.lower()] = value
                print(f"SET {param} TO {value}")
            except ValueError:
                print("INVALID INPUT. PLEASE PROVIDE A PARAMETER AND ITS VALUE. EXAMPLE: set voltage 5V")
        else:
            print("PLEASE PROVIDE A PARAMETER AND ITS VALUE.")

    def do_show(self, arg):
        'SHOW CURRENT COMPONENTS: show'
        print("CURRENT CIRCUIT COMPONENTS:")
        if not self.current_circuit:
            print("NO COMPONENTS IN THE CIRCUIT.")
        else:
            for component in self.current_circuit:
                print(component)

    def do_save(self, arg):
        'SAVE THE CURRENT SIMULATION STATE: save <filename>'
        if arg:
            with open(arg, 'w') as f:
                state = {
                    'components': self.current_circuit,
                    'default_params': self.default_params,
                    'description': 'CURRENT SIMULATION STATE'
                }
                f.write(json.dumps(state, indent=4))
            print(f"SIMULATION STATE SAVED TO {arg}.")
        else:
            print("PLEASE PROVIDE A FILENAME TO SAVE THE SIMULATION STATE.")

    def do_load(self, arg):
        'LOAD A PREVIOUSLY SAVED SIMULATION: load <filename>'
        if arg:
            try:
                with open(arg, 'r') as f:
                    state = json.load(f)
                    self.current_circuit = state.get('components', [])
                    self.default_params = state.get('default_params', self.default_params)
                    print(f"LOADED SIMULATION STATE: {self.current_circuit}")
            except FileNotFoundError:
                print("FILE NOT FOUND. PLEASE CHECK THE FILENAME.")
        else:
            print("PLEASE PROVIDE A FILENAME TO LOAD THE SIMULATION STATE.")

    def do_templates(self, arg):
        'LIST AVAILABLE CIRCUIT TEMPLATES: templates'
        print("AVAILABLE CIRCUIT TEMPLATES:")
        for template in self.templates.keys():
            print(template)

    def do_examples(self, arg):
        'LIST AVAILABLE EXAMPLE SIMULATIONS: examples'
        print("AVAILABLE EXAMPLE SIMULATIONS:")
        for example in self.examples.keys():
            print(example)

    def do_example(self, arg):
        'RUN AN EXAMPLE SIMULATION: example <template_name>'
        if arg:
            arg = arg.lower()
            if arg in self.examples:
                print(f"RUNNING EXAMPLE: {arg} - {self.examples[arg]}")
                # Logic to simulate the example would go here
                print("Example simulation completed successfully!")
            else:
                print("AVAILABLE EXAMPLES ARE:", ', '.join(self.examples.keys()))
        else:
            print("PLEASE PROVIDE A TEMPLATE NAME. EXAMPLE: example series_resistor")

    def complete_example(self, text, line, begidx, endidx):
        """Auto-complete example names."""
        if text:
            completions = [ex for ex in self.examples.keys() if ex.startswith(text.lower())]
        else:
            completions = list(self.examples.keys())
        return completions

    def complete_templates(self, text, line, begidx, endidx):
        """Auto-complete template names."""
        if text:
            completions = [temp for temp in self.templates.keys() if temp.startswith(text.lower())]
        else:
            completions = list(self.templates.keys())
        return completions

    def do_clear(self, arg):
        'CLEAR THE CLI: clear'
        os.system('cls' if os.name == 'nt' else 'clear')
        print("CLI CLEARED.")

    def do_exit(self, arg):
        'EXIT THE CLI: exit'
        print("EXITING THE SIMULATOR. GOODBYE!")
        return True

    def do_help(self, arg):
        'LIST AVAILABLE COMMANDS: help or help <command>'
        if arg:
            print(self.help_commands.get(arg, "NO HELP AVAILABLE FOR THAT COMMAND."))
        else:
            print(self.intro)
            print("AVAILABLE COMMANDS:")
            for command in self.get_commands():
                print(command)

    def get_commands(self):
        return [
            'sim', 
            'select', 
            'set', 
            'show', 
            'save', 
            'load', 
            'templates', 
            'examples', 
            'example', 
            'clear', 
            'exit'
        ]

if __name__ == '__main__':
    ElectricalSimulationCLI().cmdloop()

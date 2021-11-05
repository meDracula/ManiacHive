class SemanticHandler:
    @classmethod
    def syntax(cls, stdin, sprites_info):
        if len(stdin.split()) % 2 == 0:
            stdout_dict = cls.grammer(stdin, sprites_info)
        else:
            raise SyntaxError("In stdout: conform to id Direction EX '1 East'")

        return stdout_dict

    def grammer(stdin, sprites_info):
        commands = stdin.split()
        compas = ['East', 'West', 'North', 'South']
        stdout_dict = {}

        for i in range(0, len(commands), 2):
            if not(commands[i].isdigit() and commands[i+1] in compas):
                raise TypeError("The stdout: requiers a id number and a possible cardinal direction")

            unit = int(commands[i])

            if not(unit in sprites_info.keys()):
                raise KeyError("Must give a existing object id")

            if not(commands[i+1] in sprites_info[unit][1]):
                raise IndexError("Must give valid/possible cardinal directions")

            stdout_dict.update({unit: commands[i+1]})
        return stdout_dict

class Equation(object):

    def __init__(self, line=None):
        self.is_resolved = False
        if line:
            self.left_hand_side, self.right_hand_side = extract_LHS_and_RHS(line)
        else:
            self.left_hand_side = Variable()
            self.right_hand_side = RHS({}, 0)

    def resolve(self):
        result = self.right_hand_side.integer

        for variable in self.right_hand_side.variables.values():
            if variable.value:
                result += variable.value * variable.coef
            else:
                raise Exception("Not resolvable")

        self.left_hand_side.value = result
        self.is_resolved = True
        return self.left_hand_side

    def get_array_of_coefs(self, column_names):
        result = []
        for column_name in column_names:
            if column_name in self.right_hand_side.variables:
                result.append(self.right_hand_side.variables[column_name].coef)
            elif column_name == self.left_hand_side.name:
                result.append(self.left_hand_side.coef)
            else:
                result.append(0)
        return result, self.right_hand_side.integer - 2 * self.right_hand_side.integer


    def __str__(self):
        result = "" + self.left_hand_side.name + " = " + str(self.right_hand_side.integer)

        for variable in self.right_hand_side.variables.items():
            result += variable.name + " + "

        return result.strip(' + ')




class Variable(object):
    def __init__(self, name="", value=None, coef=1):
        self.name = name
        self.value = value
        self.coef = coef


class RHS(object):
    def __init__(self, variables, integer):
        self.variables = variables
        self.integer = integer

    def add_element(self, element):
        if isinstance(element, int):
            self.integer = self.integer +  element
        elif isinstance(element, Variable):
            if not element.name in self.variables:
                self.variables[element.name] = element
            else:
                self.variables[element.name].coef += 1
        else:
            raise Exception("Invalid input")



def parse_RHS(line):
    split_line = line.split("+")
    result = RHS({}, 0)
    for element_as_string in split_line:
        try:
            element = int(element_as_string)
        except ValueError:
            element = Variable(element_as_string.strip(), None)
        result.add_element(element)
    return result


def extract_LHS_and_RHS(line):
    split_line = line.split("=")
    if len(split_line) == 2:
        left_hand_side = Variable(split_line[0].strip(" "), coef=-1)
        right_hand_side = parse_RHS(split_line[1])
        return left_hand_side, right_hand_side
    else:
        raise Exception("Invalid input")

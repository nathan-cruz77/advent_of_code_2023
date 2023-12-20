import sys
from pprint import pp
from dataclasses import dataclass
import operator


@dataclass
class Rule:
    attribute: str
    operation: str
    value: int
    target: str

    def __post_init__(self):
        ops = {
            '>': operator.gt,
            '<': operator.lt
        }

        self._operator = ops[self.operation]

    def is_applicable(self, part):
        part_attr = part.__getattribute__(self.attribute)

        return self._operator(part_attr, self.value)


@dataclass
class Workflow:
    name: str
    rules: (Rule,)
    default_destination: str

    def process_part(self, part):
        rule = next((rule for rule in self.rules if rule.is_applicable(part)), None)

        if rule is None:
            return self.default_destination

        return rule.target


@dataclass
class Part:
    x: int
    m: int
    a: int
    s: int

    def sum_attr(self):
        return self.x + self.m + self.a + self.s


with open(sys.argv[1]) as file:
    input = file.read().splitlines()

separator_idx = input.index('')
instructions = input[:separator_idx]
input_parts = input[separator_idx + 1:]
workflows = {}

for instruction in instructions:
    name = instruction.split('{')[0]
    rule_desc = instruction.split('{')[-1].strip('}').split(',')
    rules = []

    for description in rule_desc[:-1]:
        attribute, operation = description[0], description[1]
        value, target = description[2:].split(':')

        rule = Rule(
            attribute=attribute,
            operation=operation,
            value=int(value),
            target=target
        )

        rules.append(rule)

    workflows[name] = Workflow(
        name=name,
        default_destination=rule_desc[-1],
        rules=rules
    )


parts = []
for part in input_parts:
    x, m, a, s = [int(item.split('=')[1]) for item in part.strip('{}').split(',')]

    p = Part(x=x, s=s, m=m, a=a)
    parts.append(p)

total_accepted = 0
for part in parts:
    current_workflow = workflows['in']

    while current_workflow not in ['A', 'R']:
        target = current_workflow.process_part(part)

        current_workflow = target

        if target in workflows:
            current_workflow = workflows[target]

    if current_workflow == 'A':
        total_accepted += part.sum_attr()

print(total_accepted)

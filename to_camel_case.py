import re

def to_camel_case(text):
    a = re.split('_|-', text)
    answer = [i.capitalize() for i in a]
    answer[0] = answer[0].lower() if a[0] != answer[0] else answer[0]
    print(''.join(answer))


to_camel_case('')
# '', "An empty string was provided but not returned"
to_camel_case("the_stealth_warrior")
# "theStealthWarrior", "to_camel_case('the_stealth_warrior') did not return correct value"
to_camel_case("The-Stealth-Warrior")
# "TheStealthWarrior", "to_camel_case('The-Stealth-Warrior') did not return correct value"
to_camel_case("A-B-C")
# "ABC", "to_camel_case('A-B-C') did not return correct value"
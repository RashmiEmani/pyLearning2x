# Single - 80% of time we use single inheritance
# Multiple
# Multi level
# Hierarchical
# Hybrid

# API, Web Automation -> 80% -> Single inheritance

# Multi level Inheritance
class GrandParent:

    def grandparent_method(self):
        return "Grandparent's Method"

class Parent(GrandParent):

    def parent_method(self):
        return "Parent's Method"


class Child(Parent):

    def child_method(self):
        return "Child's Method"

child = Child()
print(child.grandparent_method())
print(child.parent_method())
print(child.child_method())

parent = Parent()
print(parent.grandparent_method())
print(parent.parent_method())

grandparent = GrandParent()
print(grandparent.grandparent_method())

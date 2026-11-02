import alchemy

print("=== Alembic 1 ===")
print("Accessing the alchemy module using 'import alchemy'")
print("Testing create_air:")
print(alchemy.create_air())

print()
print("Now show that not all functions can be reached")
print("This will raise an exception!")
print("Testing the hidden create_earth:")
print(alchemy.create_earth())
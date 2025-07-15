def decorator(func):
    print("Primeiro")
    func()
    print("Depois")

@decorator
def main():
    print("OLá, mundo")
import sys
from .Settings import Settings
from .GenerateUser import GenerateUser

def main():
    settingPack = Settings()
    userGenerator = GenerateUser(settingPack)
    userGenerator.addUser("212341", "bryce", "smith")

if __name__ == '__main__':
    main()

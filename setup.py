from cx_Freeze import setup, Executable

executable = Executable("alien_invasion.py")

setup(
    name = "Alien Invasion",
    version = "1.0",
    description = "The best alien shooter game ever",
    executables = [executable]
)

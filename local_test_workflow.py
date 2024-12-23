import subprocess

print("Running Codespell:\n")

codespell_command = (
    "pipenv run codespell -L paket,nd --skip=./textstat/resources/**/"
    "easy_words.txt,./build/*,./textstat.egg-info/*,./.git/*,./tests/* "
    "--exclude-file=.codespellignorelines"
)
subprocess.run(codespell_command.split())

print("\n\nRunning Linter:\n")

lint_command = "pipenv run flake8 . --exclude=build/ --max-line-length=88"
subprocess.run(lint_command.split())

print("\n\nRunning Tests:\n")

test_command = "pipenv run pytest ."
subprocess.run(test_command.split())

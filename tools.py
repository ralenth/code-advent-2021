import os


def create_dir() -> None:
    dirs = [
        f for f in os.listdir('tasks') if os.path.isdir(os.path.join('tasks', f))
    ]
    days = [int(dir.replace('day', '')) for dir in dirs]
    new_day = max(days) + 1
    path = os.path.join('tasks', f'day{new_day}')
    os.mkdir(path)
    for subdir in [os.path.join(path, f'{new_day}_1'), os.path.join(path, f'{new_day}_2')]:
        os.mkdir(subdir)
        open(os.path.join(subdir, 'README.md'), 'w').close()
        open(os.path.join(subdir, 'input'), 'w').close()
        open(os.path.join(subdir, 'solution.py'), 'w').close()


create_dir()

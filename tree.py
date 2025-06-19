import os

def print_tree(root_path, indent="", ignore_dirs=None):
    if ignore_dirs is None:
        ignore_dirs = {'__pycache__', '.git', '.venv', 'env', 'venv', '.idea', '.vscode', 'migrations', 'staticfiles'}

    try:
        entries = sorted(os.listdir(root_path))
    except PermissionError:
        return  # Ігноруємо папки, до яких немає доступу

    for entry in entries:
        full_path = os.path.join(root_path, entry)
        if os.path.isdir(full_path):
            if entry in ignore_dirs:
                continue
            print(f"{indent}📁 {entry}")
            print_tree(full_path, indent + "    ", ignore_dirs)
        else:
            print(f"{indent}📄 {entry}")

# 👉 Вкажи свій шлях до Django-проєкту
project_path = r"E:\My project\MyEducation\Softserve\UA-130 Advanced Python with Django\Sprint 15 Django Forms\Task"

print(f"Структура проєкту в: {project_path}\n")
print_tree(project_path)

with open("structure.txt", "w", encoding="utf-8") as f:
    import sys
    original_stdout = sys.stdout
    sys.stdout = f
    print(f"Структура проєкту в: {project_path}\n")
    print_tree(project_path)
    sys.stdout = original_stdout

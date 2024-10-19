from beaupy import confirm, prompt, select, select_multiple
from rich.console import Console
import subprocess
import time
import os

console = Console()

def run_command(command, cwd=None):
    try:
        start_time = time.time()
        subprocess.run(command, shell=True, check=True, cwd=cwd)
        end_time = time.time()
        execution_time = end_time - start_time
        console.print(f"🚀 [bold cyan]Command executed in {execution_time:.2f} seconds[/bold cyan] 🎉")
        return True
    except subprocess.CalledProcessError:
        return False

def is_valid_app_name(name):
    if " " in name:
        console.print("😱 [bold red]The app name cannot contain spaces.[/bold red]")
        return False
    if any(c.isupper() for c in name):
        console.print("😱 [bold red]The app name cannot contain uppercase letters.[/bold red]")
        return False
    if os.path.exists(name):
        console.print(f"😱 [bold red]A directory with the name '{name}' already exists.[/bold red]")
        return False
    return True

def get_package_manager():
    package_managers = [
        "npm", "pnpm", "yarn", "bun"
    ]
    console.print("📦 Which package manager do you want to use? 🤖")
    return select(package_managers, cursor="🢧", cursor_style="cyan")

def get_app_name():
    while True:
        app_name = prompt("✍ Enter your app name (default: 'my-next-app') 🏷️", target_type=str) or "my-next-app"
        if is_valid_app_name(app_name):
            return app_name

def get_selected_features():
    options = [
        "TypeScript (--typescript)",
        "ESLint (--eslint)",
        "src/ directory (--src-dir)",
        "App Router (--app)",
        "Tailwind CSS (--tailwind)",
        'Import alias "@/*" (--import-alias)'
    ]
    feature_descriptions = {
        "TypeScript": "Add type safety and better IDE support",
        "ESLint": "Add code linting for better code quality",
        "src/ directory": "Use a src/ directory for better code organization",
        "App Router": "Use the new Next.js App Router (recommended)",
        "Tailwind CSS": "Add utility-first CSS framework",
        'Import alias "@/*"': "Add import aliases for cleaner imports"
    }
    
    default_selected = [0, 1, 3, 4]
    
    console.print("\n⚙️ Available features and their benefits:")
    for option in options:
        feature_name = option.split(" (")[0]
        console.print(f"• [cyan]{feature_name}[/cyan]: [yellow]{feature_descriptions[feature_name]}[/yellow]")
    
    console.print("\n⚙️ Select features you want to include (Space to toggle, Enter to confirm) 📝:")
    return select_multiple(options, tick_character='✔️', maximal_count=6, ticked_indices=default_selected)

def map_flags_to_selected_options(selected_options):
    flag_mapping = {
        "TypeScript": "--typescript",
        "ESLint": "--eslint",
        "src/ directory": "--src-dir",
        "App Router": "--app",
        "Tailwind CSS": "--tailwind",
        'Import alias "@/*"': '--import-alias "@/*"'
    }

    flags = []
    for option in flag_mapping:
        if any(option in selected_option for selected_option in selected_options):
            flags.append(flag_mapping[option])
        else:
            base_flag = flag_mapping[option].split()[0]
            flags.append(f"--no-{base_flag[2:]}")
    return flags

def build_create_command(app_name, package_manager, flags):
    if package_manager == "npm":
        base_command = f"npx create-next-app@latest {app_name} --use-npm"
    elif package_manager == "yarn":
        base_command = f"yarn create next-app {app_name} --use-yarn"
    elif package_manager == "pnpm":
        base_command = f"pnpm create next-app {app_name} --use-pnpm"
    else:
        base_command = f"bunx create-next-app {app_name} --use-bun"

    return f"{base_command} {' '.join(flags)}"

def perform_post_install_action(app_name, package_manager):
    action = select(["💻 Run VSCode", "📦 Install Packages", "🛑 Close Terminal"], cursor="🢧", cursor_style="cyan")
    
    if action == "💻 Run VSCode":
        run_command(f"code {app_name}")
    elif action == "📦 Install Packages":
        install_additional_packages(app_name, package_manager)
    elif action == "🛑 Close Terminal":
        console.print("👋 [bold green]Closing terminal...[/bold green]")
        run_command("exit")
def create_package_command(package_manager: str, dev_dependency: bool = False):
    dev_flag = ""
    if dev_dependency:
        if package_manager == "npm":
            dev_flag = "--save-dev"
        elif package_manager == "yarn":
            dev_flag = "-D"
        elif package_manager == "pnpm":
            dev_flag = "-D"
        elif package_manager == "bun":
            dev_flag = "-d"

    if package_manager == "npm":
        return f"npm install {dev_flag}"
    elif package_manager == "yarn":
        return f"yarn add {dev_flag}"
    elif package_manager == "pnpm":
        return f"pnpm add {dev_flag}"
    else:
        return f"bun add {dev_flag}"

def install_additional_packages(app_name, package_manager):
    available_packages = {
        "react-icons": {
            "description": "🎨 Popular icon library with 20+ icon sets. Includes Material, FontAwesome, and more.",
            "devDependency": None
        },
        "axios": {
            "description": "🌐 Promise-based HTTP client for API requests. Helps simplify HTTP requests in your app.",
            "devDependency": None
        },
        "next-auth": {
            "description": "🔐 Authentication solution for Next.js applications. Secure and easy to implement.",
            "devDependency": None
        },
        "zustand": {
            "description": "⚡ Small, fast, and scalable state management solution for React.",
            "devDependency": None
        },
        "date-fns": {
            "description": "📅 Modern JavaScript date utility library. Simple yet powerful date manipulation.",
            "devDependency": None
        },
        "bcrypt": {
            "description": "🔑 Secure password hashing library. Allows for secure password hashing and comparison.",
            "devDependency": "@types/bcrypt"
        },
        "qrious": {
            "description": "📱 JavaScript QR code generator. Generates QR codes easily for web apps.",
            "devDependency": None
        },
        "react-confetti": {
            "description": "🎉 Fun confetti effect for React apps. Adds celebration animations with confetti.",
            "devDependency": None
        },
        "react-google-recaptcha-v3": {
            "description": "🛡️ Google reCAPTCHA v3 integration for React. Protects your app from spam.",
            "devDependency": "@types/react-google-recaptcha"
        },
        "@emotion/react": {
            "description": "🎨 CSS-in-JS library. Allows you to style React components with dynamic CSS.",
            "devDependency": None
        },
        "@emotion/styled": {
            "description": "🎨 Styled components for Emotion. Provides a flexible API for component styling.",
            "devDependency": None
        },
        "@mui/material": {
            "description": "🧩 Material-UI component library for React. A comprehensive set of UI components.",
            "devDependency": None
        },
        "@mui/x-date-pickers": {
            "description": "📅 Date picker components for Material-UI. Adds flexible and customizable date pickers.",
            "devDependency": None
        },
        "@prisma/client": {
            "description": "💽 Type-safe database client for Prisma ORM. Automatically generated from your schema.",
            "devDependency": "prisma"
        },
    }

    console.print("\n📦 Available packages and their purposes:")
    for pkg, details in available_packages.items():
        dev_dep = f" (devDependency: {details['devDependency']})" if details['devDependency'] else ""
        console.print(f"• [cyan]{pkg}[/cyan]: [yellow]{details['description']}[/yellow]{dev_dep}")

    console.print("\n📦 Select packages you want to install (Space to toggle, Enter to confirm):")
    
    ticked_indices = list(range(len(available_packages)))
    selected_packages = select_multiple(list(available_packages.keys()), tick_character='✔️', ticked_indices=ticked_indices)
    
    if selected_packages:
        regular_packages = []
        dev_dependencies = []
        
        for pkg in selected_packages:
            regular_packages.append(f"{pkg}@latest")
            if available_packages[pkg]["devDependency"]:
                dev_dependencies.append(f"{available_packages[pkg]['devDependency']}@latest")

        install_commands = []
        
        if regular_packages:
            regular_install = f"{create_package_command(package_manager)} {' '.join(regular_packages)}"
            install_commands.append(regular_install)
        
        if dev_dependencies:
            dev_install = f"{create_package_command(package_manager,True)} {' '.join(dev_dependencies)}"
            install_commands.append(dev_install)

        for cmd in install_commands:
            console.print(f"🔧 [bold yellow]Running: {cmd}[/bold yellow] 🚀")
            run_command(cmd, cwd=app_name)
            
    else:
        console.print("🛑 [yellow]No packages selected for installation.[/yellow]")

def main():
    if confirm("🛠️ Do you want to create a new Next.js app? 🤔", default_is_yes=True):
        package_manager = get_package_manager()
        app_name = get_app_name()
        selected_features = get_selected_features()
        flags = map_flags_to_selected_options(selected_features)
        create_app_command = build_create_command(app_name, package_manager, flags)

        console.print("\n⚡️ [bold yellow]Command to be executed:[/bold yellow] ⚡️")
        if confirm("🛠️ Are you prepared to begin? 🤔", default_is_yes=True):
            console.print(f"💻 [green]{create_app_command}[/green]")

            console.print("\n🔨 [bold]Creating Next.js app and installing dependencies...[/bold] 🎉")
            success = run_command(create_app_command)

            if success:
                console.print(f"\n🎉 [bold green]✓ Successfully created Next.js project: {app_name}[/bold green]")
                perform_post_install_action(app_name, package_manager)
            else:
                console.print("\n😱 [bold red]✗ Failed to create the project. Please check the error message above.[/bold red]")
        else:
            console.print("🛑 [yellow]Installation cancelled![/yellow] 😅")
    else:
        console.print("🛑 [yellow]Installation cancelled![/yellow] 😅")

if __name__ == "__main__":
    main()

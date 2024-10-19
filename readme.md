# Next.js Project Setup CLI Tool 🚀

An interactive command-line interface (CLI) tool to streamline the creation of Next.js applications with custom configurations and package installations.

## Features ✨

- 🎯 Interactive project setup with customizable options
- 📦 Multiple package manager support (npm, pnpm, yarn, bun)
- ⚙️ Configurable project features:
  - TypeScript integration
  - ESLint configuration
  - Source directory structure
  - App Router setup
  - Tailwind CSS integration
  - Custom import aliases
- 📚 Automated package installation with popular libraries
- 💻 Post-installation actions (VSCode launch, package installation)

## Prerequisites 🛠️

- Python 3.6+
- Required Python packages:
  ```bash
  pip install beaupy rich
  ```
- Node.js and a package manager (npm, pnpm, yarn, or bun)

## Installation 📥

1. Clone this repository:
```bash
git clone <repository-url>
```

2. Install the required Python dependencies:
```bash
pip install beaupy rich
```

## Usage 💡

1. Run the script:
```bash
python setup_nextjs.py
```

2. Follow the interactive prompts to:
   - Choose your package manager
   - Set your app name
   - Select project features
   - Choose additional packages to install
   - Select post-installation actions

## Available Options 🎛️

### Package Managers
- npm
- pnpm
- yarn
- bun

### Project Features
- TypeScript support
- ESLint configuration
- src/ directory structure
- App Router
- Tailwind CSS
- Import alias (@/*)

### Available Packages for Installation
- react-icons - Icon library with 20+ icon sets
- axios - Promise-based HTTP client
- next-auth - Authentication solution
- zustand - State management
- date-fns - Date utility library
- bcrypt - Password hashing
- qrious - QR code generator
- react-confetti - Confetti effects
- react-google-recaptcha-v3 - reCAPTCHA integration
- @emotion/react & @emotion/styled - CSS-in-JS solution
- @mui/material - Material-UI components
- @mui/x-date-pickers - Date picker components
- @prisma/client - Database ORM

## Post-Installation Actions 🎉

After project creation, you can:
- Open the project in VSCode
- Install additional packages
- Close the terminal

## Error Handling 🔧

The tool includes validation for:
- Invalid app names (spaces, uppercase letters)
- Existing directory names
- Failed command executions

## Contributing 🤝

Feel free to submit issues and enhancement requests!

## License 📄

[MIT License](LICENSE)

## Author ✍️

[Mahdi Ebrahim pour]

---

Made with ❤️ for the Next.js community
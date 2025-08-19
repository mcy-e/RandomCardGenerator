# Random Card Generator 🎴

A sleek mobile application built with Python, Kivy, and KivyMD that allows users to create custom card pools and randomly select items from them. Perfect for games, decision-making, random selections, or any scenario where you need to pick items from custom lists.

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![Kivy](https://img.shields.io/badge/kivy-2.0+-green.svg)
![KivyMD](https://img.shields.io/badge/kivymd-latest-orange.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Platform](https://img.shields.io/badge/platform-Android%20%7C%20iOS%20%7C%20Desktop-lightgrey.svg)

## 📱 Screenshots

| ![Asset](Assets/MC%20Cards_1.jpg) | ![Asset](Assets/MC%20Cards_2.jpg) | ![Asset](Assets/MC%20Cards_3.jpg) |
|----------------------------------|----------------------------------|----------------------------------|
| ![Asset](Assets/MC%20Cards_4.jpg) | ![Asset](Assets/MC%20Cards_5.jpg) | ![Asset](Assets/MC%20Cards_6.jpg) |
| ![Asset](Assets/MC%20Cards_7.jpg) |                                  |                                  |


## ✨ Features

### 🎯 Core Functionality
- **Custom Pool Creation**: Create named pools with custom items
- **Random Selection**: Pick random items from selected pools
- **Pool Management**: Edit, delete, and organize your card pools
- **Persistent Storage**: Automatically saves pools between app sessions
- **Sequential Drawing**: Continue drawing cards until pool is empty

### 🎨 User Interface
- **Material Design**: Clean, modern UI using KivyMD
- **Dark Theme**: Eye-friendly dark theme with accent colors
- **Responsive Layout**: Optimized for mobile devices (360x640)
- **Intuitive Navigation**: Easy-to-use interface with clear visual feedback
- **Delete Mode**: Safe deletion mode to prevent accidental removals

### 📱 Mobile Optimized
- **Touch-Friendly**: Large buttons and touch targets
- **Scroll Support**: Smooth scrolling for large lists
- **Popup Dialogs**: Modal dialogs for editing and management
- **Keyboard Support**: Full keyboard input support

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.7+ installed on your system:

```bash
python --version
```

### Required Dependencies

```bash
pip install kivy
pip install kivymd
```

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/mcy-e/random-card-generator.git
   cd random-card-generator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python random_card_Generator.py
   ```

### Building for Mobile

#### Android (using Buildozer)
```bash
# Install buildozer
pip install buildozer

# Initialize buildozer
buildozer init

# Build APK
buildozer android debug
```

#### iOS (using kivy-ios)
```bash
# Install kivy-ios
pip install kivy-ios

# Build iOS app
toolchain build python3 kivy kivymd
```

## 📖 Usage Guide

### Creating Your First Pool

1. **Launch the app** and tap the **➕ Plus** button
2. **Name your pool** in the "Name" tab
3. **Add items** in the "List" tab:
   - Type an item name
   - Press Enter to add it
   - Repeat for all items
4. **Save** your pool

### Drawing Random Cards

1. **Tap the Shuffle button** 🔀 to enter shuffle mode
2. **Select a pool** from the dropdown menu
3. **Tap the Cards button** 🎴 to draw a random card
4. **Continue drawing** cards until the pool is empty

### Managing Pools

- **Edit pools**: Tap any pool button to modify its name or items
- **Delete pools**: Enable "Delete Mode" then tap pools to remove them
- **Edit items**: Tap any item in a pool to edit or remove it

## 🏗️ Architecture

### Project Structure
```
random-card-generator/
│
├── Assets/                      # Assets
├── random_card_Generator.py    # Main application file
├── Application.kv              # Kivy UI layout file
├── requirements.txt            # Python dependencies
└── README.md                  # This file
```

### Key Components

- **MainScreen**: Home screen with pool management
- **ShuffleScreen**: Card drawing and randomization interface
- **Pool Management**: Create, edit, and delete card pools
- **Data Persistence**: JSON-based storage system

### Technical Details

- **Framework**: Kivy + KivyMD
- **Language**: Python 3.7+
- **UI**: Material Design components
- **Storage**: JSON file-based persistence
- **Screen Resolution**: Optimized for 360x640 (mobile) , may also  work on pc

## 🔧 Configuration

The app includes several configurable options:

### Display Settings
```python
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')
Config.set('graphics', 'resizable', False) # set to to true for testing and you want a desktop layout

```

### Theme Customization
```python
self.theme_cls.theme_style = "Dark"
self.theme_cls.primary_palette = "Indigo"
self.theme_cls.accent_palette = "Amber"
```

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Getting Started
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guide
- Add comments for complex logic
- Test on multiple screen sizes
- Ensure mobile compatibility

### Bug Reports
Please use the GitHub issue tracker to report bugs. Include:
- Device/OS information
- Steps to reproduce
- Expected vs actual behavior
- Screenshots if applicable

## 📋 Requirements



```
kivy>=2.1.0
kivymd>=1.1.1
```

## 🔄 Version History

### v1.0.0 (Current)
- ✅ Initial release
- ✅ Basic pool creation and management
- ✅ Random card selection
- ✅ Data persistence
- ✅ Material Design UI
- ✅ Mobile optimization

### Planned Features

- 🔄 Import/Export functionality
- 🔄 Pool sharing capabilities
- 🔄 Statistics and history
- 🔄 Custom themes
- 🔄 Backup to cloud
- 🔄 More customization features

## 🐛 Known Issues

- Performance may slow with very large pools (>1000 items)
- Text truncation on very long item names
- Minor UI adjustments needed for tablet layouts

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Kivy Team** - For the amazing Python mobile framework
- **KivyMD Team** - For beautiful Material Design components
- **Python Community** - For continuous support and resources

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/mcy-e/RandomCardGenerator/issues)
- **Documentation**: [Wiki](https://github.com/mcy-e/RandomCardGenerator/wiki)


---

**Made with ❤️ and Python** 

*If you find this project useful, please consider giving it a ⭐ star on GitHub!*
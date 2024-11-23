# Custom Universe AI Chat

This is an interactive AI-powered chat application that allows users to create custom universes and characters, chat with AI characters, and even roleplay as their own characters in various scenarios. The app also provides predefined scenarios like "The Battle Against Knull", "Cosmic Invasion", and "The Multiverse Crisis".

### Features:

- **Create Custom Universes & Characters**: Build your own universe with custom characters and interact with them.
- **Multiple Scenarios**: Choose from predefined scenarios to shape your AI-powered story.
- **Multi-Character Mode**: Select multiple characters to chat with AI and create a group conversation.
- **Live Action Roleplay (LARP)**: Immerse yourself by roleplaying as one of the characters in your custom universe and interact with the AI.
- **AI Conversations**: Generate conversations between AI characters and users, with dynamic story-building.

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/arbab-kamal/Fictional-chat.git
cd Fictional-chat
```

# Setting Up the Virtual Environment (`myenv`)

This guide explains how to set up and activate the `myenv` virtual environment for this project, ensuring that all necessary dependencies are installed and the app works correctly.

## 1. Create and Activate the Virtual Environment

Before installing any dependencies, you need to create a virtual environment where the project dependencies will be isolated. Follow the steps below to set it up:

### For Windows

1. **Create the virtual environment** (if not already created):

   Open a terminal/command prompt and navigate to the root directory of your project:

   ```bash
   python -m venv myenv
   ```

### Steps in the README:

1. **Clone the Repository**: This section explains how to clone the project to your local machine.
2. **Install Dependencies**: Use `pip install` to install all the required packages listed in the `requirements.txt`.
3. **Create `.env` File**: It explains how to set up your `.env` file, where you will add the OpenAI API key.
4. **Running the App**: Shows the command to run the Streamlit app locally.
5. **Using the App**: Briefly explains how to interact with the app—create universes, select scenarios, chat with AI, and roleplay.
6. **Future Features**: Mentions potential features that can be added in the future, like chat exporting and user authentication.

### Additional Notes:

1. **Ensure `.env` is not committed**: It’s important to add `.env` to your `.gitignore` file to prevent the API key from being exposed on GitHub.
2. **requirements.txt**: Make sure your `requirements.txt` includes the necessary dependencies such as:
   ```txt
   streamlit
   openai
   python-dotenv
   ```

### Steps Breakdown:

1. **Create the Virtual Environment**:
   - For Windows, you use `python -m venv myenv` to create the environment.
   - For macOS/Linux, you use `python3 -m venv myenv`.
2. **Activate the Virtual Environment**:
   - For Windows: `myenv\Scripts\activate`
   - For macOS/Linux: `source myenv/bin/activate`
3. **Install Dependencies**:
   - The command `pip install -r requirements.txt` will install the dependencies.
4. **Deactivate the Virtual Environment**:

   - Simply run `deactivate` to exit the environment.

5. **Updating Dependencies**:
   - Whenever you add new dependencies, update the `requirements.txt` and run `pip install -r requirements.txt`.

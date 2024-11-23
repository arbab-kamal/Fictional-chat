import streamlit as st
import openai
from dotenv import load_dotenv
import os
from datetime import datetime

# Load environment variables from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize session state for chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
st.set_page_config(
    page_title="Enhanced Universe AI Chat & LARP",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)
# Predefined Universes
PREDEFINED_UNIVERSES = [
    {
        'name': 'Marvel Universe',
        'description': 'A universe of superheroes and villains.',
        'characters': [
            {'name': 'Spider-Man', 'description': 'A hero with spider-like abilities.'},
            {'name': 'Iron Man', 'description': 'A genius inventor in a powerful suit.'},
            {'name': 'Captain America', 'description': 'A super-soldier and symbol of freedom.'},
            {'name': 'Thor', 'description': 'The Norse god of thunder with a mighty hammer.'},
            {'name': 'Black Widow', 'description': 'A skilled spy and martial artist.'},
            {'name': 'Doctor Strange', 'description': 'The Sorcerer Supreme who defends Earth from mystical threats.'},
        ]
    },
    {
        'name': 'DC Universe',
        'description': 'A universe of iconic heroes and villains.',
        'characters': [
            {'name': 'Batman', 'description': 'A vigilante detective in Gotham.'},
            {'name': 'Superman', 'description': 'An alien with incredible powers.'},
            {'name': 'Wonder Woman', 'description': 'An Amazonian princess with superhuman strength.'},
            {'name': 'The Flash', 'description': 'A speedster who can move at incredible speeds.'},
            {'name': 'Green Lantern', 'description': 'A member of the Green Lantern Corps who wields a powerful ring.'},
            {'name': 'Aquaman', 'description': 'The king of Atlantis with the ability to communicate with sea life.'},
        ]
    },
    {
        'name': 'Harry Potter',
        'description': 'A magical world of wizards and witches.',
        'characters': [
            {'name': 'Harry Potter', 'description': 'The Boy Who Lived.'},
            {'name': 'Hermione Granger', 'description': 'A brilliant witch and loyal friend.'},
            {'name': 'Ron Weasley', 'description': 'A loyal friend of Harry with a sense of humor.'},
            {'name': 'Dumbledore', 'description': 'The wise and powerful Headmaster of Hogwarts.'},
            {'name': 'Voldemort', 'description': 'The Dark Lord who seeks to conquer the wizarding world.'},
            {'name': 'Severus Snape', 'description': 'A skilled potions master and double agent.'},
        ]
    },
    {
        'name': 'Star Wars',
        'description': 'A galaxy far, far away filled with Jedi and Sith.',
        'characters': [
            {'name': 'Luke Skywalker', 'description': 'A Jedi Knight who fights the Dark Side.'},
            {'name': 'Darth Vader', 'description': 'A Sith Lord with a tragic past.'},
            {'name': 'Princess Leia', 'description': 'A leader of the Rebellion and twin sister to Luke.'},
            {'name': 'Han Solo', 'description': 'A smuggler turned hero who helps the Rebellion.'},
            {'name': 'Yoda', 'description': 'A wise and ancient Jedi Master.'},
            {'name': 'Obi-Wan Kenobi', 'description': 'A legendary Jedi Knight and mentor to Luke.'},
        ]
    },
    {
        'name': 'Lord of the Rings',
        'description': 'A world of hobbits, elves, and epic quests.',
        'characters': [
            {'name': 'Frodo Baggins', 'description': 'A hobbit tasked with destroying the One Ring.'},
            {'name': 'Gandalf', 'description': 'A wise wizard and guide to the Fellowship.'},
            {'name': 'Aragorn', 'description': 'The heir to the throne of Gondor and skilled ranger.'},
            {'name': 'Legolas', 'description': 'An elf and expert archer.'},
            {'name': 'Gimli', 'description': 'A dwarf warrior with a strong heart and fierce loyalty.'},
            {'name': 'Gollum', 'description': 'A creature corrupted by the power of the One Ring.'},
        ]
    },
    {
        'name': 'Game of Thrones',
        'description': 'A world of dragons, knights, and political intrigue.',
        'characters': [
            {'name': 'Jon Snow', 'description': 'The bastard son of Ned Stark and a key figure in the battle for the Iron Throne.'},
            {'name': 'Daenerys Targaryen', 'description': 'The Mother of Dragons and last of the Targaryen dynasty.'},
            {'name': 'Tyrion Lannister', 'description': 'A witty and clever member of the Lannister family.'},
            {'name': 'Arya Stark', 'description': 'A skilled assassin and member of House Stark.'},
            {'name': 'Cersei Lannister', 'description': 'The manipulative queen who seeks power at all costs.'},
            {'name': 'Jaime Lannister', 'description': 'A knight with a complicated past and honor to redeem.'},
        ]
    },
    {
        'name': 'The Witcher',
        'description': 'A world of monsters, magic, and destiny.',
        'characters': [
            {'name': 'Geralt of Rivia', 'description': 'A monster hunter known as a Witcher, with extraordinary abilities.'},
            {'name': 'Yennefer of Vengerberg', 'description': 'A powerful sorceress and Geralt’s lover.'},
            {'name': 'Ciri', 'description': 'The Princess of Cintra and the Child of Surprise.'},
            {'name': 'Dandelion', 'description': 'A bard and close friend of Geralt.'},
            {'name': 'Triss Merigold', 'description': 'A sorceress and loyal ally of Geralt.'},
            {'name': 'Emhyr var Emreis', 'description': 'The Emperor of Nilfgaard and Ciri’s father.'},
        ]
    }
]


def select_universe():
    """Function to select and display universe information in the sidebar"""
    st.sidebar.title("Select Universe")
    
    # Get list of universe names including custom universe if it exists
    universe_names = [u['name'] for u in PREDEFINED_UNIVERSES]
    if 'custom_universe' in st.session_state:
        universe_names.append(st.session_state['custom_universe']['name'])
    
    # Create selectbox for universe selection
    selected_universe_name = st.sidebar.selectbox(
        "Choose a Universe",
        universe_names,
        help="Select a universe to interact with its characters"
    )
    
    # Find selected universe
    universe = next((u for u in PREDEFINED_UNIVERSES if u['name'] == selected_universe_name), None)
    
    # If selected universe is custom universe, use that instead
    if selected_universe_name == st.session_state.get('custom_universe', {}).get('name'):
        universe = st.session_state['custom_universe']
    
    # Display universe information
    if universe:
        st.sidebar.write("**Description:**", universe['description'])
        st.sidebar.write("**Available Characters:**")
        for char in universe['characters']:
            st.sidebar.write(f"- {char['name']}: {char['description']}")
    
    return universe

def create_custom_universe():
    """Function to create and manage custom universes"""
    st.subheader("Create Custom Universe")

    # Initialize session state for temp_characters if not already present
    if 'temp_characters' not in st.session_state:
        st.session_state.temp_characters = []
    
    # Input fields for universe name and description
    universe_name = st.text_input("Universe Name", help="Enter a name for your custom universe")
    universe_description = st.text_area("Universe Description", help="Describe your universe's setting and theme")

    # Display universe name and description after input
    if universe_name and universe_description:
        st.write(f"### Universe: {universe_name}")
        st.write(universe_description)

        # Define columns for character inputs and character list display
        col1, col2 = st.columns(2)
        
        with col1:
            char_name = st.text_input("Character Name", key="new_char_name")
            char_desc = st.text_area("Character Description", key="new_char_desc")
            char_backstory = st.text_area("Character Backstory", key="new_char_backstory")
            char_traits = st.text_input("Character Traits", key="new_char_traits")
            
            # Button to add character
            if st.button("Add Character"):
                if char_name and char_desc:
                    # Check for duplicates
                    if any(char['name'] == char_name for char in st.session_state.temp_characters):
                        st.warning(f"A character named '{char_name}' already exists.")
                    else:
                        st.session_state.temp_characters.append({
                            'name': char_name,
                            'description': char_desc,
                            'backstory': char_backstory,
                            'traits': char_traits
                        })
                        st.success(f"Added Character: {char_name}")
                else:
                    st.warning("Please provide both name and description.")
        
        # Display added characters
        with col2:
            st.write("### Added Characters")
            for idx, char in enumerate(st.session_state.temp_characters):
                st.write(f"**{char['name']}**: {char['description']}")
                if st.button(f"Remove {char['name']}", key=f"remove_{idx}"):
                    st.session_state.temp_characters.pop(idx)
                    st.script_runner.rerun()  # Rerun to reflect changes
        
        # Button to save universe
        if st.button("Save Universe"):
            if st.session_state.temp_characters:
                st.session_state['custom_universe'] = {
                    'name': universe_name,
                    'description': universe_description,
                    'characters': st.session_state.temp_characters.copy()
                }
                st.success("Universe saved successfully!")
                st.session_state.temp_characters = []  # Clear temporary characters
                
            else:
                st.warning("Please add at least one character before saving the universe.")


def generate_character_prompt(character, scenario):
    """Generate a detailed prompt for character behavior"""
    return f"""You are {character['name']}, {character['description']}. 
    You are in a scenario: {scenario}
    Maintain character consistency and speak in a way that reflects your personality and background.
    Consider your character's:
    - Typical speech patterns and vocabulary
    - Personal history and experiences
    - Relationships with other characters
    - Motivations and goals in this scenario
    
    Respond in character, using first-person perspective."""

def generate_ai_conversation(characters, scenario, previous_messages=None):
    """Generate more contextual and character-driven conversations"""
    system_prompt = {
        "role": "system",
        "content": f"""You are orchestrating a conversation between characters in the scenario: {scenario}.
        Generate natural, in-character dialogue that:
        - Maintains consistent character voices
        - Advances the story naturally
        - References the current scenario
        - Builds on previous conversation if any
        - Includes both dialogue and minimal action descriptions in *asterisks*
        Format: Character Name: Dialogue *actions*"""
    }
    
    messages = [system_prompt]
    
    # Add previous conversation context if it exists
    if previous_messages:
        for msg in previous_messages[-5:]:  # Include last 5 messages for context
            messages.append({"role": "assistant", "content": msg})
    
    # Add character introductions
    for char in characters:
        char_prompt = generate_character_prompt(char, scenario)
        messages.append({"role": "system", "content": char_prompt})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.8,
        max_tokens=400,
        presence_penalty=0.6,  # Encourage varied responses
        frequency_penalty=0.3,  # Reduce repetition
    )
    return response['choices'][0]['message']['content']

def chat_with_ai(universe):
    """Interactive real-time chat with AI characters."""
    st.subheader("Chat with AI Characters")

    if not universe or not universe['characters']:
        st.warning("No characters available in this universe.")
        return

    # Initialize session states
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'last_speaker' not in st.session_state:
        st.session_state.last_speaker = "User"  # Start with user

    # Character and scenario setup
    col1, col2 = st.columns(2)
    with col1:
        characters = st.multiselect(
            "Select AI Characters",
            options=[c['name'] for c in universe['characters']],
            help="Choose one or more characters to chat with."
        )
    with col2:
        scenario = st.text_input(
            "Scenario",
            help="Describe the scenario or context for the conversation."
        )

    # Display chat history
    chat_container = st.container()
    with chat_container:
        for message in st.session_state.chat_history:
            st.markdown(message)

    # Message input
    user_message = st.text_input("Your Message", placeholder="Type your message here...")

    if st.button("Send Message"):
        if not characters:
            st.warning("Please select at least one character to chat with.")
            return
        if not user_message:
            st.warning("Please type a message before sending.")
            return

        # Add user message to chat history
        timestamp = datetime.now().strftime("%H:%M")
        st.session_state.chat_history.append(f"**You [{timestamp}]:** {user_message}")
        st.session_state.last_speaker = "AI"

        # Generate AI response
        selected_characters = [c for c in universe['characters'] if c['name'] in characters]
        ai_response = generate_ai_conversation(
            selected_characters,
            scenario,
            st.session_state.chat_history
        )
        st.session_state.chat_history.append(f"**AI [{timestamp}]:** {ai_response}")
        st.session_state.last_speaker = "User"  # Switch back to user

    # Clear chat history button
    if st.button("Clear Chat History"):
        st.session_state.chat_history = []
        st.session_state.last_speaker = "User"

def live_action_roleplay(universe):
    st.subheader("Enhanced Live Action Roleplay")

    # Initialize session state
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    if not universe or not universe['characters']:
        st.warning("No characters available in this universe.")
        return

    col1, col2 = st.columns(2)

    with col1:
        characters = st.multiselect(
            "Select Characters for LARP",
            options=[c['name'] for c in universe['characters']],
            help="Choose at least two characters for the roleplay session"
        )

    with col2:
        scenario_input = st.text_input(
            "Enter Scenario or Choose Predefined One",
            help="Enter a custom scenario or leave blank to select a predefined one"
        )
        predefined_scenarios = [
            "The Battle Against Knull",
            "Cosmic Invasion",
            "The Multiverse Crisis",
            "A Quiet Moment in the Base",
            "Training Day",
            "Mission Briefing"
        ]
        scenario = scenario_input if scenario_input else st.selectbox(
            "Predefined Scenarios",
            predefined_scenarios
        )

    # Display Chat History
    chat_container = st.container()
    with chat_container:
        for message in st.session_state.chat_history:
            st.markdown(message)

    # Message Input
    user_message = st.text_input("Your Message", placeholder="Type your message here...")

    # Start/Continue Button
    if st.button("Send Message"):
        if len(characters) < 2:
            st.warning("Please select at least two characters for the LARP session.")
            return
        if not user_message:
            st.warning("Please type a message to continue.")
            return

        # Add user message to chat history
        timestamp = datetime.now().strftime("%H:%M")
        st.session_state.chat_history.append(f"**You [{timestamp}]:** {user_message}")

        # Generate AI responses
        selected_characters = [c for c in universe['characters'] if c['name'] in characters]
        ai_response = generate_ai_conversation(selected_characters, scenario, st.session_state.chat_history)
        st.session_state.chat_history.append(f"**AI [{timestamp}]:** {ai_response}")

    # Clear Chat History Button
    if st.button("Clear Chat"):
        st.session_state.chat_history = []



def main():
    st.title("Enhanced Universe AI Chat")
    
    action = st.selectbox("Choose Action", [
        "Chat with AI",
        "Create Custom Universe",
        "Live Action Roleplay"
    ])
    
    if action == "Create Custom Universe":
        create_custom_universe()
        
    universe = select_universe()
    
    if action == "Chat with AI":
        chat_with_ai(universe)
    elif action == "Live Action Roleplay":
        live_action_roleplay(universe)

if __name__ == "__main__":
    main()
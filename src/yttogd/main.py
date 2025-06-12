import streamlit as st
from src.yttogd.ui.streamlitui.load_ui import LoadStreamlitUI
from src.yttogd.LLMS.groq_llm import GroqLLM
from src.yttogd.Prompt.ShikarPrompt import ShikharPrompt
# from src.sdlc.graph.graph_builder import GraphBuilder
# from src.sdlc.ui.streamlitui.display_result import DisplayResultStreamlit

# MAIN Function START
def load_sdlc_app():
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input from the UI.")
        return
    
    transcription = st.text_input("Enter a transcript")

    if st.button("Submit"):
        try:
            obj_llm_config = GroqLLM(user_controls_input=user_input)
            model = obj_llm_config.get_llm_model()
                
            if not model:
                st.error("Error: LLM model could not be initialized.")
                return

            try:
                summary_response = model.invoke(f"Summarize the following transcript {transcription} into a short and clear story summary. Focus on the key events and highlight the main points. The transcript is a story, so ensure the summary captures the full narrative in a way that is easy to understand.")
                st.write(summary_response.content)

                st.write(" ")
                st.write(" ")
                st.write(" ")

                game_ideas_response = model.invoke(f"""After reading the following transcript{transcription} and its summary {summary_response.content}, generate 10 unique game ideas inspired by the story. Each idea must include the following structured information in square-box format:
                [Game Title]
                [Genre: Hyper Casual / Adventure / Puzzle / etc.]
                [Core Gameplay Idea: Explain in 1–2 lines]
                [Target Audience]
                [Platform: Mobile / PC / Web / Console]
                [Art Style: Cartoon / Realistic / Stylized / etc.]
                [Monetization: Ads / IAP / Subscription / Premium / None]
                Keep the descriptions short but clear. The ideas should be creative, practical, and inspired directly from the story themes or events.""")
                st.write(game_ideas_response.content)

                st.write(" ")
                st.write(" ")
                st.write(" ")
                
                gdd_response = model.invoke(ShikharPrompt.prompt +" "+game_ideas_response.content)
                st.write(gdd_response.content)
            except Exception as e:
                st.error(f"Error: Graph setup failed - {e}  \n\n Please refresh the page and try again.")
                return
                

        except Exception as e:
            raise ValueError("Please add Groq API key in the sidebar")

            

        

   

    
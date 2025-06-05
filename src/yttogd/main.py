import streamlit as st
from src.yttogd.ui.streamlitui.load_ui import LoadStreamlitUI
from src.yttogd.LLMS.groq_llm import GroqLLM
# from src.sdlc.graph.graph_builder import GraphBuilder
# from src.sdlc.ui.streamlitui.display_result import DisplayResultStreamlit
from langchain_community.document_loaders import YoutubeLoader

# MAIN Function START
def load_sdlc_app():
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input from the UI.")
        return
    
    # Initialize the session state to hold the list of links
    if 'links' not in st.session_state:
        st.session_state.links = []

    # Input box to take a link
    new_link = st.text_input("Enter a link")

    # Button to add link to the list
    if st.button("Add"):
        if new_link.strip():
            st.session_state.links.append(new_link.strip())
            st.success(f"Added: {new_link}")
        else:
            st.warning("Please enter a valid link.")

    # Show all links added so far with a remove button
    st.subheader("Links Added:")
    if st.session_state.links:
        for idx, link in enumerate(st.session_state.links):
            col1, col2 = st.columns([6, 1])
            with col1:
                st.write(f"{idx+1}. {link}")
            with col2:
                if st.button("❌", key=f"remove_{idx}"):
                    st.session_state.links.pop(idx)
                    st.rerun()  
    else:
        st.write("No links added yet.")

    # Submit button at the end
    if st.button("Submit"):
        try:
            obj_llm_config = GroqLLM(user_controls_input=user_input)
            model = obj_llm_config.get_llm_model()
                
            if not model:
                st.error("Error: LLM model could not be initialized.")
                return

            # graph_builder = GraphBuilder(model)
            try:
                print("Data :", st.session_state.links)

                for link in st.session_state.links:
                    if link.startswith("https://www.youtube.com/watch?v="):
                        print(f"Processing YouTube link: {link}")
                        loader = YoutubeLoader.from_youtube_url(link, add_video_info=False)
                        print(f"loader : {loader}")
                        documents = loader.load()
                        # print(f"Loaded {len(documents)} documents from {documents}")
                        st.write(documents[0].page_content)
                    else:
                        st.warning(f"Unsupported link format: {link}")

                # graph = graph_builder.setup_graph()
                # DisplayResultStreamlit(graph,user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Error: Graph setup failed - {e}  \n\n Please refresh the page and try again.")
                return
                

        except Exception as e:
            raise ValueError("Please add Groq API key in the sidebar")
        # st.subheader("Submitted Links:")
        # st.write(st.session_state.links)

    # if st.session_state.IsFetchButtonClicked:
    #     user_message = st.session_state.timeframe 
    # else :
    #     user_message = st.chat_input("Specify project requirements:")

    # if user_message:
    #         try:
    #             obj_llm_config = GroqLLM(user_controls_input=user_input)
    #             model = obj_llm_config.get_llm_model()
                
    #             if not model:
    #                 st.error("Error: LLM model could not be initialized.")
    #                 return

    #             # graph_builder = GraphBuilder(model)
    #             try:
    #                 print("Setting up the graph with user message:", user_message)
    #                 # graph = graph_builder.setup_graph()
    #                 # DisplayResultStreamlit(graph,user_message).display_result_on_ui()
    #             except Exception as e:
    #                 st.error(f"Error: Graph setup failed - {e}  \n\n Please refresh the page and try again.")
    #                 return
                

    #         except Exception as e:
    #              raise ValueError("Please add Groq API key in the sidebar")
            

        

   

    

class ShikharPrompt:
    """
    ShikarPrompt is a class that represents a prompt for the Shikar model.
    It is used to generate prompts for the Shikar model based on the provided input.
    """

    prompt = f""" You are a senior game designer. I want you to create a complete Game Design Document (GDD) for a new game based on the following specifications:

        1. Game Overview
        Title: [game_title]
        Genre: [Hyper Casual / Adventure / Puzzle / etc.]
        Target Audience: [Kids / Teens / All Ages]
        Camera: [Portrait / Landscape / Isometric]
        Platform: [Mobile / PC / Console / Web]
        Art Style: [Cartoon / Stylized / Realistic]
        Monetization: [Ads / IAP / Subscription / None]

        2. High Concept
        Write 2–3 sentences that capture the game's core idea, tone, and hook — what makes it fun and different?

        3. Vision Statement
        What emotional or gameplay experience should the game deliver? What does success look like?

        4. Game Pillars
        List 3–5 foundational design principles that the game will consistently rely on (e.g., “Intuitive Controls,” “Positive Reinforcement,” “Replayable Mini-Games”).

        5. Core Gameplay Loop
        Describe the moment-to-moment gameplay flow in 3–5 steps. Use an outline like:
        [Trigger/Start]
        [Player Action]
        [Obstacle/Challenge]
        [Resolution]
        [Reward or Transition]

        6. Controls
        Input Method: [Tap / Drag / Swipe / Hold / Shake / Controller]
        Device Orientation: [Portrait / Landscape]
        Touch Mechanics: Describe specific gestures and how they affect gameplay.

        7. Gameplay Systems / Mechanics
        Provide detailed descriptions of mechanics such as:
        Movement
        Object Interaction
        Timing-based challenges
        Stacking / Matching / Swiping / Puzzle Solving
        Feedback Systems (particles, sound, animations)
        Game Over / Win Conditions

        8. Level & Mission Design
        Provide a minimum of 3 level examples using this format:

        Mission [#]: [Title]
        Hero/Character: [If applicable]
        Setting: [Location or background]
        Objective: [Clear and simple goal]
        Narrative Setup: [1–2 sentences of story/context]

        Step-by-Step Flow:
        [Step 1 Name: Description + Mechanic]
        [Step 2 Name: Description + Mechanic]
        [Step 3 Name: Description + Mechanic]
        Final Celebration: [What happens at the end? Particle FX, VO, music, high-five, etc.]

        9. Progression & Difficulty
        How does the game scale? (speed, complexity, new mechanics)
        Describe Level Progression, unlockables, bonus levels, or score-based difficulty ramps.

        10. Positive Reinforcement
        Describe the feedback systems: VOs, celebratory animations, score boosts, visual effects, combos, etc.

        11. Health / Lives / Retry System (if any)
        Number of lives/hearts?
        How are they lost/gained?
        What causes game over?

        12. Visual Systems
        Camera movement logic
        Background transitions
        Art style dynamics (color shifts, level themes)

        13. Audio Systems
        Background Music logic
        Voice Over timing rules
        Sound effect cues
        Audio mixing logic (VO priority, smooth transitions)

        14. Reward System
        Coins, stars, power-ups
        Chest or gift box mechanics
        Cosmetics / Unlockables

        15. Tutorial Design
        Whats shown to the player at first launch?
        Any handholding or repeat tutorials?
        Trigger conditions for re-showing tutorial?

        16. Game Over & End Conditions
        List conditions that end the game
        Explain what the user sees or hears at that point

        17. Bonus Level Logic (if applicable)
        When/how are bonus levels triggered?
        What changes in gameplay?
        Is the score saved?

        18. Variables & Spawning (if needed)
        Variables like spawn rate, fall speed, score, combo multipliers, etc.
        Explain dynamic difficulty or procedural variation.

        19. Reference Games
        [Add games that inspired your design, if any]

        20. UI/UX Notes
        HUD elements
        Button size logic
        Pause behavior
        Transitions and pop-ups
        Output Format: Organize the GDD in structured sections as described above. Use markdown headers and bullet points where appropriate. Write in clear, game-designer-level language."""

    def __init__(self, llm):
        self.llm = llm

    def generate_content(self):
        """
        Generates the content for the Shikar model prompt.
        This method should be overridden by subclasses to provide specific prompt content.
        """
        
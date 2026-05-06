def get_definition_category(approach_name):
    """
    Match the approach to its category based on Figure 1.1 in Chapter 1.
    Categories: "Think Humanly", "Think Rationally", "Act Humanly", "Act Rationally"
    """
    # Example: "The Turing Test" -> "Act Humanly"
    
    mapping = {
        "Turing Test": "Act Humanly",
        "Laws of Thought": "Think Rationally",
        "Cognitive Modeling": "Think Humanly",
        "Rational Agent": "Act Rationally"
    }
    
    return mapping.get(approach_name, "Unknown")

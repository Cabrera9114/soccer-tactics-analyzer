from utils.ai_analysis import generate_ai_analysis


def generate_coaching_feedback(formation, width, depth, compactness, spacing_metrics):
    base_text = generate_ai_analysis(formation, width, depth, compactness)

    x_spacing = spacing_metrics["avg_x_spacing"]
    y_spacing = spacing_metrics["avg_y_spacing"]

    coaching_notes = []

    if x_spacing > 8:
        coaching_notes.append("The team appears vertically stretched, so tighter distances between lines may improve compactness.")
    else:
        coaching_notes.append("The vertical spacing looks fairly compact, which can help defensive balance.")

    if y_spacing > 7:
        coaching_notes.append("The horizontal spread is strong, which supports width in possession.")
    else:
        coaching_notes.append("The shape looks narrow, so wider positioning could improve ball circulation.")

    coaching_notes.append("Consider adjusting line spacing depending on whether the goal is to press high or defend compactly.")

    return base_text + "\n\nCoaching Feedback:\n- " + "\n- ".join(coaching_notes)
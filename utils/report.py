from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(filename, formation, width, depth, compactness, spacing_metrics, ai_text):
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("Soccer Tactics Analyzer Report", styles["Title"]))
    story.append(Spacer(1, 12))

    story.append(Paragraph(f"Formation: {formation}", styles["Normal"]))
    story.append(Paragraph(f"Team Width: {width:.2f}", styles["Normal"]))
    story.append(Paragraph(f"Team Depth: {depth:.2f}", styles["Normal"]))
    story.append(Paragraph(f"Compactness: {compactness:.2f}", styles["Normal"]))
    story.append(Paragraph(f"Average X Spacing: {spacing_metrics['avg_x_spacing']:.2f}", styles["Normal"]))
    story.append(Paragraph(f"Average Y Spacing: {spacing_metrics['avg_y_spacing']:.2f}", styles["Normal"]))
    story.append(Spacer(1, 12))

    story.append(Paragraph("AI Tactical Analysis", styles["Heading2"]))
    story.append(Paragraph(ai_text.replace("\n", "<br/>"), styles["Normal"]))

    doc.build(story)
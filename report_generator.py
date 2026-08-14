from datetime import datetime
from fpdf import FPDF

def generate_report_pdf(target_role, score, found_skills, matched, missing, roadmap, chart_image_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 10, "AI Resume Analyzer - Report", ln=True)

    pdf.set_font("Helvetica", "", 10)
    pdf.cell(0, 8, f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}", ln=True)
    pdf.ln(4)

    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(0, 8, f"Target Role: {target_role}", ln=True)
    pdf.cell(0, 8, f"Match Score: {score}%", ln=True)
    pdf.ln(4)

    def write_section(title, items):
        pdf.set_font("Helvetica", "B", 12)
        pdf.cell(0, 8, title, ln=True)
        pdf.set_font("Helvetica", "", 10)
        if items:
            for item in items:
                pdf.cell(0, 6, f"- {item}", ln=True)
        else:
            pdf.cell(0, 6, "- None", ln=True)
        pdf.ln(3)

    write_section("Skills Found:", found_skills)
    write_section("Matched Skills:", list(matched))
    write_section("Missing Skills:", list(missing))
    write_section("Suggested Roadmap:", roadmap)

    # embed the chart image
    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(0, 8, "Match Score Chart:", ln=True)
    pdf.image(chart_image_path, x=10, w=180)
    pdf.ln(4)

    pdf.set_font("Helvetica", "I", 9)
    pdf.multi_cell(0, 6, "Note: This score is an estimate for guidance only, not a hiring decision.")

    return bytes(pdf.output(dest="S"))
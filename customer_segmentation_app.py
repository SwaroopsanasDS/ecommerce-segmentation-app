import gradio as gr

# Prediction function with 4 customer segments
def predict_customer(recency, frequency, monetary):
    score = recency * 0.5 + frequency * 0.3 + monetary * 0.2
    if score < 20:
        return "🧊 Churned Customer"
    elif score < 50:
        return "😐 Mid-Value Customer"
    elif score < 80:
        return "💰 Low-Value Customer"
    else:
        return "🌟 High-Value Customer"

# Custom futuristic CSS
css = """
.gr-button {
    background: linear-gradient(90deg, #6e00ff, #00e0ff);
    color: #fff;
    font-weight: bold;
    border-radius: 12px;
    padding: 12px 20px;
    font-size: 16px;
    box-shadow: 0 0 10px rgba(110, 0, 255, 0.8);
    transition: 0.4s ease;
}
.gr-button:hover {
    background: linear-gradient(270deg, #00e0ff, #6e00ff);
    transform: scale(1.05);
    box-shadow: 0 0 20px rgba(0, 224, 255, 1);
}

h1, h2, h3, .gr-textbox label, .gr-slider label {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: #ffffff;
    text-shadow: 0 0 5px rgba(0, 255, 255, 0.6);
}

.output-textbox {
    font-size: 20px;
    font-weight: bold;
    color: #00ffff;
    border: 2px solid #00ffff;
    padding: 12px;
    border-radius: 10px;
    background-color: #1a1a1a;
}

body {
    background-color: #111;
}
"""

# Build the app
with gr.Blocks(css=css, theme=gr.themes.Soft()) as demo:
    gr.Markdown("<h1 style='text-align: center;'>Customer Segmentation App</h1>")
    gr.Markdown("### 🔍 Adjust the RFM values to see which segment your customer belongs to.")

    with gr.Row():
        recency = gr.Slider(minimum=0, maximum=100, label="📅 Recency (days since last purchase)")
    with gr.Row():
        frequency = gr.Slider(minimum=0, maximum=100, label="🔁 Frequency (purchase count)")
    with gr.Row():
        monetary = gr.Slider(minimum=0, maximum=2000, label="💵 Monetary (total spend in $)")

    predict_btn = gr.Button("🔮 Predict Customer Segment")
    output = gr.Textbox(label="🎯 Prediction Result", elem_classes="output-textbox")

    predict_btn.click(fn=predict_customer, inputs=[recency, frequency, monetary], outputs=output)

# Launch the app locally
demo.launch()
